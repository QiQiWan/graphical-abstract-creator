# Journal Visual Style Guide

## Overall aesthetic

Aim for the visual language of Nature, Science, Cell, Advanced Materials, ACS, Elsevier engineering journals, and top AI/science venues: clean, precise, restrained, and explanatory. The slide should look like a publication-quality schematic, not a marketing poster.

## Canvas

- Default aspect ratio: 16:9 PowerPoint.
- Use a white or very light neutral background.
- Use a 6% to 8% margin around the canvas.
- Use a simple 12-column or 3-zone grid.
- Leave clear negative space around the central mechanism.

## Typography

- Use common editable fonts available in PowerPoint environments: Arial, Aptos, Calibri, Helvetica, or Times New Roman when a journal-like serif is requested.
- Do not bundle font files.
- Recommended sizes for 16:9:
  - Title: 26 to 34 pt.
  - Subtitle or claim: 16 to 20 pt.
  - Section labels: 13 to 16 pt.
  - Object labels: 10 to 13 pt.
  - Footnote/citation: 7 to 9 pt.
- Use sentence case for scientific labels unless field convention requires capitalization.
- Keep all text editable as PowerPoint text boxes.

## Color

Use restrained palettes. Do not use rainbow palettes unless showing ordered scalar fields and the user requests it.

Default palette:
- Background: #FFFFFF
- Text: #1F2933
- Muted text: #52616B
- Primary accent: #2A6F97
- Secondary accent: #52B788
- Warning/contrast accent: #E76F51
- Neutral shape fill: #F4F7FA
- Line: #334E68

Rules:
- Use no more than 4 semantic colors in one slide.
- Use color to encode meaning, not decoration.
- Maintain sufficient contrast for small text.
- Avoid saturated red/green as the only distinction.

## Lines and shapes

- Use consistent stroke widths: 1.0 to 1.5 pt for standard lines; 2.0 to 2.5 pt for emphasis.
- Use rounded rectangles for conceptual blocks and sharper rectangles for instruments, data arrays, or computational modules.
- Use simple arrows with consistent arrowheads.
- Put connectors behind nodes.
- Avoid heavy drop shadows, bevels, 3D extrusion, glow, and texture fills.

## Diagrams

- Use vector abstraction rather than literal photo-realistic depiction.
- Use icons only if they are drawn from native PowerPoint shapes or fully editable vector elements.
- For neural networks, use small circles, grouped layers, and arrows; avoid unnecessary layer counts.
- For materials/mechanics, represent microstructure, cracks, particles, fibers, pores, stress fields, or gradients with simple editable shapes.
- For charts, use editable PowerPoint charts or vector bars/lines.

## Common failure modes

Avoid:
- a slide that reads like an abstract paragraph;
- a figure pasted from the manuscript as a bitmap;
- decorative icons unrelated to the research mechanism;
- multiple competing focal points;
- labels too small to edit or read;
- mismatched arrow styles;
- unverified quantitative claims.


## Chinese and bilingual graphical abstracts

- Use Chinese top-journal style when the user requests Chinese output or a Chinese journal target.
- Use concise scientific Chinese, not promotional wording.
- Use common editable CJK fonts; do not bundle fonts.
- Use `chinese_science_blue` as the safest Chinese top-journal palette.
- Use `sci_cjk_bilingual` for bilingual English-Chinese outputs.
- In bilingual figures, establish one primary language and make the secondary language smaller and subordinate.
- Avoid duplicated long bilingual sentences. Use paired short terms instead.
- Keep the same vector-only and editability constraints as English outputs.
