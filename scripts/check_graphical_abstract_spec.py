#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_CONTENT_KEYS = [
    'main_process', 'visual_objects', 'method_or_model', 'mechanism',
    'key_result', 'application', 'source_figures_to_redraw'
]

DENSITY_PROFILES = {
    'compact': {
        'min_units': 7, 'max_units': 12,
        'min_cjk': 45, 'max_cjk': 110,
        'min_en': 22, 'max_en': 60,
        'max_blocks': 4, 'max_connectors': 4,
        'max_labels': 2, 'min_visual_types': 3,
    },
    'standard': {
        'min_units': 9, 'max_units': 16,
        'min_cjk': 70, 'max_cjk': 170,
        'min_en': 35, 'max_en': 95,
        'max_blocks': 5, 'max_connectors': 6,
        'max_labels': 2, 'min_visual_types': 4,
    },
    'rich': {
        'min_units': 12, 'max_units': 20,
        'min_cjk': 100, 'max_cjk': 230,
        'min_en': 55, 'max_en': 130,
        'max_blocks': 6, 'max_connectors': 8,
        'max_labels': 3, 'min_visual_types': 6,
    },
}

EVIDENCE_TERMS = re.compile(r'(IoU|F1|AUC|RMSE|MAE|R2|R²|accuracy|precision|recall|dice|mIoU|%|提升|降低|验证|评价|精度|误差|指标|量化|对比|结果)', re.I)
CJK_RE = re.compile(r'[\u4e00-\u9fff]')
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_+\-/.]*")


def text_len(x):
    if isinstance(x, dict):
        return sum(text_len(v) for v in x.values())
    if isinstance(x, list):
        return sum(text_len(v) for v in x)
    if x is None:
        return 0
    return len(str(x).strip())


def score_content(ac):
    if isinstance(ac, str):
        n = len(ac.strip())
        score = 0
        if n >= 60:
            score += 2
        if n >= 150:
            score += 2
        if n >= 300:
            score += 2
        return min(score, 6)
    if isinstance(ac, dict):
        score = 0
        for k in REQUIRED_CONTENT_KEYS:
            if text_len(ac.get(k, '')) >= 12:
                score += 1
        if text_len(ac) >= 280:
            score += 1
        return score
    return 0


def flatten_text(value):
    out = []
    if isinstance(value, dict):
        for v in value.values():
            out.extend(flatten_text(v))
    elif isinstance(value, list):
        for v in value:
            out.extend(flatten_text(v))
    elif value is not None:
        s = str(value).strip()
        if s:
            out.append(s)
    return out


def visible_text_items(data):
    items = []
    for key in ('title', 'subtitle', 'key_message'):
        if data.get(key):
            items.append(str(data.get(key)))
    for b in data.get('blocks', []) or []:
        if not isinstance(b, dict):
            continue
        for key in ('title', 'label', 'label_secondary'):
            if b.get(key):
                items.append(str(b.get(key)))
        for key in ('labels', 'bullets'):
            vals = b.get(key, [])
            if isinstance(vals, list):
                items.extend(str(v) for v in vals if str(v).strip())
        for obj in b.get('objects', []) or []:
            if isinstance(obj, dict):
                for key in ('label', 'title'):
                    if obj.get(key):
                        items.append(str(obj.get(key)))
    for c in data.get('connectors', []) or []:
        if isinstance(c, dict) and c.get('label'):
            items.append(str(c.get('label')))
    for obj in data.get('objects', []) or []:
        if isinstance(obj, dict):
            for key in ('label', 'title'):
                if obj.get(key):
                    items.append(str(obj.get(key)))
    return items


def count_text_budget(items):
    text = ' '.join(items)
    cjk = len(CJK_RE.findall(text))
    words = len(WORD_RE.findall(text))
    return cjk, words


def object_types(data):
    types = []
    for obj in data.get('objects', []) or []:
        if isinstance(obj, dict) and obj.get('type'):
            types.append(str(obj.get('type')))
    for b in data.get('blocks', []) or []:
        if not isinstance(b, dict):
            continue
        for obj in b.get('objects', []) or []:
            if isinstance(obj, dict) and obj.get('type'):
                types.append(str(obj.get('type')))
    return sorted(set(types))


