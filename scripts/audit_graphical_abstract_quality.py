#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from check_graphical_abstract_spec import (  # noqa: E402
    validate_data, profile_name, estimate_information_units,
    count_text_budget, visible_text_items, object_types, DENSITY_PROFILES,
)


def audit_spec(data):
    issues, warnings = validate_data(data, strict=True)
    blocks = data.get('blocks', []) or []
    comp = data.get('composition', {}) or {}
    profile = profile_name(data)
    limits = DENSITY_PROFILES[profile]

    valid_blocks = [b for b in blocks if isinstance(b, dict)]
    if len(valid_blocks) >= 5 and not any(b.get('emphasis') == 'core' for b in valid_blocks):
        issues.append('equal-card risk: no dominant core block identified')
    if str(comp.get('bottom_message_mode', '')).lower() == 'large_box':
        warnings.append('large boxed bottom message is discouraged')
    if comp.get('avoid_visible_style_tags') is False:
        issues.append('visible style tags are not allowed in final figure')
    if len(valid_blocks) > limits['max_blocks']:
        warnings.append(f'{profile} profile has too many primary modules')

    for b in valid_blocks:
        labels = b.get('labels', []) or []
        if isinstance(labels, list) and len(labels) > limits['max_labels'] and b.get('emphasis') != 'core':
            warnings.append(f"block {b.get('id', b.get('title',''))} has too many labels for {profile} profile")

    units, evidence_count = estimate_information_units(data)
    cjk, words = count_text_budget(visible_text_items(data))
    visual_types = object_types(data)
    density = {
        'profile': profile,
        'semantic_units': units,
        'visible_cjk_chars': cjk,
        'visible_english_words': words,
        'visual_object_types': visual_types,
        'evidence_cues': evidence_count,
    }
    return issues, warnings, density


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('spec')
    ap.add_argument('pptx', nargs='?')
    ap.add_argument('report', nargs='?')
    args = ap.parse_args()
    data = json.loads(Path(args.spec).read_text(encoding='utf-8'))
    issues, warnings, density = audit_spec(data)
    if args.pptx:
        validator = Path(__file__).with_name('validate_pptx_editability.py')
        proc = subprocess.run([sys.executable, str(validator), args.pptx], capture_output=True, text=True)
        if proc.returncode != 0:
            issues.append('PPTX editability validation failed')
            warnings.append(proc.stdout + proc.stderr)
    score = max(0, 100 - 18 * len(issues) - 4 * len(warnings))
    report = {'score': score, 'density': density, 'issues': issues, 'warnings': warnings}
    if args.report:
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(1 if issues else 0)


if __name__ == '__main__':
    main()
