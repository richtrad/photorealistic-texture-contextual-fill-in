# Provenance

## Article archive

| Field | Value |
| --- | --- |
| Title | Photorealistic Texture Contextual Fill-In |
| Author | Radek Richtr |
| Venue | *Heritage*, 8(1), article 9, 2025 |
| DOI | [10.3390/heritage8010009](https://doi.org/10.3390/heritage8010009) |
| Version | Local copy of the published PDF; 22 PDF pages |
| PDF SHA-256 | `246832bb68ad01386482b46f51133decdc151aa36902b057064130721a924285` |

The PDF in `paper/` is preserved as received from the local publication audit.
The public article page and an institutional mirror are linked from the
README. The repository does not silently replace the version of record with a
newly typeset or edited manuscript.

## Figure extraction

`tools/extract_pdf_figures.py` uses `pypdf` and Pillow to decode raster objects
from the PDF pages containing Figures 1–8 and 10. It performs no resampling,
retouching, colour correction, generative enhancement, or caption editing.
The output manifest records the source PDF hash, PDF page, embedded object
name, dimensions, output path, and SHA-256 for every extracted file.

Figure 9 is vector-drawn in the PDF and is intentionally left in the original
PDF rather than being rasterised into this archive.

## Working PSD layer export

A separate layer export was built from the directly verified local `cp_1.psd`
working file. The source PSD binary stays outside the public repository. The
four exported PNGs in `data/layers/working_psd_exports/` were produced with
`psd-tools` 1.19.0 by rasterising visible top-level layers, preserving native
layer crops, alpha, and canvas bounds. No generative enhancement or manual
retouching was applied. The machine-readable manifest in
`metadata/psd-layer-manifest.json` records the source basename, byte size,
SHA-256, layer names/kinds/bounds, output path, dimensions, and output hash.

The `cp_1` source is visually and structurally mapped to the article's Figure
7/10 case: its four visible layers are the historical source and three
successive contextual-fill/colourisation/detail states. Additional local
working candidates were intentionally left out of this public commit until
their exact article mapping and rights are checked. The raw supporting data
described in the article remain available from the authors on request rather
than being claimed here as a complete public dataset.

## Recovered material boundary

The original LaTeX project was not found in the available local archive. The
text file in `paper/` is a convenience extraction from the PDF and is not a
source reconstruction. The article reports that raw supporting data are
available from the authors on request; no raw photo collection or user-test
dataset is included or claimed to be publicly released here.
