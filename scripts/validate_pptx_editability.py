#!/usr/bin/env python3
"""Validate that a PPTX contains no raster/media/OLE/external assets."""
import sys, zipfile, re
from pathlib import Path

BAD_PATTERNS = [
    (re.compile(rb"<p:pic\b"), "picture object"),
    (re.compile(rb"<pic:pic\b"), "picture object"),
    (re.compile(rb"oleObject"), "OLE object"),
    (re.compile(rb"videoFile"), "video file"),
    (re.compile(rb"audioFile"), "audio file"),
    (re.compile(rb"TargetMode=\"External\""), "external relationship"),
]
BAD_DIRS = ["ppt/media/", "ppt/embeddings/"]
BAD_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".svg", ".wmf", ".emf", ".mp4", ".mov", ".avi", ".wav", ".mp3"}


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_pptx_editability.py <file.pptx>")
        return 2
    pptx = Path(sys.argv[1])
    issues = []
    if not pptx.exists():
        print(f"Missing file: {pptx}")
        return 2
    try:
        with zipfile.ZipFile(pptx, "r") as zf:
            names = zf.namelist()
            for name in names:
                low = name.lower()
                if low == "docprops/thumbnail.jpeg":
                    continue
                if any(low.startswith(d) for d in BAD_DIRS):
                    issues.append(f"Forbidden embedded asset path: {name}")
                if Path(low).suffix in BAD_EXT:
                    issues.append(f"Forbidden embedded asset extension: {name}")
                if low.endswith(".xml") or low.endswith(".rels"):
                    data = zf.read(name)
                    for pattern, label in BAD_PATTERNS:
                        if pattern.search(data):
                            issues.append(f"Detected {label} in {name}")
    except zipfile.BadZipFile:
        print("Not a valid PPTX zip archive")
        return 2
    if issues:
        print("FAIL: non-editable or external content detected")
        for item in sorted(set(issues)):
            print(f"- {item}")
        return 1
    print("PASS: no raster/media/OLE/external assets detected")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
