#!/usr/bin/env python3
"""Check graphical abstract JSON specs before PPTX generation."""
import argparse, json, re, sys
from pathlib import Path

PALETTES = {
    "nature_blue", "science_graphite", "advanced_materials_teal", "cell_biomedical",
    "engineering_amber", "ai4science_indigo", "earth_environment", "minimal_mono",
    "chinese_science_blue", "chinese_academy_red", "sci_cjk_bilingual"
}
LAYOUTS = {
    "left_to_right_pipeline", "problem_method_outcome", "center_core_radial",
    "before_after_comparison", "multiscale_stack", "data_model_decision", "comparison"
}
LANGS = {"en", "zh-CN", "zh-TW", "bilingual"}
PROFILES = {"international_top_journal", "chinese_top_journal", "bilingual_submission", "cover_like"}
BLOCK_TYPES = {"data", "dataset", "sample", "instrument", "process", "model", "mechanism", "validation", "outcome", "application"}
CONTENT_FIELDS = ["main_process", "visual_objects", "method_or_model", "mechanism", "key_result", "application", "source_figures_to_redraw", "forbidden_content"]
STRICT_MIN_SCORE = 5


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def text_len(value):
    if value is None:
        return 0
    if isinstance(value, str):
        return len(value.strip())
    if isinstance(value, list):
        return sum(text_len(x) for x in value)
    if isinstance(value, dict):
        return sum(text_len(v) for v in value.values())
    return len(str(value))


def content_score(ac):
    if not ac:
        return 0, []
    if isinstance(ac, str):
        score = 1 if len(ac.strip()) >= 20 else 0
        if len(ac.strip()) >= 100:
            score = 2
        return score, ["string_brief"]
    if not isinstance(ac, dict):
        return 0, []
    present = []
    for field in CONTENT_FIELDS:
        if text_len(ac.get(field)) > 0:
            present.append(field)
    score = 0
    for field in ["main_process", "visual_objects", "method_or_model", "key_result", "application"]:
        if field in present:
            score += 1
    if "mechanism" in present:
        score += 1
    if "source_figures_to_redraw" in present:
        score += 1
    if "forbidden_content" in present:
        score += 1
    return min(score, 8), present


def cjk_count(s):
    return len(re.findall(r"[\u4e00-\u9fff]", s or ""))


