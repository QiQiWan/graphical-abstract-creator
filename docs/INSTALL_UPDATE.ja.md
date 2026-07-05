# グラフィカルアブストラクト作成ツール - Install and update

## Install

Upload `skill.zip` to the ChatGPT Skills interface. The package name is `graphical-abstract-creator`.

## Update

Replace the existing skill with the new `skill.zip`. Keep only one active version to avoid conflicting instructions.

## Smoke test

Run:

```bash
python tests/run_smoke_tests.py
```

The test checks example specs, builds PPTX files, validates editability, and runs the quality audit.
