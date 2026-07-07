#!/usr/bin/env python3
"""Audit graphical-abstract complexity metadata.

This lightweight checker reads a JSON spec and enforces the package's main hard rules:
- max_main_modules <= 4
- actual main module count <= 4
- min_visual_object_types >= 3
- max_primary_connectors <= 6
- required preview hard-gate booleans are true when present
"""
import argparse, json, sys
from pathlib import Path

REQUIRED_REVIEW_KEYS = [
    "visual_complexity_pass",
    "mechanism_completeness_pass",
    "frame_hierarchy_pass",
    "information_density_floor_pass",
    "academic_aesthetics_pass",
    "module_cap_pass",
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('spec')
    args = ap.parse_args()
    data = json.loads(Path(args.spec).read_text(encoding='utf-8'))
    issues = []
    cc = data.get('complexity_control', {})
    max_modules = cc.get('max_main_modules', 4)
    if max_modules > 4:
        issues.append('max_main_modules must be <= 4')
    modules = cc.get('main_modules', [])
    if isinstance(modules, list) and len(modules) > 4:
        issues.append(f'main module count is {len(modules)}; maximum is 4')
    min_types = cc.get('min_visual_object_types', 3)
    if min_types < 3:
        issues.append('min_visual_object_types must be >= 3')
    max_conn = cc.get('max_primary_connectors', 6)
    if max_conn > 6:
        issues.append('max_primary_connectors must be <= 6')
    review = data.get('preview_review', {})
    for key in REQUIRED_REVIEW_KEYS:
        if key in review and review.get(key) is not True:
            issues.append(f'preview review gate failed: {key}')
    if issues:
        print('FAIL')
        for item in issues:
            print('-', item)
        return 1
    print('PASS')
    return 0

if __name__ == '__main__':
    sys.exit(main())
