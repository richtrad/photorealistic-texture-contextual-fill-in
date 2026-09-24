"""Extract the article's raster figure assets from the version-of-record PDF.

The PDF is the authoritative source. This script does not resample or retouch
the images; it only asks pypdf to decode the embedded raster objects and writes
an auditable manifest with their source page, object name, dimensions, and hash.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

Image.MAX_IMAGE_PIXELS = None

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "paper" / "Photorealistic_Texture_Contextual_Fill-In_Heritage_2025.pdf"
OUT = ROOT / "figures" / "pdf_extracted"
MANIFEST = ROOT / "metadata" / "figure-extraction-manifest.json"

# The article's raster figure pages. Figure 9 is vector-drawn in the PDF and
# is therefore intentionally not represented as a raster extraction here.
FIGURE_PAGES = {
    1: 3,
    2: 5,
    3: 6,
    4: 9,
    5: 12,
    6: 13,
    7: 16,
    8: 17,
    10: 21,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(str(PDF))
    rows: list[dict[str, object]] = []

    for figure, page_number in FIGURE_PAGES.items():
        page = reader.pages[page_number - 1]
        for index, image in enumerate(page.images, start=1):
            suffix = Path(image.name).suffix.lower() or ".bin"
            output = OUT / f"figure-{figure:02d}_asset-{index:02d}{suffix}"
            image.image.save(output)
            rows.append(
                {
                    "figure": figure,
                    "pdf_page": page_number,
                    "pdf_object": image.name,
                    "path": output.relative_to(ROOT).as_posix(),
                    "format": suffix.removeprefix("."),
                    "width": image.image.width,
                    "height": image.image.height,
                    "sha256": sha256(output),
                }
            )

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(
        json.dumps(
            {
                "source_pdf": PDF.relative_to(ROOT).as_posix(),
                "source_pdf_sha256": sha256(PDF),
                "figure_pages": FIGURE_PAGES,
                "vector_figure_pages": {9: 18},
                "extracted_images": rows,
                "transformations": ["PDF raster-object decode only", "no resampling", "no retouching"],
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
