---
name: graphical-abstract-creator
description: create, revise, audit, and validate editable vector PowerPoint graphical abstracts for manuscript visual summaries. Use for graphical abstracts, visual abstracts, paper summary figures, editable scientific PPTX schematics, Chinese top-journal graphical abstracts, bilingual English-Chinese graphical abstracts, publication-grade style intake, prompt-confirmation planning, native PowerPoint vector icon construction, structured abstract-content intake, palette-strip preview, and publication-grade quality gates.
---

# Graphical Abstract Creator

## Objective

Produce one-slide or few-slide graphical abstracts in editable PowerPoint format for journal manuscripts and research outputs. Treat the output as a publication-grade scientific schematic, not as a decorative poster. Every text element must be editable PowerPoint text. Every visual element must be a native PowerPoint vector object whenever technically possible.

## Non-negotiable constraints

- Output `.pptx` unless the user explicitly asks for planning text only.
- Use native PowerPoint text boxes for all visible text.
- Use native PowerPoint shapes, connectors, arrows, lines, tables, and editable charts for all visual elements.
- Do not insert raster images, screenshots, embedded bitmaps, flattened SVG/PNG/PDF artwork, decorative stock icons, videos, audio, OLE objects, or external linked assets into the graphical abstract body.
- Do not bundle or share font files. Use common editable fonts available in PowerPoint environments.
- Support English, Simplified Chinese, Traditional Chinese, and bilingual English-Chinese graphical abstracts.
- Support user-facing documentation in Arabic, English, Spanish, French, Japanese, Korean, Portuguese, Simplified Chinese, and Traditional Chinese.
- Keep the design suitable for top-tier journals: evidence-driven, visually restrained, readable, aligned, semantically colored, and scientifically conservative.
- Support Chinese top-journal graphical abstracts with concise Chinese labels, strict evidence wording, and restrained editorial style.
- Prefer one coherent visual composition over dashboards, card grids, excessive badges, UI-like panels, or decorative icon collages.
- Never invent quantitative results, mechanisms, molecular structures, device configurations, model architectures, equipment details, material processes, biological pathways, or clinical effects.
- Report honestly when a requested element cannot be represented as a native PowerPoint vector object.

## Entry interaction protocol

At workflow entry, use `references/interaction-intake-protocol.md` and `references/intake-questionnaire.md`. Ask in one compact intake block; do not ask questions one by one.

### Minimum required intake

Require only these minimum inputs before drafting or generating the PPTX:

1. **Graphical abstract content brief**. The user must provide at least the approximate content to be shown. Request as much detail as possible: main process, visual objects, method/model, mechanism, key result, application scenario, and source figures to redraw. Do not generate the PPTX if this brief is absent.
2. Output language: English, Simplified Chinese, Traditional Chinese, or bilingual English-Chinese.
3. Journal profile: international top-journal, Chinese top-journal, bilingual submission, or journal-cover-like graphical abstract.
4. Source-figure policy: conceptual reference only, redraw as editable vector elements, or no source figures.
5. Output package: PPTX only, PPTX + JSON spec, PPTX + notes, PPTX + quality report, or PPTX + palette strip preview.

Ask only the minimum intake fields listed above. Infer remaining domain context from the content brief and uploaded materials.

### Layered intake and defaulting

- Use minimum mode first. Do not overwhelm the user with a long questionnaire.
- After the content brief exists, infer the central claim, layout pattern, vector object set, palette, unsupported-content exclusions, and prompt-confirmation plan.
- Present a compact confirmation card only when the user requests strict quality, Chinese top-journal style, bilingual layout, top-journal finish, or editable vector-only generation.
- When the user asks to choose colors, generate or show the palette-strip preview using `scripts/generate_palette_strips.py` and `docs/PALETTE_STRIPS.*.md`.
- If the user gives no content brief, stop and ask for it. Do not generate placeholder science.

## Default workflow

