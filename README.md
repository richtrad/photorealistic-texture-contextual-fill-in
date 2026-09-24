# Photorealistic Texture Contextual Fill-In

Public archival companion for **Radek Richtr**, “Photorealistic Texture Contextual Fill-In,” *Heritage* 8(1), 9 (2025).

- [Version of record at MDPI](https://www.mdpi.com/2571-9408/8/1/9)
- [DOI: 10.3390/heritage8010009](https://doi.org/10.3390/heritage8010009)
- [Institutional PDF mirror](https://most.vugtk.cz/media/doc/publikace/Richter-Photorealistic_Texture_Contextual_Fill-In.pdf)
- [Related companion: Dynamic Texture Editing](https://github.com/richtrad/dynamic-texture-editing)

The article discusses contextual fill-in, colourisation, retouching, and user
evaluation in the reconstruction of historical photographs of Most. This
repository makes the published article easier to cite and inspect. It is an
archive of the publication, not a claim of an executable reproduction.

## Contents

```text
paper/
  Photorealistic_Texture_Contextual_Fill-In_Heritage_2025.pdf  # byte-preserved PDF
  article_text_extracted.txt                                   # convenience text extraction
figures/pdf_extracted/                                         # raster objects decoded from the PDF
metadata/
  figure-extraction-manifest.json                             # dimensions, pages, hashes
  FIGURES.md                                                   # figure/page inventory
  psd-layer-manifest.json                                     # source/output hashes for layer exports
data/layers/working_psd_exports/                               # PNG exports; source PSDs are excluded
  README.md                                                    # export method and provenance boundary
tools/extract_pdf_figures.py                                   # reproducible extraction script
CITATION.cff
citation.bib
LICENSE-ARTICLE.md
PROVENANCE.md
```

The PDF is kept byte-for-byte as the local version-of-record copy. The text
file is only a search and accessibility aid; it is not a reconstructed source
manuscript. Figure 9 is vector-drawn in the PDF, so it is documented in the
inventory but is not represented by a raster extraction. The other 26 image
files are decoded from embedded PDF raster objects without resampling or
retouching. Their source page, object name, dimensions, and SHA-256 are in the
manifest.

The repository also contains a separate layer archive under
`data/layers/working_psd_exports/`. It contains four PNG exports from the
directly verified `cp_1` working PSD. The source PSD/PSB binaries are not copied into Git;
the export manifest records their basenames, sizes, SHA-256 hashes, layer
names, bounding boxes, and the hashes of the PNG outputs. `cp_1` is the
verified Figure 7/10 case. Additional local candidates remain outside this
public commit until their article mapping and rights are checked.

## Source and data boundary

No original LaTeX source for this Heritage article was recovered. The related
`dynamic-texture-editing` repository contains a different 2015 article and its
historical material; it is linked for context and should not be treated as the
implementation of this Heritage paper.

The article’s Data Availability Statement says that raw supporting data are
available from the authors on request and are intended for a future web-based
platform and 3D module. Raw historical photographs, user-test records, and
other project data are therefore not asserted to be public in this archive.
The PNG layer archive is a derived, presentation-friendly export of local
working files, not a replacement for those raw sources. Historical photographs
and other third-party material may have additional rights; see the rights note
below and the layer archive's own README.

## Citation

```bibtex
@article{Richtr2025PhotorealisticTextureContextualFillIn,
  author  = {Richtr, Radek},
  title   = {Photorealistic Texture Contextual Fill-In},
  journal = {Heritage},
  year    = {2025},
  volume  = {8},
  number  = {1},
  pages   = {9},
  doi     = {10.3390/heritage8010009},
  url     = {https://doi.org/10.3390/heritage8010009}
}
```

## Rights

The article is published under the [Creative Commons Attribution 4.0
International licence](https://creativecommons.org/licenses/by/4.0/). See
[`LICENSE-ARTICLE.md`](LICENSE-ARTICLE.md) for the scope of that statement.
Historical photographs and other third-party material may have additional
rights or attribution requirements; repository visibility does not grant a
blanket licence over those materials.
