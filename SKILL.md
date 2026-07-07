---
name: graphical-abstract-creator
description: create publication-grade graphical abstracts through a preview-first workflow that delivers a PowerPoint package. Use for research graphical abstracts, visual abstracts, preview-image generation, style confirmation, exact visual-lock PPT delivery, editable reconstruction slides, preview-to-PPT visual parity validation, and scientific infographic quality review.
---

# Graphical Abstract Creator

## Objective

Create manuscript graphical abstracts through a preview-first workflow. The preview image is the visual design lock. When the user asks to create or export a graphical abstract, deliver a PowerPoint package that preserves the approved preview appearance and also provides editable PowerPoint elements.

## Core principle

There are two different requirements that must be handled explicitly:

1. **Visual parity**: the PowerPoint should look the same as the approved preview when opened or exported.
2. **Editability**: text, arrows, labels, frames, formulas, metrics, and major structural elements should be editable when the user needs to revise them.

Pixel-identical visual parity and full editability of every texture, crack, heatmap, material morphology, or generated illustration cannot always be satisfied on the same single slide. Use the package mode below to satisfy both requirements without misleading the user.

## Default final-output mode: visual parity plus editable overlay package

When the user asks for a final graphical abstract PPTX, create a PowerPoint package with these slides unless a different mode is explicitly requested:

1. **Slide 1: exact-view slide.**
   - Place the approved preview image full-slide as the visual-lock layer.
   - This slide is used for viewing, exporting, sharing, and publication layout checks.
   - It must match the approved preview as closely as possible.

2. **Slide 2: editable overlay slide.**
   - Start from the approved preview as a visual reference layer or localized image panels.
   - Use a cover-and-replace strategy for editable regions: cover the original title, subtitle, module titles, key formulas, metric cards, legend, major arrows, and other key labels, then redraw them as editable PowerPoint objects.
   - Keep local scientific visual panels as high-quality images when they represent texture, cracks, masks, heatmaps, microscopy, morphology, generated scientific illustrations, or other image-like content.
   - The slide should still look close to the preview, but its purpose is editing the structural and textual layer.

3. **Optional Slide 3: edit map and assumptions.**
   - Identify editable PowerPoint object groups.
   - Identify local raster scientific panels.
   - Record any simplifications, unsupported details, and preview-to-PPT consistency notes.

If the user explicitly requires one-slide delivery, choose one of these modes and state the tradeoff:
- **exact-view single slide**: visually identical, but the graphical abstract body is raster.
- **editable overlay single slide**: visually close and structurally editable, but some original preview pixels remain under editable layers.
- **pure editable redraw**: most editable, but visual similarity is lower.

## Non-negotiable constraints

- Require a content brief before starting generation.
- Use a compact style card. Do not ask a long questionnaire.
- Generate a preview image to lock composition, hierarchy, palette, arrows, labels, information density, and scientific meaning.
- Do not stop after preview generation when the user asked for a final PPTX.
- Keep the graphical abstract to no more than four main modules. If the story has more than four modules, merge or nest modules before preview generation.
- Avoid overly simple outputs. A preview that is only a row of boxes, a plain flowchart, or a text-heavy poster fails review.
- Preserve scientific accuracy. Do not invent unsupported claims, mechanisms, structures, devices, quantitative results, or causal links.
- Do not present a raster-only slide as an editable reconstruction.
- Do not claim that all scientific textures or generated image details are editable when they are not.
- In visual-parity package mode, always include both the exact-view slide and the editable overlay slide.
- Do not force image-like scientific panels into crude vector redraws when this would reduce visual fidelity.

## Entry interaction

Use `references/interaction-intake-protocol.md` and `references/intake-questionnaire.md`.

Ask in two compact steps:

1. **Content brief.** Ask the user to describe what the graphical abstract should show. Request the object of study, mechanism or workflow, method or model, key result, application endpoint, and reference figures or text.
2. **Compressed style card.** After reading the brief, ask only four grouped choices:
   - **Language and tone:** English, Simplified Chinese, Traditional Chinese, or bilingual; international-journal, Chinese top-journal, or cover-like.
   - **Structure and complexity:** auto, left-to-right, center-core, before-after, multiscale, or comparison; always limited to at most four main modules.
   - **Palette and density:** auto palette or named palette; compact, standard, or rich density.
   - **Source and output:** concept reference, vector redraw, or no source figure; exact visual-parity package, editable hybrid single slide, pure editable redraw, or preview only.

Use defaults when the user does not care: language inferred from the request, Chinese top-journal tone for Chinese output, auto structure, auto palette, standard density, vector redraw when source figures exist, and exact visual-parity package for final PPTX output.

## Default workflow

1. **Read and normalize the content.**
   - Read user-provided text and uploaded materials.
   - Convert the content into the structured format in `references/spec-format.md`.
   - Preserve supported statements and mark unknown items as unspecified.

