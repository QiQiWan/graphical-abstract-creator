# Graphical Abstract Creator - Install and update

Graphical Abstract Creator is an EatRice Lab work. The skill package name is `graphical-abstract-creator`.

## Install in Codex

1. Prepare `skill.zip`.
2. Open a Codex or ChatGPT environment that supports Skills, then open Skills, Manage skills, or the equivalent skill-management entry.
3. Upload or import `skill.zip`.
4. Confirm the skill name `graphical-abstract-creator` and display name `Graphical Abstract Creator`.
5. After enabling the skill, start a Codex conversation with a graphical abstract content brief.

## Update

Upload the new `skill.zip` and replace the old version. Keep only one enabled version to avoid conflicting instructions.

## Smoke test

```bash
python tests/run_smoke_tests.py
```

The test checks example specs, builds PPTX files, validates editability, and runs the quality audit.
