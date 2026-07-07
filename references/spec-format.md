# JSON Specification Format

This skill uses a JSON spec as the intermediate contract before generating a PPTX.

## Required top-level fields

```json
{
  "title": "...",
  "language": "en | zh-CN | zh-TW | bilingual",
  "journal_profile": "international_top_journal | chinese_top_journal | bilingual_submission | cover_like",
  "palette_name": "nature_blue",
  "layout_pattern": "left_to_right_pipeline",
  "strict_mode": true,
  "abstract_content": {
    "main_process": "...",
    "visual_objects": ["..."],
    "method_or_model": "...",
    "mechanism": "...",
    "key_result": "...",
    "application": "...",
    "source_figures_to_redraw": ["..."],
    "forbidden_content": ["..."]
  },
  "blocks": [],
  "connectors": [],
  "information_density": {
    "profile": "standard",
    "semantic_unit_target": "9-16",
    "evidence_cue_required": true
  }
}
```

## `abstract_content`

`abstract_content` is mandatory. It may be supplied as a string for quick drafts, but strict generation should use the structured object above.

Minimum acceptable content must describe what the figure should show. Better content includes process, objects, method/model, mechanism, result, application, source figures, and forbidden unsupported content. Strict generation should target a content sufficiency score of at least 5/8.

## Blocks

Each block represents a semantic region:

```json
{
  "id": "data",
  "type": "data | sample | process | model | mechanism | validation | outcome | application",
  "label": "Data acquisition",
  "label_secondary": "数据采集",
  "bullets": ["Editable vector representation", "No embedded images"],
  "x": 0.08,
  "y": 0.35,
  "w": 0.20,
  "h": 0.32,
  "objects": [
    {"type": "dataset", "x": 0.42, "y": 0.25, "w": 0.16, "h": 0.16}
  ],
  "claim_source": "user brief / manuscript result / assumption"
}
```

Coordinates are normalized relative to the slide. If omitted, the builder assigns coordinates from `layout_pattern`.

## Vector object DSL

Objects can be placed globally or inside blocks. Supported object types include:

- `dataset`
- `neural_network`
- `material_microstructure`
- `magnetic_domain`
- `rare_earth_magnet`
- `crack_defect`
- `sensor_array`
- `monitoring_site`
- `civil_structure`
- `fem_mesh`
- `finite_element_result`
- `vision_pipeline`
- `molecule_grid`
- `mechanism_loop`
- `optimization_loop`
- `multiscale_bridge`
- `process_stack`
- `performance_chart`

## Connectors

```json
{"from": "data", "to": "model", "label": "train", "style": "straight | elbow"}
```

Use connectors for logical flow only. Avoid decorative spaghetti lines.

## Prompt confirmation

```json
{
  "prompt_confirmation": {
    "decision": "accepted_all | edited_selected | skipped | json_first",
    "accepted_items": ["claim", "layout", "palette", "vector_redraw"],
    "user_confirmed": true
  }
}
```


## Information density fields

Use the optional `information_density` object to make density constraints explicit:

```json
{
  "information_density": {
    "profile": "compact | standard | rich",
    "semantic_unit_target": "9-16",
    "visible_text_budget": {
      "zh_chars": "70-170",
      "en_words": "35-95"
    },
    "max_labels_per_module": 2,
    "max_connectors": 6,
    "min_visual_object_types": 4,
    "evidence_cue_required": true,
    "detail_destination": "notes_or_caption"
  }
}
```

Rules:

- `compact` is recommended for Chinese top-journal and single-column-friendly figures.
- `standard` is recommended for most manuscript graphical abstracts.
- `rich` is reserved for multiscale, multiphysics, multimodal, or coupled model-experiment stories.
- Visible text should stay within the selected profile budget.
- Every non-core module should normally have no more than two visible labels.
- Add verified visual objects or result cues when the figure is under-dense.
- Move method detail, assumptions, and long explanations to notes or caption when the figure is over-dense.

## Output options

```json
{
  "output_options": {
    "include_notes_slide": true,
    "include_quality_slide": true,
    "include_palette_slide": false,
    "write_quality_report": true
  }
}
```

## Palette preview

Use `examples/palette_strips.pptx` or run `scripts/generate_palette_strips.py <out.pptx>` when the user wants to compare color combinations. The palette preview is an editable vector PowerPoint file.


## Composition fields

Use the optional `composition` object to make publication layout rules explicit:

```json
{
  "composition": {
    "frame_hierarchy": "small input frame -> large central core frame -> small output frame",
    "core_frame_scale": 1.5,
    "primary_module_count": 3,
    "text_density_mode": "compact_labels",
    "bottom_message_mode": "light_strip",
    "avoid_visible_style_tags": true
  }
}
```

Rules:

- `core_frame_scale` should normally be 1.3-1.8 when there is a central model, mechanism, or result.
- `primary_module_count` should normally be 3-5.
- `text_density_mode` should be `compact_labels` for publication figures.
- `bottom_message_mode` should be `light_strip` or `caption`, not `large_box`, unless requested.
- `avoid_visible_style_tags` must be true for final graphical abstracts.
