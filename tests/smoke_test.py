#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / 'examples' / 'compact_crack_graphical_abstract.json'
OUT = ROOT / 'examples' / '_smoke_compact.pptx'
REPORT = ROOT / 'examples' / '_smoke_quality.json'
cmds = [
    [sys.executable, str(ROOT/'scripts/check_graphical_abstract_spec.py'), '--strict', str(SPEC)],
    [sys.executable, str(ROOT/'scripts/build_graphical_abstract_pptx.py'), str(SPEC), str(OUT)],
    [sys.executable, str(ROOT/'scripts/validate_pptx_editability.py'), str(OUT)],
    [sys.executable, str(ROOT/'scripts/audit_graphical_abstract_quality.py'), str(SPEC), str(OUT), str(REPORT)],
]
for cmd in cmds:
    print('RUN', ' '.join(cmd))
    subprocess.check_call(cmd)
print('PASS')
