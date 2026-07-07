# Composition and Compactness Standard

Use this reference whenever a graphical abstract is planned, reviewed, or generated. The goal is to make the figure look like a manuscript graphical abstract rather than a slide poster or workflow board.

## Overall shape

- Prefer a single horizontal 16:9 canvas unless the user or journal requires another size.
- Keep one dominant visual story. The viewer should understand the main direction within 5 seconds.
- Use 3-5 primary modules by default. Use 6 modules only when the manuscript genuinely has a multi-step method. Avoid 7+ modules on a single slide.
- Keep the active visual area at 68-78% of the canvas. Keep quiet whitespace at 18-28% of the canvas.
- Keep the title band within 8-12% of the canvas height. Keep a bottom key-message band within 6-8% if used.
- Avoid equal-card poster layouts. A top-journal graphical abstract should have one large core visual element and smaller supporting elements.

## Large and small frame hierarchy

Use three frame scales:

1. Core frame: represents the central innovation, model, mechanism, or method. It should occupy 1.3-1.8 times the area of a normal module.
2. Support frame: represents input, preprocessing, validation, or application. Use consistent size and shape.
3. Micro frame: represents a short label, metric, callout, legend, or stage tag. Keep it visually quiet.

Recommended arrangements:

- Method pipeline: small input frame -> large method/core frame -> small output/application frame.
- Model-driven paper: data frame on the left, large model frame in the center, result/application frame on the right.
- Mechanism paper: large central mechanism frame with 3-4 smaller evidence or condition frames around it.
- Materials or mechanics paper: vertical multiscale stack with macro/micro/model/result layers; place the dominant mechanism in the largest layer.
- Before-after paper: two balanced panels with a narrow central intervention or method frame.

Avoid five or more equal-size rounded rectangles aligned as a row. That structure reads as a presentation workflow, not as an editorial graphical abstract.

## Frame shape rules

- Use rounded rectangles with a small radius for functional modules. Do not over-round every module into pill shapes.
- Use pill labels only for stage tags, process names, or short metric badges.
- Use open containers or lightly tinted background zones for grouped regions. Avoid heavy borders around every object.
- Use thin strokes for supporting frames and stronger strokes only for the core frame or verified key result.
- Avoid shadows, 3D bevels, heavy gradients, ornamental frames, and decorative icons.
- Use one shape grammar across the figure: e.g. all modules rounded rectangles, all connectors arrows, all metric badges pills.

## Compactness and spacing

- Use a regular grid. Recommended safe margins: 4-6% left/right and 5-7% top/bottom.
- Use inter-module gutters of 2-4% of canvas width. Reduce gaps before reducing font size.
- Align top edges, baselines, and connector centers. Misalignment is more damaging than moderate simplicity.
- Keep connectors short and direct. Use elbow connectors only when straight arrows would cross major objects.
- Keep the central visual enlarged enough to dominate the page. If every module has equal weight, the composition is under-designed.

## Text density

- Each module should contain one concise title plus 0-2 short labels. Avoid paragraph bullets inside modules.
- Replace bullet sentences with compact technical labels.
- Put explanatory detail in speaker notes, JSON notes, or the manuscript figure caption, not in the graphical abstract body.
- Use no more than 35-55 visible Chinese characters per module and no more than 18-28 English words per module.
- The key-message sentence should be one line if possible. Use a two-line key message only when the content is highly technical.

## Title and caption treatment

- Use a short claim-like title. Avoid long descriptive subtitles inside the figure.
- Remove style tags such as 'Chinese top journal', 'international top journal', or 'publication grade' from the visible figure.
- If a subtitle is necessary, keep it as a small caption-like line below the title, not as a second headline.
- Prefer a concise bottom key message over a large bordered conclusion box.

## Color semantics

- Assign colors by scientific meaning, not by decoration.
- Use one primary method color, one data/input color, one result/application color, and one warning or defect color.
- Reserve red or orange for risk, defects, cracks, failure, inhibition, or warning. Do not use red as a generic module border.
- Keep the background near-white or very light gray. Use dark neutral text.

## Font and typography

Recommended editable font families:

- English: Arial, Aptos, Calibri, Helvetica-compatible fallback.
- Simplified Chinese: Microsoft YaHei, DengXian, SimHei, Noto Sans CJK-compatible fallback.
- Traditional Chinese: Microsoft JhengHei or Noto Sans CJK-compatible fallback.

Hierarchy for a 16:9 PPT canvas:

- Main title: 22-28 pt, semibold or bold, one line preferred.
- Section or module title: 12-16 pt, semibold.
- Module labels: 9-11.5 pt, regular.
- Micro labels or metric tags: 8-9.5 pt, regular or semibold.
- Bilingual secondary text: 65-80% of the primary-language size.

Rules:

- Do not mix more than two font families in one figure.
- Use weight and size for hierarchy before adding colors.
- Keep Chinese labels short and avoid full-sentence module text.
- Avoid underlines, all caps, decorative italics, and excessive bold text.
- Ensure all visible text remains legible after shrinking to a single-column manuscript width.

## Review heuristics from common weak layouts

When a generated figure looks like five equal workflow cards, revise it using these steps:

1. Merge adjacent preparation stages into one input/preparation region.
2. Enlarge the core model or mechanism into a dominant central frame.
3. Merge evaluation and application into one output/decision region unless they are the paper's main contribution.
4. Replace bullet lists with short labels.
5. Remove visible style labels and redundant subtitles.
6. Convert large bordered conclusion boxes into light key-message strips.
7. Strengthen the main arrow chain and suppress secondary connectors.


## Information-density coupling

Use `references/information-density-standard.md` together with this file. Compactness controls geometry; information density controls how much scientific meaning is carried by each region. A figure is not publication-ready if it is geometrically neat but scientifically empty, or scientifically rich but unreadable after reduction.

Default coupling:

- Compact density: 3-4 modules, one dominant core, 7-12 semantic units, minimal bottom message.
- Standard density: 3-5 modules, 9-16 semantic units, one verified result cue where available.
- Rich density: 4-6 modules, 12-20 semantic units, used only for genuinely multiscale or multi-evidence stories.

When reducing clutter, remove text before removing scientifically necessary visual objects. When adding substance, add verified visual evidence before adding text.
