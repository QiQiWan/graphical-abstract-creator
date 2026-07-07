# Spec Format

Use this working spec shape for the preview-first workflow.

```json
{
  "content_brief": "...",
  "content_structure": {
    "study_object": "...",
    "main_flow": ["..."],
    "method_or_model": "...",
    "mechanism": "...",
    "key_result": "...",
    "application": "...",
    "source_materials": ["..."]
  },
  "compact_style_card": {
    "language_and_tone": "...",
    "visual_structure_and_complexity": "...",
    "palette_and_density": "...",
    "source_handling_and_output": "..."
  },
  "complexity_control": {
    "max_main_modules": 4,
    "main_modules": ["input/source", "method/model", "mechanism/result", "application"],
    "merged_modules": ["mechanism + result"],
    "min_visual_object_types": 3,
    "max_primary_connectors": 6,
    "max_visible_labels_per_module": 2
  },
  "master_preview_prompt": "...",
  "preview_review": {
    "visual_complexity_pass": true,
    "mechanism_completeness_pass": true,
    "frame_hierarchy_pass": true,
    "information_density_floor_pass": true,
    "academic_aesthetics_pass": true,
    "module_cap_pass": true,
    "accepted": true
  },
  "ppt_blueprint": {
    "slide_ratio": "16:9",
    "regions": ["..."],
    "object_plan": ["..."],
    "text_hierarchy": ["..."],
    "consistency_locks": ["..."]
  }
}
```
