---
name: graphical-abstract-creator
description: "create publication-grade graphical abstracts through a preview-first workflow: read the content brief, use a compact style card, build a detailed generation prompt, create and audit a preview image, reconstruct a matching editable PowerPoint file, and enforce complexity, module-count, information-density, and preview-to-PPT consistency gates."
---

# Graphical Abstract Creator

## Objective

Create manuscript graphical abstracts through a preview-first workflow. The skill reads the scientific content, uses a compact style-confirmation card, creates a detailed preview-generation prompt, generates a graphical-abstract preview image, audits the preview against publication-grade constraints, and then rebuilds the accepted preview as an editable PowerPoint file. The final `.pptx` must remain editable and must match the approved preview in composition, hierarchy, palette, labels, arrows, information density, and scientific meaning.

## Non-negotiable constraints

- Require a content brief before starting generation.
- Use the preview image to lock the visual solution before building the PPT.
- Do not build the PPT until the preview passes the hard preview-review gates.
- Keep the final graphical abstract to **no more than four main modules**. If the story has more than four modules, merge or nest them before preview generation.
- Avoid overly simple outputs. A preview that is only a row of boxes, a plain flowchart, or a text-heavy poster fails review.
- Preserve scientific accuracy. Do not invent unsupported claims, mechanisms, structures, devices, quantitative results, or causal links.
- Deliver `.pptx` unless the user asks for planning output only.
- Use editable PowerPoint text boxes for all final visible text.
- Use native PowerPoint vector objects wherever technically possible.
- Do not use screenshots or bitmap inserts as the final graphical-abstract body.
- If a preview element cannot be faithfully rebuilt as editable PowerPoint vectors, state the limitation and simplify that element while preserving meaning.

## Entry interaction

Use `references/interaction-intake-protocol.md` and `references/intake-questionnaire.md`.

The interaction has two parts.

1. **Content brief.** Ask the user to describe what the graphical abstract should show. Request as much detail as possible: object of study, mechanism or workflow, method or model, key result, application endpoint, and reference figures or text.
2. **Compact style card.** After reading the brief, ask the user to confirm only four grouped choices:
   - **Language and academic tone:** English, Simplified Chinese, Traditional Chinese, or bilingual; international journal, Chinese top-journal, or cover-like.
   - **Visual structure and complexity:** auto, left-to-right, center-core, before-after, multiscale, or comparison; always limited to at most four main modules.
   - **Palette and density:** auto palette or a named palette; compact, standard, or rich density.
   - **Source handling and output:** concept reference, vector redraw, or no source figure; PPTX only or PPTX plus prompt/spec/report.

Do not ask a long questionnaire. Use defaults when the user does not care: language inferred from the request, international journal tone unless Chinese output is requested, auto visual structure, auto palette, standard density, vector redraw when source figures exist, and PPTX plus prompt/spec/report for strict tasks.

## Default workflow

1. **Read and normalize the content.**
   - Read the user-provided text and uploaded materials.
   - Convert the content into the structured format defined in `references/spec-format.md`.
   - Preserve supported statements and mark unknown items as unspecified.

2. **Compress the story to four modules or fewer.**
   - Use `references/complexity-and-module-control.md`.
   - Select no more than four main modules from: input/source, method/model, mechanism/process, validation/result, application/decision.
   - Merge secondary details into callouts, labels, background layers, or speaker notes.
   - Do not allow five or more main modules in the preview prompt or final PPT.

3. **Prepare the visual story.**
   - Identify the central claim, visual objects, result cues, and mechanism chain.
   - Select information density using `references/information-density-standard.md`.
   - Select a layout using `references/layout-patterns.md`.
   - Enforce the large-frame/small-frame hierarchy from `references/composition-and-compactness.md`.

4. **Confirm the compact style card.**
   - Present the four grouped choices defined above.
   - Allow the user to accept defaults or modify one grouped choice.
   - Do not expand into many independent questions unless the user asks.

5. **Build the master preview prompt.**
   - Use `references/prompt-construction-standard.md`.
   - Include scientific content, visual complexity, mechanism completeness, four-module cap, large/small frame hierarchy, palette, typography, density, arrow logic, label style, and exclusions.
   - The prompt must request a visually rich publication graphical abstract, not a simple block diagram.

6. **Generate the preview image.**
   - Use image generation to create a graphical-abstract preview image.
   - The preview must show a complete visual solution: dominant core, supporting modules, mechanism cues, labels, arrows, palette, hierarchy, and key message.

7. **Audit and refine the preview.**
   - Use `references/preview-review-standard.md` and `references/review-checklist.md`.
   - Reject previews that are too simple, too text-heavy, visually flat, mechanism-poor, academically decorative, or over the four-module limit.
   - Regenerate or revise the prompt until the preview passes the hard gates.

8. **Create the PPT reconstruction blueprint.**
   - Use `references/preview-to-ppt-consistency.md`.
   - Record slide regions, object list, z-order, text hierarchy, connectors, colors, alignment, module grouping, and consistency locks.

9. **Rebuild the editable PPT.**
   - Reconstruct the accepted preview as an editable `.pptx` using native PowerPoint text boxes, shapes, connectors, tables, and editable charts.
   - Preserve the approved preview's composition, module hierarchy, color logic, and key message.

10. **Validate preview-PPT consistency and complexity.**
   - Use `scripts/audit_preview_ppt_consistency.py` and `scripts/audit_preview_complexity.py`.
   - Verify that the PPT matches the preview and that both comply with the four-module cap, visual-complexity floor, mechanism-completeness gate, information-density floor, and academic-aesthetic gate.
   - Correct failures before delivery.

## Preview hard gates

A preview passes only when all of the following are true:

- **Module cap:** no more than four main modules.
- **Visual-complexity floor:** at least one dominant core object, at least three distinct scientific visual object types, visible supporting context, and more than plain rectangles with text.
- **Mechanism completeness:** the image shows a clear relationship among source/input, method or mechanism, output/result, and implication/application when those elements are provided.
- **Large/small frame hierarchy:** one primary region is visually dominant; supporting modules are smaller and secondary.
- **Information-density floor:** the preview contains enough scientific content to be meaningful after journal-size scaling; empty decorative space or generic icon-only compositions fail.
- **Academic aesthetics:** the layout is restrained, aligned, balanced, non-cartoonish, non-poster-like, and free of decorative clutter.

## Quality gates

- Q0: content brief sufficiency.
- Q1: compact style card completed.
- Q2: story compressed to four modules or fewer.
- Q3: master preview prompt generated.
- Q4: preview image passes hard gates.
- Q5: preview image accepted.
- Q6: editable PPT reconstruction completed.
- Q7: PowerPoint editability and vector purity verified.
- Q8: preview-PPT consistency verified.
- Q9: typography, palette, composition, and academic aesthetics verified.
- Q10: information density and module complexity verified.