2. **Compress the story to four modules or fewer.**
   - Use `references/complexity-and-module-control.md`.
   - Select no more than four main modules from: input/source, method/model, mechanism/process, validation/result, application/decision.
   - Merge secondary details into callouts, labels, background layers, or notes.
   - Do not allow five or more main modules in the prompt, preview, or final PPT.

3. **Prepare the visual story.**
   - Identify the central claim, scientific visual objects, result cues, and mechanism chain.
   - Select information density using `references/information-density-standard.md`.
   - Select layout using `references/layout-patterns.md`.
   - Enforce large-frame/small-frame hierarchy from `references/composition-and-compactness.md`.

4. **Confirm the compressed style card.**
   - Present the four grouped choices.
   - Let the user accept defaults or modify one grouped choice.
   - Do not expand into many independent questions unless requested.

5. **Build the master preview prompt.**
   - Use `references/prompt-construction-standard.md`.
   - Include scientific content, visual complexity, mechanism completeness, four-module cap, large/small frame hierarchy, palette, typography, density, arrow logic, label style, and exclusions.
   - The prompt must request a visually rich publication graphical abstract, not a simple block diagram.

6. **Generate and audit the preview image.**
   - Use image generation to create a graphical-abstract preview image.
   - Use `references/preview-review-standard.md` and `references/review-checklist.md`.
   - Reject previews that are too simple, too text-heavy, visually flat, mechanism-poor, academically decorative, or over the four-module limit.
   - If the preview passes hard gates and the user asked to create/export/deliver the graphical abstract, continue into PPT package construction.

7. **Create the PPT package blueprint.**
   - Use `references/exact-visual-parity-standard.md` and `references/preview-to-ppt-consistency.md`.
   - Record slide size, preview image placement, regions, module boundaries, object list, z-order, text hierarchy, connectors, colors, alignment, editable object layer, local raster panels, and consistency locks.

8. **Build the final PowerPoint package.**
   - Slide 1: exact-view slide using the approved preview image full-slide.
   - Slide 2: editable overlay slide using cover-and-replace editable PowerPoint objects for title, subtitle, module headings, arrows, frames, formulas, metrics, legends, and major labels; keep complex scientific panels as high-quality local images.
   - Slide 3 when useful: edit map, assumptions, and consistency notes.
   - Never deliver only Slide 1 when the user asked for editable output.

9. **Validate visual parity and editability.**
   - Render Slide 1 and compare it with the approved preview. The exact-view slide should visually match the preview.
   - Review Slide 2 for editability, cover-and-replace quality, structural consistency, and local-image panel quality.
   - Use `scripts/audit_visual_parity.py`, `scripts/audit_preview_ppt_consistency.py`, and `scripts/audit_preview_complexity.py` where available.
   - Correct failures before delivery.

10. **Deliver.**
   - Deliver the `.pptx` package.
   - Optionally deliver the preview image, prompt, spec, and quality report if requested.
   - State the package mode: exact visual-parity package, editable hybrid single slide, pure editable redraw, or preview only.

## Preview hard gates

A preview passes only when all of the following are true:

- **Module cap:** no more than four main modules.
- **Visual-complexity floor:** at least one dominant core object, at least three distinct scientific visual object types, visible supporting context, and more than plain rectangles with text.
- **Mechanism completeness:** the image shows source/input, method or mechanism, output/result, and implication/application when those elements are provided.
- **Large/small frame hierarchy:** one primary region is visually dominant; supporting modules are smaller and secondary.
- **Information-density floor:** the preview contains enough scientific content to be meaningful after journal-size scaling.
- **Academic aesthetics:** the layout is restrained, aligned, balanced, non-cartoonish, non-poster-like, and free of decorative clutter.

## PPT package gates

A final PPT package passes only when all of the following are true:

- Slide 1 visually matches the approved preview.
- Slide 2 contains editable PowerPoint reconstruction objects for text, arrows, frames, formulas, metrics, legends, and major structure.
- The package does not falsely claim that local raster scientific panels are editable.
- The package has no more than four main modules.
- Major labels, metrics, colors, arrows, and module hierarchy match the preview.
- Any intentional simplification or raster usage is documented.

## Quality gates

- Q0: content brief sufficiency.
- Q1: compact style card completed.
- Q2: story compressed to four modules or fewer.
- Q3: master preview prompt generated.
- Q4: preview image passes hard gates.
- Q5: exact-view slide created from approved preview.
- Q6: editable reconstruction slide completed.
- Q7: visual parity of exact-view slide verified.
- Q8: editability of reconstruction slide verified.
- Q9: typography, palette, composition, academic aesthetics, information density, and module complexity verified.
- Q10: delivery package complete.
