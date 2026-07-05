# Interaction Intake Protocol

## Purpose

Collect the minimum information needed to produce a defensible graphical abstract, infer the remaining design choices, and present a compact confirmation card before strict generation. Avoid long questionnaire behavior.

## First message pattern

When the user starts a graphical abstract task and equivalent information is not already available, ask one compact block:

1. **Required content brief**: What should the graphical abstract show? Please describe the main process, visual objects, method/model, mechanism, key result, application scenario, and any source figures that should be redrawn as editable vectors. More detail gives a better figure.
2. Output language: English, Simplified Chinese, Traditional Chinese, or bilingual English-Chinese.
3. Journal profile: international top-journal, Chinese top-journal, bilingual submission, or cover-like graphical abstract.
4. Source-figure policy: conceptual reference only, redraw as editable vector elements, or no source figures.
5. Output package: PPTX only, PPTX + JSON spec, PPTX + notes, PPTX + quality report, or PPTX + palette strip preview.

Ask only these five fields in the first intake block. Infer remaining domain context from the content brief and uploaded materials.

## Layered intake logic

### Minimum mode

Use minimum mode by default. Require only the five fields above. If the user already supplied any of these fields, do not ask again.

### Auto-suggestion mode

After the minimum brief is present, propose defaults instead of asking more questions:

- central visual claim;
- layout pattern;
- palette;
- vector object set;
- unsupported-content exclusions;
- prompt enhancements;
- quality gates to run.

### Advanced mode

Use advanced mode only when the user asks for strict quality, high-impact journal style, Chinese top-journal style, bilingual layout, vector-only output, or scientific review before generating.

## Missing content brief gate

If the user says only "make a graphical abstract", "generate a PPT", or similar, stop and ask for the required content brief. Do not generate placeholder scientific content.

## Content brief sufficiency levels

- **Level 0**: absent. Block generation.
- **Level 1**: one vague sentence. Ask for more detail or generate only an outline.
- **Level 2**: process + objects + method. Drafting is allowed with assumptions.
- **Level 3**: process + objects + method + result + application. PPTX generation is allowed.
- **Level 4**: Level 3 plus source figures, forbidden claims, verified numbers, and preferred language tone. Use strict generation.

## Confirmation card template

After auto-suggestion, present this compact card when strict output is requested:

```text
Generation enhancement plan
1. Core claim sharpening: ...
2. Layout strategy: ...
3. Vector redraw strategy: ...
4. Result emphasis: ...
5. Language style: ...
6. Palette: ...
7. Unsupported-content exclusion: ...
8. Quality gates: Q0-Q8

Choose: A accept all / B edit selected items / C conservative draft / D JSON spec first / E show palette strips first
```

## Palette selection interaction

When the user is unsure about colors, show or generate the palette strip preview. Prefer `examples/palette_strips.pptx` or create a fresh editable PPTX by running `scripts/generate_palette_strips.py`. The palette strip must be vector rectangles with editable palette names and hex labels.
