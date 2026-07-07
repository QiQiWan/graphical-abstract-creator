# Editable Overlay Reconstruction Standard

Use this standard for the editable slide.

## Purpose

The editable overlay slide should look close to the preview while allowing revision of the most important presentation objects. It is not required to be pixel-identical; the exact-view slide carries that role.

## Required editable objects

- title, subtitle, module titles, and subsection headings;
- badges, numbers, outer frames, main borders, and large/small frame hierarchy;
- arrows, connectors, dashed links, and decision branches;
- formulas, metrics, tables, legends, callouts, and emphasis tags;
- major labels and scientific key messages.

## Allowed high-quality image panels

Use localized images for scientific visual content whose fidelity would be damaged by crude vectorization:
- cracks, masks, heatmaps, probability maps;
- concrete textures, microscopy, material morphology, medical or biological images;
- complex generated illustration panels;
- dense network or instrument thumbnails when their internal details are not the main editable target.

## Cover-and-replace method

When an editable text or structural element already exists in the preview image:
1. cover the preview pixels under that element with a matching background shape;
2. redraw the element as a PowerPoint object;
3. check that the replacement does not visibly damage the composition.

## Prohibited

- delivering only a raster slide while calling it editable;
- vectorizing scientific image panels into low-quality decorative shapes;
- losing the visual hierarchy of the preview;
- leaving key labels, formulas, metrics, or arrows uneditable on the editable slide.