def is_strict(spec, cli_strict):
    return bool(cli_strict or spec.get("strict_mode") or spec.get("journal_profile") in {"chinese_top_journal", "international_top_journal"})


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a graphical abstract JSON spec.")
    parser.add_argument("spec_json")
    parser.add_argument("--strict", action="store_true", help="Apply publication-grade blocking thresholds.")
    args = parser.parse_args(argv)
    path = Path(args.spec_json)
    spec = load(path)
    strict = is_strict(spec, args.strict)
    issues, warnings = [], []

    ac = spec.get("abstract_content")
    score, present = content_score(ac)
    if score == 0:
        issues.append("Missing required abstract_content. Provide at least a brief description of what the graphical abstract should show.")
    elif score < 3:
        warnings.append(f"abstract_content is sparse (score={score}/8). Add process, objects, method/model, result, and application for better generation.")
    elif score < STRICT_MIN_SCORE:
        warnings.append(f"abstract_content is usable but not detailed (score={score}/8). Add mechanism, source figures, or forbidden content for strict generation.")
    if strict and score < STRICT_MIN_SCORE:
        issues.append(f"Strict mode requires abstract_content sufficiency >= {STRICT_MIN_SCORE}/8; current score={score}/8.")

    for req in ["title", "language", "journal_profile", "palette_name", "layout_pattern", "blocks"]:
        if req not in spec or spec.get(req) in (None, "", []):
            issues.append(f"Missing required field: {req}")
    if spec.get("language") not in LANGS:
        issues.append(f"Unsupported language: {spec.get('language')}")
    if spec.get("journal_profile") not in PROFILES:
        issues.append(f"Unsupported journal_profile: {spec.get('journal_profile')}")
    if spec.get("palette_name") not in PALETTES:
        issues.append(f"Unsupported palette_name: {spec.get('palette_name')}")
    if spec.get("layout_pattern") not in LAYOUTS:
        issues.append(f"Unsupported layout_pattern: {spec.get('layout_pattern')}")

    title = str(spec.get("title", ""))
    if len(title) > 95:
        warnings.append("Title is long for a graphical abstract. Prefer a compact claim-oriented title.")
    if spec.get("language") in {"zh-CN", "zh-TW", "bilingual"} and cjk_count(title) > 32:
        warnings.append("Chinese title exceeds 32 CJK characters. Prefer 18-28 characters for Chinese top-journal style.")

    if not (spec.get("central_claim") or spec.get("visual_claim")):
        warnings.append("central_claim/visual_claim is absent. The graphical abstract may lack a clear message.")

    blocks = spec.get("blocks", []) or []
    if not isinstance(blocks, list):
        issues.append("blocks must be a list")
        blocks = []
    if len(blocks) < 3:
        warnings.append("Fewer than 3 blocks may produce an under-developed graphical abstract.")
    if len(blocks) > 7:
        warnings.append("More than 7 blocks may be too dense for one graphical abstract.")
    ids = []
    for i, b in enumerate(blocks):
        if not isinstance(b, dict):
            issues.append(f"Block {i} is not an object")
            continue
        bid = b.get("id")
        if not bid:
            issues.append(f"Block {i} missing id")
        elif bid in ids:
            issues.append(f"Duplicate block id: {bid}")
        else:
            ids.append(bid)
        btype = b.get("type", "process")
        if btype not in BLOCK_TYPES:
            warnings.append(f"Block {bid or i} has uncommon type '{btype}'; it will use generic styling.")
        label = str(b.get("label", ""))
        if not label:
            warnings.append(f"Block {bid or i} missing label")
        if len(label) > 46 and spec.get("language") == "en":
            warnings.append(f"English block label is long in block {bid}: {label}")
        if spec.get("language") in {"zh-CN", "zh-TW", "bilingual"} and cjk_count(label) > 14:
            warnings.append(f"Chinese block label is long in block {bid}: {label}")
        bullets = b.get("bullets", []) or []
        if len(bullets) > 3:
            warnings.append(f"Block {bid or i} has more than 3 bullets; excess bullets may be omitted or moved to notes.")
        if text_len(bullets) > 140:
            warnings.append(f"Block {bid or i} has dense bullet text.")
        if not b.get("claim_source"):
            warnings.append(f"Block {bid or i} has no claim_source; provenance audit will be weaker.")
            if strict:
                issues.append(f"Strict mode requires claim_source for block {bid or i}.")
        for obj in b.get("objects", []) or []:
            if not isinstance(obj, dict):
                warnings.append(f"Block {bid or i} contains non-object DSL entry.")
            elif not obj.get("type"):
                warnings.append(f"Block {bid or i} object missing type.")

    block_ids = set(ids)
    for c in spec.get("connectors", []) or []:
        if c.get("from") not in block_ids:
            warnings.append(f"Connector source not found: {c.get('from')}")
        if c.get("to") not in block_ids:
            warnings.append(f"Connector target not found: {c.get('to')}")
        if c.get("style") and c.get("style") not in {"straight", "elbow"}:
            warnings.append(f"Unsupported connector style: {c.get('style')}")

    pconf = spec.get("prompt_confirmation") or {}
    if not pconf:
        warnings.append("prompt_confirmation is absent. Strict top-journal generation should record whether prompt enhancements were accepted, edited, or skipped.")
    if strict and pconf and not pconf.get("decision"):
        issues.append("Strict mode requires prompt_confirmation.decision.")

    opts = spec.get("output_options") or {}
    if opts.get("include_palette_slide") and not spec.get("palette_name"):
        issues.append("include_palette_slide requires a palette_name.")

    quality = 100 - 12 * len(issues) - 4 * len(warnings)
    quality = max(0, quality)
    print(f"Spec: {path}")
    print(f"Strict mode: {'on' if strict else 'off'}")
    print(f"Content sufficiency score: {score}/8 ({', '.join(present) if present else 'none'})")
    print(f"Estimated preflight quality: {quality}/100")
    if issues:
        print("\nBlocking issues:")
        for item in issues:
            print(f"- {item}")
    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"- {item}")
    if issues:
        print("\nFAIL")
        return 1
    print("\nPASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
