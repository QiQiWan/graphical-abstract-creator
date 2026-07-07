# Exact Visual-Parity Standard

Use this standard whenever the final PowerPoint must look the same as the generated preview.

## General rule

A graphical-abstract preview may contain image-like scientific content that cannot be rebuilt exactly as PowerPoint shapes. To guarantee displayed appearance while retaining practical editability, use a package-level solution:

- Slide 1: exact-view slide with the approved preview image filling the slide.
- Slide 2: editable overlay slide using the preview or local scientific panels as visual base and editable PowerPoint objects for the structural/text layer.
- Optional Slide 3: edit map and assumptions.

This is the general default method for preview-first graphical abstracts when visual parity and editability are both required.

## Slide 1: exact-view slide

- Use the approved preview image as a full-slide visual lock.
- Preserve aspect ratio and crop precisely.
- Do not add visible overlays that alter the preview appearance.
- Use this slide for export, visual review, and publication layout comparison.

## Slide 2: editable overlay slide

Use a cover-and-replace strategy:

1. Use the preview image as a base layer or use cropped local image panels from the preview.
2. Cover key text/structural regions with background-matched shapes.
3. Redraw those regions as editable PowerPoint objects.

Mandatory editable regions:
- title and subtitle;
- module numbers and module titles;
- main frames, key borders, and section headers;
- main arrows, connectors, and decision branches;
- key formulas and metric tables;
- legend, callouts, and emphasis labels.

Image-like regions may remain as high-quality raster panels:
- surface texture or field images;
- crack masks and probability maps;
- microscopy, morphology, medical, material, geoscience, or sensor panels;
- generated scientific illustration subpanels.

## Validation

- Render Slide 1 and compare it with the preview. Differences should be visually negligible.
- Inspect Slide 2 to ensure the requested editable layers are present.
- Do not claim that local raster panels are editable vectors.
- Do not pass the package if Slide 1 fails visual parity or Slide 2 lacks the mandatory editable regions.
