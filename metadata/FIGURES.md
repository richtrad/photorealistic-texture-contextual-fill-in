# Figure inventory

This inventory records where the article figures occur in the 22-page PDF and
which figures have raster objects available in `figures/pdf_extracted/`.

| Article figure | PDF page | Archive representation |
| --- | ---: | --- |
| 1 | 3 | 2 decoded raster objects |
| 2 | 5 | 2 decoded raster objects |
| 3 | 6 | 2 decoded raster objects |
| 4 | 9 | 3 decoded raster objects |
| 5 | 12 | 2 decoded raster objects |
| 6 | 13 | 4 decoded raster objects |
| 7 | 16 | 8 decoded raster objects |
| 8 | 17 | 2 decoded raster objects |
| 9 | 18 | Vector drawing retained in the PDF; no raster extraction |
| 10 | 21 | 1 decoded raster object |

The files are named `figure-XX_asset-YY.jpg`. They are the embedded raster
objects as decoded by `tools/extract_pdf_figures.py`; they are not AI-upscaled
or otherwise visually altered. Use the original PDF for page layout, labels,
vector graphics, and captions. The complete per-file dimensions and hashes are
in [`figure-extraction-manifest.json`](figure-extraction-manifest.json).
