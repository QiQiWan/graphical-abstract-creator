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
  "connectors": []
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
