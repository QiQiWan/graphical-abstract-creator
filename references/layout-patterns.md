# Layout Patterns

Use one dominant layout pattern per graphical abstract. If the user provides no preference, infer the layout from the content brief.

## left_to_right_pipeline

Use for method workflows and causal mechanisms. Place 3-5 blocks along a horizontal path. Use one dominant arrow chain.

## problem_method_outcome

Use for most paper visual abstracts. Place the problem/input on the left, method in the center, result/application on the right.

## center_core_radial

Use when one central innovation dominates the story. Place the core method in the center and supporting elements around it. Keep radial labels short to prevent crowding.

## before_after_comparison

Use when the paper compares baseline versus proposed method, untreated versus treated, or unoptimized versus optimized. Preserve visual symmetry unless the result intentionally breaks symmetry.

## multiscale_stack

Use for materials, mechanics, biology, manufacturing, geoscience, multiscale simulations, and AI-for-science topics. Place macro/micro/model/outcome tiers vertically.

## data_model_decision

Use for AI/ML workflows: data -> model -> physics/constraints -> decision/application. Prefer 4-5 blocks and one clear arrow chain.

## comparison

Use for two-path comparisons, ablation, or baseline-versus-proposed visual stories. Keep both paths symmetric and avoid more than four comparison regions.

## Auto-layout rules

- If block coordinates are absent, the builder assigns normalized coordinates from the selected pattern.
- Keep main block count between 3 and 7.
- Use global objects sparingly; they should explain the visual story, not decorate unused space.
- Use elbow connectors only when straight connectors would cross blocks.
- Reserve the bottom callout for the central claim.


## Publication-shape refinements

Always apply `references/composition-and-compactness.md` after selecting a layout pattern.

- Prefer a large central core plus smaller support frames over equal-size card rows.
- Keep the main visual story to 3-5 primary modules when possible.
- Use open grouping zones for related stages and reduce visible borders.
- Make the model, mechanism, or core contribution 1.3-1.8 times larger than ordinary support frames.
- Use the bottom strip only for one concise key message; avoid large boxed paragraphs.
- Remove style tags from the visible canvas.


## Density-aware layout selection

Select layout together with information density:

- `compact` + method pipeline: use three-zone flow with one enlarged central model.
- `standard` + method/result story: use four-zone flow or center-core composition with one result cue.
- `rich` + multiscale story: use stacked or nested zones; avoid more than six primary modules.
- If the chosen layout requires too many labels, switch to a layout with stronger visual grouping rather than shrinking fonts.
