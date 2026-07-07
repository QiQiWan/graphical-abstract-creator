# Information Density Standard

Use this reference whenever a graphical abstract is planned, generated, or audited. The target is a dense scientific figure that remains readable after manuscript-scale reduction. A good graphical abstract should not look empty, but it should also not become a text-heavy workflow poster.

## Density objective

A publication-grade graphical abstract should answer four questions visually:

1. What is the object or system?
2. What is the method, mechanism, or intervention?
3. What is the main output or verified result?
4. Why does the result matter for the paper's application or scientific claim?

Treat information density as a balance among visual semantics, text economy, and evidence traceability. Do not increase density by adding long labels, decorative icons, repeated arrows, or unsupported claims.

## Recommended density profiles

Choose one profile before building the PPTX.

### compact

Use for single-column readability, Chinese top-journal graphical abstracts, simple method summaries, and figures that must remain clear when reduced.

- Primary modules: 3-4.
- Semantic information units: 7-12.
- Visible Chinese text budget: 45-110 characters.
- Visible English text budget: 22-60 words.
- Labels per module: 1-2.
- Connectors: 2-4.
- Visual object types: 3-6.
- Best for: input -> core method/mechanism -> output/application.

### standard

Use for most manuscript graphical abstracts.

- Primary modules: 3-5.
- Semantic information units: 9-16.
- Visible Chinese text budget: 70-170 characters.
- Visible English text budget: 35-95 words.
- Labels per module: 1-2.
- Connectors: 2-6.
- Visual object types: 4-8.
- Best for: data -> model/mechanism -> validation -> application.

### rich

Use only when the paper has a multiscale mechanism, multi-step experimental pipeline, or coupled model-experiment result that cannot be simplified further.

- Primary modules: 4-6.
- Semantic information units: 12-20.
- Visible Chinese text budget: 100-230 characters.
- Visible English text budget: 55-130 words.
- Labels per module: 1-3, with the third label allowed only for the core module.
- Connectors: 3-8.
- Visual object types: 6-10.
- Best for: multiscale, multiphysics, multimodal, or model-data-physics-decision figures.

## Semantic information units

Count the figure's information units before generation.

- Each primary module: 1 unit.
- Each essential visual object type: 0.5-1 unit depending on distinctiveness.
- Central model, mechanism, or verified result object: 1-2 units depending on dominance.
- Each short module label: 0.4-0.5 unit.
- Each necessary connector label: 0.4-0.5 unit.
- Each verified metric/result badge: 0.5-1 unit.
- Bottom key message: 1 unit.
- Repeated decorative objects: 0 units.
- Visible style labels such as "top journal" or "publication grade": 0 units and should be removed.

The target range is usually 9-16 units. Fewer than 7 units usually looks too empty. More than 20 units usually becomes unreadable at manuscript scale.

## Text-density limits

For a 16:9 graphical abstract:

- Main title: 12-26 Chinese characters or 6-12 English words.
- Subtitle: avoid by default. If used, keep below 30 Chinese characters or 15 English words.
- Module title: 4-10 Chinese characters or 2-5 English words.
- Module label: 4-12 Chinese characters or 1-6 English words.
- Key message: 18-42 Chinese characters or 10-22 English words.
- Each module: one title plus 0-2 labels by default.
- Avoid paragraph bullets inside visible modules.

When content exceeds the text budget, do not reduce font size first. Merge wording, move details to speaker notes, or convert text into visual encoding.

## Visual-density limits

- Active visual coverage should be roughly 68-78% of the canvas.
- Quiet whitespace should remain roughly 18-28% of the canvas.
- One core frame or core object should occupy 25-35% of the active visual area.
- Support frames should normally occupy 8-15% each.
- Avoid more than seven connectors unless the figure is a network mechanism.
- Avoid more than four semantic colors in the body.
- Use one large object or frame for the central claim, not many equal icons.

## Frame density

The size relationship between large and small frames controls perceived quality.

- Core frame scale: 1.3-1.8 times a support frame when a central method, mechanism, or result exists.
- Input and output frames should be visually subordinate to the core.
- Evaluation and application can share one output frame unless both are major contributions.
- Use open background zones when a hard border would make the figure feel like a poster.

## Evidence density

A top-tier graphical abstract should show enough evidence to make the scientific claim credible.

- Include at least one verified result or validation cue when the paper has results.
- Use metric placeholders only when real values are unavailable; mark them as placeholders in notes, not as final evidence.
- Do not add mechanism arrows, causal labels, or performance claims without user-provided support.
- Keep every visible scientific claim traceable to the content brief, manuscript, or confirmed user instruction.

## Revision rules

If the figure is under-dense:

1. Add one verified output, result badge, or visual object rather than more text.
2. Add a concise connector label only if it clarifies causality or transformation.
3. Strengthen the central object before adding extra side modules.

If the figure is over-dense:

1. Merge preparation steps.
2. Remove secondary labels.
3. Convert bullets into short tags.
4. Move details to notes or caption.
5. Remove repeated icons and decorative connectors.
6. Reduce the number of visible claims.