def estimate_information_units(data):
    blocks = [b for b in data.get('blocks', []) or [] if isinstance(b, dict)]
    connectors = [c for c in data.get('connectors', []) or [] if isinstance(c, dict)]
    units = float(len(blocks))
    label_count = 0
    evidence_count = 0
    for b in blocks:
        labels = b.get('labels', []) or []
        if isinstance(labels, list):
            label_count += len(labels)
            evidence_count += sum(1 for x in labels if EVIDENCE_TERMS.search(str(x)))
        if b.get('emphasis') == 'core' or b.get('role') in ('method', 'mechanism'):
            units += 1.0
        for x in flatten_text(b.get('bullets', [])):
            if EVIDENCE_TERMS.search(x):
                evidence_count += 1
    units += 0.4 * label_count
    units += 0.6 * len(object_types(data))
    units += 0.4 * sum(1 for c in connectors if c.get('label'))
    if data.get('key_message'):
        units += 1.0
    if EVIDENCE_TERMS.search(' '.join(visible_text_items(data))):
        evidence_count += 1
    return round(units, 1), evidence_count


def profile_name(data):
    info = data.get('information_density', {}) or {}
    profile = str(info.get('profile') or '').strip().lower()
    if profile in DENSITY_PROFILES:
        return profile
    jp = str(data.get('journal_profile', '')).lower()
    lang = str(data.get('language', '')).lower()
    if 'chinese' in jp or lang.startswith('zh'):
        return 'compact'
    if data.get('layout_pattern') == 'multiscale_stack' or data.get('layout') == 'multiscale_stack':
        return 'rich'
    return 'standard'


