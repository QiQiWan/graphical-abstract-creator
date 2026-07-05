# Prompt Confirmation Workflow

## Trigger

Use this workflow before final PPTX generation when the user requests strict top-journal quality, strict publication refinement, Chinese top-journal style, bilingual output, or when the source brief is ambiguous.

## Confirmation card

Present the following card:

**Generation enhancement plan**

1. Core claim sharpening: `<one sentence>`
2. Layout strategy: `<pattern and reason>`
3. Vector redraw strategy: `<which objects will be redrawn and how>`
4. Result emphasis: `<which verified result will be visually emphasized>`
5. Language style: `<English / Chinese / bilingual tone>`
6. Palette: `<palette preset>`
7. Unsupported-content exclusion: `<what will not be added>`
8. Quality gates: `<which audit checks will be run>`

Ask the user to choose:

A. Accept all and generate.
B. Modify selected items.
C. Skip confirmation and generate a conservative draft.
D. Produce only the JSON spec first.

## Rules

- Do not introduce new scientific claims during prompt enhancement.
- Do not create fake numbers, fake materials, fake mechanisms, or fake benchmark results.
- If the content brief lacks the result, use neutral labels such as "validated improvement" only when the user explicitly states improvement exists.
- Preserve uncertainty using phrases such as "schematic representation" or "conceptual workflow" when source details are incomplete.
