#!/usr/bin/env python3
import argparse, sys, zipfile, re
from pathlib import Path

BAD_PREFIXES = ('ppt/media/', 'ppt/embeddings/')
BAD_EXTS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff', '.mp4', '.mov', '.avi', '.wmv', '.mp3', '.wav')
BAD_XML = [b'<p:pic', b'<p:oleObj', b'<a:blip', b'TargetMode="External"']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pptx')
    args = ap.parse_args()
    path = Path(args.pptx)
    issues = []
    with zipfile.ZipFile(path, 'r') as z:
        names = z.namelist()
        for n in names:
            low = n.lower()
            if low.startswith('docprops/thumbnail'):
                continue
            if low.startswith(BAD_PREFIXES) or (low.endswith(BAD_EXTS) and low.startswith('ppt/')):
                issues.append(f'non-vector or embedded asset: {n}')
        for n in names:
            if n.endswith('.xml') or n.endswith('.rels'):
                try:
                    data = z.read(n)
                except Exception:
                    continue
                for token in BAD_XML:
                    if token in data:
                        issues.append(f'blocked XML token {token.decode(errors="ignore")} in {n}')
    if issues:
        print('FAIL')
        for i in issues[:50]:
            print('ISSUE:', i)
        sys.exit(1)
    print('PASS')

if __name__ == '__main__':
    main()
