# API 规范

稳定的中间格式为 JSON specification，由 `scripts/build_graphical_abstract_pptx.py` 读取并生成 PPTX。

必填字段包括：`title`、`language`、`journal_profile`、`palette_name`、`layout_pattern`、`abstract_content` 和 `blocks`。

严格输出建议同时包含：`strict_mode: true`、`central_claim`、`prompt_confirmation`、每个 block 的 `claim_source` 以及 `output_options`。

`abstract_content` 建议结构化填写：`main_process`、`visual_objects`、`method_or_model`、`mechanism`、`key_result`、`application`、`source_figures_to_redraw` 和 `forbidden_content`。

支持的版式包括：`left_to_right_pipeline`、`problem_method_outcome`、`center_core_radial`、`before_after_comparison`、`multiscale_stack`、`data_model_decision` 和 `comparison`。

支持的矢量对象类型包括：`dataset`、`neural_network`、`material_microstructure`、`magnetic_domain`、`rare_earth_magnet`、`crack_defect`、`sensor_array`、`monitoring_site`、`civil_structure`、`fem_mesh`、`finite_element_result`、`vision_pipeline`、`molecule_grid`、`mechanism_loop`、`optimization_loop`、`multiscale_bridge`、`process_stack` 和 `performance_chart`。

运行流程：

```bash
python scripts/check_graphical_abstract_spec.py --strict examples/chinese_top_journal_graphical_abstract.json
python scripts/build_graphical_abstract_pptx.py examples/chinese_top_journal_graphical_abstract.json examples/chinese_top_journal_graphical_abstract.pptx
python scripts/validate_pptx_editability.py examples/chinese_top_journal_graphical_abstract.pptx
python scripts/audit_graphical_abstract_quality.py examples/chinese_top_journal_graphical_abstract.json examples/chinese_top_journal_graphical_abstract.pptx examples/chinese_top_journal_graphical_abstract_quality_report.json
```

配色预览：

```bash
python scripts/generate_palette_strips.py examples/palette_strips.pptx
```
