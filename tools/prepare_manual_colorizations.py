"""Create GitHub-sized presentation copies of manual-colourisation images.

The source PNG/JPEG files remain outside the public repository. This tool only
resizes them to a bounded maximum dimension and writes losslessly compressed
PNG outputs, preserving RGB/RGBA mode where possible. A manifest records the
source and output hashes and dimensions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-dimension", type=int, default=4096)
    parser.add_argument("--skip-existing", action="store_true")
    args = parser.parse_args()

    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    for source in sorted(args.source.iterdir()):
        if source.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        target = output / f"{source.stem}.png"
        with Image.open(source) as image:
            source_size = list(image.size)
            source_mode = image.mode
            output_image = image.copy()
            output_image.thumbnail(
                (args.max_dimension, args.max_dimension), Image.Resampling.LANCZOS
            )
            if not (args.skip_existing and target.exists() and target.stat().st_size > 0):
                output_image.save(target, format="PNG", optimize=True, compress_level=9)
            rows.append(
                {
                    "source_file": source.name,
                    "source_size_bytes": source.stat().st_size,
                    "source_sha256": sha256(source),
                    "source_dimensions": source_size,
                    "source_mode": source_mode,
                    "output_file": target.name,
                    "output_dimensions": list(output_image.size),
                    "output_mode": output_image.mode,
                    "output_size_bytes": target.stat().st_size,
                    "output_sha256": sha256(target),
                }
            )
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "max_dimension": args.max_dimension,
        "resampling": "Pillow LANCZOS",
        "encoding": "PNG optimize=True compress_level=9",
        "transformation": [
            "bounded downscaling for a GitHub-safe presentation copy",
            "no colour correction, retouching, generative enhancement, or content edits",
            "RGB/RGBA source mode preserved",
        ],
        "files": rows,
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"sources={len(rows)} output={output}")


if __name__ == "__main__":
    main()