def validate_data(data, strict=False):
    issues, warnings = [], []

    ac = data.get('abstract_content')
    if not ac:
        issues.append('missing abstract_content: user must provide the approximate graphical abstract content')
    else:
        sc = score_content(ac)
        min_score = 5 if strict else 3
        if sc < min_score:
            issues.append(f'abstract_content sufficiency score {sc}/8 is below required {min_score}/8')

    title = str(data.get('title', '')).strip()
    if not title:
        warnings.append('title is empty')
    if len(CJK_RE.findall(title)) > 28 or len(WORD_RE.findall(title)) > 14 or len(title) > 90:
        warnings.append('title is long; shorten it for manuscript-scale viewing')

    blocks = data.get('blocks', [])
    if not isinstance(blocks, list) or not blocks:
        issues.append('blocks must be a non-empty list')
        blocks = []
    else:
        if len(blocks) > 5:
            warnings.append('more than five primary blocks; consider merging support stages')
        if len(blocks) >= 5 and all(not (isinstance(b, dict) and b.get('emphasis')) for b in blocks):
            warnings.append('five or more blocks without a core emphasis may look like equal workflow cards')
        for b in blocks:
            if not isinstance(b, dict):
                issues.append('each block must be an object')
                continue
            labels = b.get('labels', [])
            if isinstance(labels, list) and len(labels) > 2 and b.get('emphasis') != 'core':
                warnings.append(f"block '{b.get('id', b.get('title',''))}' has more than two labels")
            if len(CJK_RE.findall(str(b.get('title','')))) > 12 or len(WORD_RE.findall(str(b.get('title','')))) > 6:
                warnings.append(f"block title '{b.get('title','')}' may be too long")
            bullets = b.get('bullets', [])
            if isinstance(bullets, list) and bullets and strict:
                warnings.append(f"block '{b.get('id', b.get('title',''))}' uses bullets; prefer compact labels")
            if strict and not b.get('claim_source'):
                warnings.append(f"block '{b.get('id', b.get('title',''))}' lacks claim_source")

    comp = data.get('composition', {}) or {}
    if comp:
        pcs = comp.get('primary_module_count')
        if isinstance(pcs, int) and pcs > 5:
            warnings.append('composition.primary_module_count should normally be 3-5')
        scale = comp.get('core_frame_scale')
        if scale is not None:
            try:
                scale = float(scale)
                if scale < 1.2 or scale > 2.0:
                    warnings.append('core_frame_scale is outside the recommended publication range')
            except Exception:
                warnings.append('core_frame_scale should be numeric')
        if comp.get('avoid_visible_style_tags') is False:
            issues.append('final graphical abstract must avoid visible style tags')

    profile = profile_name(data)
    limits = DENSITY_PROFILES[profile]
    blocks_count = len([b for b in blocks if isinstance(b, dict)])
    connectors_count = len([c for c in data.get('connectors', []) or [] if isinstance(c, dict)])
    units, evidence_count = estimate_information_units(data)
    cjk, words = count_text_budget(visible_text_items(data))
    visual_types = object_types(data)

    if strict and not data.get('information_density'):
        warnings.append(f'information_density not declared; inferred profile={profile}')
    if blocks_count > limits['max_blocks']:
        warnings.append(f'{profile} density expects at most {limits["max_blocks"]} primary blocks')
    if connectors_count > limits['max_connectors']:
        warnings.append(f'{profile} density expects at most {limits["max_connectors"]} connectors')
    if units < limits['min_units']:
        msg = f'information density too low for {profile}: {units} semantic units < {limits["min_units"]}'
        (issues if strict else warnings).append(msg)
    if units > limits['max_units']:
        msg = f'information density too high for {profile}: {units} semantic units > {limits["max_units"]}'
        (issues if strict else warnings).append(msg)

    lang = str(data.get('language', '')).lower()
    has_cjk = cjk > 0 or lang.startswith('zh')
    if has_cjk:
        if cjk > limits['max_cjk']:
            (issues if strict else warnings).append(f'visible Chinese text exceeds {profile} budget: {cjk} chars > {limits["max_cjk"]}')
        if cjk < limits['min_cjk'] and not words > limits['min_en']:
            warnings.append(f'visible Chinese text may be too sparse for {profile}: {cjk} chars < {limits["min_cjk"]}')
    if words > 0:
        if words > limits['max_en']:
            (issues if strict else warnings).append(f'visible English text exceeds {profile} budget: {words} words > {limits["max_en"]}')
        if words < limits['min_en'] and cjk < limits['min_cjk']:
            warnings.append(f'visible English text may be too sparse for {profile}: {words} words < {limits["min_en"]}')

    info = data.get('information_density', {}) or {}
    min_visual = int(info.get('min_visual_object_types', limits['min_visual_types'])) if str(info.get('min_visual_object_types', '')).isdigit() else limits['min_visual_types']
    if strict and len(visual_types) < min_visual:
        warnings.append(f'few declared visual object types: {len(visual_types)} < {min_visual}; add vector objects or confirm builder glyphs are sufficient')
    evidence_required = info.get('evidence_cue_required', True)
    if strict and evidence_required and evidence_count == 0:
        issues.append('strict mode requires at least one verified result, validation, metric, mechanism, or application evidence cue')

    return issues, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('spec')
    ap.add_argument('--strict', action='store_true')
    ap.add_argument('--report')
    args = ap.parse_args()
    path = Path(args.spec)
    data = json.loads(path.read_text(encoding='utf-8'))
    issues, warnings = validate_data(data, args.strict)
    profile = profile_name(data)
    units, evidence_count = estimate_information_units(data)
    cjk, words = count_text_budget(visible_text_items(data))
    report = {
        'status': 'FAIL' if issues else 'PASS',
        'density_profile': profile,
        'semantic_units': units,
        'visible_cjk_chars': cjk,
        'visible_english_words': words,
        'evidence_cues': evidence_count,
        'issues': issues,
        'warnings': warnings,
    }
    if args.report:
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(report['status'])
    print(f"DENSITY: profile={profile}, units={units}, cjk={cjk}, en_words={words}, evidence_cues={evidence_count}")
    for x in issues:
        print('ISSUE:', x)
    for x in warnings:
        print('WARNING:', x)
    sys.exit(1 if issues else 0)


if __name__ == '__main__':
    main()
