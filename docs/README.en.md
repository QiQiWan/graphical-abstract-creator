[中文](README.zh-CN.md) | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [繁體中文](README.zh-TW.md)

# Graphical Abstract Creator

Graphical Abstract Creator is an EatRice Lab work for producing editable vector PowerPoint graphical abstracts for English manuscripts, Chinese top-journal submissions, and bilingual English-Chinese visual summaries. The primary output is `.pptx`. Visible text is editable PowerPoint text, and visual elements are built with native PowerPoint vector shapes whenever technically possible.

## Install in Codex

1. Prepare the packaged `skill.zip`.
2. Open a Codex or ChatGPT environment that supports Skills, then open Skills, Manage skills, or the equivalent skill-management entry.
3. Upload or import `skill.zip`.
4. Confirm the skill name `graphical-abstract-creator` and display name `Graphical Abstract Creator`.
5. After enabling the skill, start a Codex conversation with a detailed graphical abstract content brief, for example: “Use Graphical Abstract Creator to create an English graphical abstract showing ...”.
6. To update, upload the new `skill.zip` and replace the old version. Keep only one enabled version to avoid conflicting instructions.

## Minimum input

Before generation, provide a content brief describing what the graphical abstract should show. More detail produces a more reliable result. Include the main process, visual objects, method or model, mechanism, key result, application scenario, and source figures to redraw when available.

## Optional settings

- Output language: English, Simplified Chinese, Traditional Chinese, or bilingual English-Chinese.
- Journal profile: international top-journal, Chinese top-journal, bilingual submission, or cover-like graphical abstract.
- Source-figure policy: conceptual reference, editable vector redraw, or no source figures.
- Output package: PPTX, JSON spec, notes, quality report, and palette-strip preview.
- Palette selection: use `../examples/palette_strips.pptx` to inspect all preset color combinations.

## Core workflow

1. Provide the graphical abstract content brief.
2. Choose language, journal profile, source-figure policy, and output package.
3. Review the generated claim, layout, vector redraw strategy, palette, and quality gates.
4. Confirm the generation plan.
5. Generate the editable vector PPTX.
6. Run specification checks, editability validation, and quality audit.

## Information density control

The creator uses publication-level information-density profiles: `compact`, `standard`, or `rich`. It checks semantic information units, visible text volume, module count, connector count, visual object count, and evidence cues. Chinese top-journal and single-column-friendly outputs should normally use `compact`; general international graphical abstracts should use `standard`; multiscale, multiphysics, or multimodal mechanism figures may use `rich`.

## Output standards

- All visible text is editable PowerPoint text.
- Visual elements in the graphical abstract body use native PowerPoint shapes, lines, arrows, connectors, tables, and editable charts.
- No screenshots, raster images, embedded media, OLE objects, or externally linked artwork are used in the graphical abstract body.
- Chinese outputs use restrained, accurate, evidence-driven academic wording.
- Bilingual outputs keep a clear hierarchy between primary and secondary languages.
- Palette, typography, line weight, spacing, alignment, and visual hierarchy follow publication-grade graphical abstract standards.

## Main files

- `../SKILL.md`: skill entrypoint.
- `../references/`: interaction, layout, palette, vector-object, Chinese-style, and quality rules.
- `../scripts/`: PPTX generation, spec checking, editability validation, quality audit, and palette-strip generation.
- `../examples/`: English example, Chinese top-journal example, and palette-strip preview.
- `./`: installation, usage, API, quality gates, and palette documentation.
