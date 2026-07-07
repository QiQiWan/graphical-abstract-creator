# API Spec

The stable intermediate contract is a JSON specification consumed by `scripts/build_graphical_abstract_pptx.py`.

Required fields: `title`, `language`, `journal_profile`, `palette_name`, `layout_pattern`, `abstract_content`, and `blocks`.

Strict outputs should also include `strict_mode: true`, `central_claim`, `prompt_confirmation`, `claim_source` for every block, and `output_options`.

`abstract_content` should be structured with: `main_process`, `visual_objects`, `method_or_model`, `mechanism`, `key_result`, `application`, `source_figures_to_redraw`, and `forbidden_content`.

Supported layout patterns: `left_to_right_pipeline`, `problem_method_outcome`, `center_core_radial`, `before_after_comparison`, `multiscale_stack`, `data_model_decision`, and `comparison`.

Supported object DSL types include: `dataset`, `neural_network`, `material_microstructure`, `magnetic_domain`, `rare_earth_magnet`, `crack_defect`, `sensor_array`, `monitoring_site`, `civil_structure`, `fem_mesh`, `finite_element_result`, `vision_pipeline`, `molecule_grid`, `mechanism_loop`, `optimization_loop`, `multiscale_bridge`, `process_stack`, and `performance_chart`.

Run sequence:

```bash
python scripts/check_graphical_abstract_spec.py --strict examples/ai_for_science_graphical_abstract.json
python scripts/build_graphical_abstract_pptx.py examples/ai_for_science_graphical_abstract.json examples/ai_for_science_graphical_abstract.pptx
python scripts/validate_pptx_editability.py examples/ai_for_science_graphical_abstract.pptx
python scripts/audit_graphical_abstract_quality.py examples/ai_for_science_graphical_abstract.json examples/ai_for_science_graphical_abstract.pptx examples/ai_for_science_graphical_abstract_quality_report.json
```

Palette preview:

```bash
python scripts/generate_palette_strips.py examples/palette_strips.pptx
```


## Information density object

Strict specs should include `information_density`:

```json
{
  "information_density": {
    "profile": "compact | standard | rich",
    "semantic_unit_target": "9-16",
    "visible_text_budget": {"zh_chars": "70-170", "en_words": "35-95"},
    "max_labels_per_module": 2,
    "max_connectors": 6,
    "min_visual_object_types": 4,
    "evidence_cue_required": true,
    "detail_destination": "notes_or_caption"
  }
}
```

The checker and audit scripts use this object to control whether the figure is under-dense, over-dense, or balanced for manuscript-scale reading.
