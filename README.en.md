[中文](README.md) | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [繁體中文](README.zh-TW.md)

# Graphical Abstract Creator

Graphical Abstract Creator is an **EatRice Lab** skill for manuscript graphical abstracts. It uses a preview-first workflow and delivers a PowerPoint package.

## Default output mode

The default final output is an **exact-view plus editable-reconstruction PowerPoint package**:

1. **Slide 1: exact-view slide**  
   Uses the approved preview image as a full-slide visual lock so the PPT looks the same as the preview when opened or exported.

2. **Slide 2: editable reconstruction slide**  
   Rebuilds the abstract with editable PowerPoint text boxes, shapes, arrows, formulas, metric tables, and legends. Complex local scientific panels may remain raster images when necessary.

3. **Optional Slide 3: edit map**  
   Explains editable elements, local raster panels, and simplifications.

This package separates visual fidelity and editability so the user does not lose either requirement.

## Install in Codex

Upload `skill.zip` in a Skills-enabled Codex or ChatGPT environment and enable `graphical-abstract-creator`.

## Minimum input

Provide a detailed content brief describing the graphical abstract: object of study, mechanism or workflow, method/model, key results, application endpoint, and source figures or abstract text when available.
