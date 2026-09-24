# Rasterised Photoshop layers

This directory contains raster exports of the visible top-level layers from
the directly verified `cp_1` working PSD related to the Most reconstruction
workflow.
The original PSD/PSB files are deliberately excluded from the repository.
The exports are ordinary PNG files and do not require Photoshop to inspect.

The export is mechanical and reproducible with `psd-tools` 1.19.0:

- each visible layer was rasterised with `topil()`;
- the native layer crop, canvas position, dimensions, and alpha channel were
  preserved;
- no upscaling, generative enhancement, manual retouching, or colour
  correction was applied during export.

The complete source basenames, source sizes and SHA-256 hashes, layer names,
layer kinds, canvas bounds, output paths, and output hashes are in
[`../../metadata/psd-layer-manifest.json`](../../metadata/psd-layer-manifest.json).
The Czech layer names are retained exactly because they are part of the
working provenance (several are the prompts used for contextual fill-in and
colourisation).

`cp_1` is the directly verified case for the article's Figure 7/10 motif. It
contains the historical source and three successive working results. Additional
local `cp_*` candidates remain outside this public commit until their exact
article mapping and rights are checked; this repository does not claim to be a
complete raw dataset. The article's Data Availability Statement says that raw
supporting data are available from the authors on request.

The article is published under CC BY 4.0, but historical photographs and
other third-party material can have additional rights. Check the provenance
and attribution requirements before reusing an image outside this archive.
