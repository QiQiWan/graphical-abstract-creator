#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(cmd):
    print('$ ' + ' '.join(map(str, cmd)), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True, timeout=120)

palette = ROOT / 'examples' / 'palette_strips.pptx'
eng_spec = ROOT / 'examples' / 'ai_for_science_graphical_abstract.json'
zh_spec = ROOT / 'examples' / 'chinese_top_journal_graphical_abstract.json'
eng_out = ROOT / 'examples' / 'ai_for_science_graphical_abstract.pptx'

run([sys.executable, 'scripts/generate_palette_strips.py', str(palette)])
run([sys.executable, 'scripts/validate_pptx_editability.py', str(palette)])
run([sys.executable, 'scripts/check_graphical_abstract_spec.py', '--strict', str(eng_spec)])
run([sys.executable, 'scripts/check_graphical_abstract_spec.py', '--strict', str(zh_spec)])
run([sys.executable, 'scripts/build_graphical_abstract_pptx.py', str(eng_spec), str(eng_out)])
run([sys.executable, 'scripts/validate_pptx_editability.py', str(eng_out)])
run([sys.executable, 'scripts/audit_graphical_abstract_quality.py', str(eng_spec), str(eng_out), str(ROOT / 'examples' / 'ai_for_science_graphical_abstract_quality_report.json')])
print('Smoke tests passed')