1. **Normalize the content brief.**
   - Convert user input into the structured `abstract_content` object in `references/spec-format.md`.
   - Preserve user wording for verified claims.
   - Mark missing details as `unspecified` instead of inventing them.
   - Score content sufficiency using `scripts/check_graphical_abstract_spec.py`.

2. **Extract one visual story.**
   - Identify the problem, gap, method, mechanism, key result, and implication only when supported by the brief or uploaded material.
   - Reduce the story to one central visual claim.
   - Rank source reliability: manuscript figures and methods > abstract/results > user notes > clearly marked assumptions.

3. **Run prompt confirmation when needed.**
   - Use `references/prompt-confirmation-workflow.md`.
   - Present a fixed confirmation card with claim sharpening, layout, vector redraw, result emphasis, palette, language tone, unsupported-content exclusion, and quality gates.
   - Let the user choose: accept all, edit selected items, skip confirmation, or request JSON first.

4. **Choose a structure.**
   - Use `references/layout-patterns.md`.
   - Prefer left-to-right flow for method pipelines and causal mechanisms.
   - Prefer center-core radial composition for one dominant innovation.
   - Prefer before-after for performance improvement or intervention effects.
   - Prefer multiscale stack for materials, mechanics, manufacturing, biology, geoscience, and AI-for-science topics.
   - Use comparison layout for contrastive methods, ablation, or baseline-versus-proposed visual stories.

5. **Select and preview a palette.**
   - Use `references/palette-presets.md`.
   - Default to `nature_blue` for international English output, `chinese_science_blue` for Chinese top-journal output, and `sci_cjk_bilingual` for bilingual output.
   - Use one palette consistently; do not mix palettes casually.
   - Use no more than four semantic colors on one slide.
   - If color choice matters, provide a palette strip preview. The preview must be editable vector rectangles, not a screenshot.

6. **Apply language-specific scientific style.**
   - Use `references/chinese-top-journal-style.md` for Chinese or bilingual output.
   - For Chinese top-journal outputs, use concise scientific Chinese, avoid marketing adjectives, and keep terms consistent with the manuscript.
   - For bilingual outputs, use one primary language in major labels and the other as smaller secondary labels.

7. **Build editable vector objects.**
   - Use `references/vector-icon-library.md` for the vector object DSL.
   - Represent datasets, AI models, materials, samples, fields, magnetic domains, cracks, FEM meshes, molecules, sensors, civil structures, rare-earth magnets, multiscale mechanisms, optimization loops, and performance charts with native PowerPoint shapes.
   - Redraw user-provided raster figures conceptually as editable vector shapes. Do not embed the source image.

8. **Generate the PPTX.**
   - Create a JSON spec following `references/spec-format.md`.
   - Run `scripts/check_graphical_abstract_spec.py`; use `--strict` for publication-level outputs.
   - Run `scripts/build_graphical_abstract_pptx.py` to create the editable vector PPTX.
   - Use widescreen 16:9 unless the user explicitly requests another aspect ratio.

9. **Audit quality and editability.**
   - Run `scripts/validate_pptx_editability.py`.
   - Run `scripts/audit_graphical_abstract_quality.py` for layout, language, palette, text density, claim provenance, contrast, and vector purity checks.
   - Fix every detected raster image, picture object, embedded media file, external relationship, OLE object, out-of-bounds element, unsupported claim, or density violation before delivery.

10. **Deliver with traceable assumptions.**
   - Provide the PPTX and any requested JSON spec/report.
   - State which inputs were used, which assumptions were applied, and which elements are editable vector PowerPoint objects.
   - If any request could not be fulfilled as editable vectors, identify the limitation explicitly.

## Quality gates

Use `docs/QUALITY_GATES.en.md` or `docs/QUALITY_GATES.zh-CN.md` as the publication-level gate sequence:

- Q0: content brief sufficiency;
- Q1: claim provenance;
- Q2: visual story coherence;
- Q3: editable-vector construction;
- Q4: typographic and language discipline;
- Q5: palette and contrast consistency;
- Q6: PowerPoint technical purity;
- Q7: final package completeness;
- Q8: palette-strip preview available when color style is being chosen.
