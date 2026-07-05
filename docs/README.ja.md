[中文](README.zh-CN.md) | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [繁體中文](README.zh-TW.md)

# グラフィカルアブストラクト作成ツール

Graphical Abstract Creator は EatRice Lab の作品です。編集可能なベクター PowerPoint 図形要旨を作成します。最低入力: 図に表示したい内容を説明してください。

## Codex へのインストール

`skill.zip` を用意し、Codex または ChatGPT の Skills 管理画面を開いてアップロードし、`graphical-abstract-creator` を有効化します。更新時は新しい `skill.zip` をアップロードして旧版を置き換えます。

## Core workflow

1. Provide a detailed graphical abstract content brief.
2. Choose output language and journal profile.
3. Confirm or edit the suggested claim, layout, palette, vector redraw strategy, and unsupported-content exclusions.
4. Generate the PPTX.
5. Run spec check, editability validation, and quality audit.

## Strict guarantees

- Editable PowerPoint text.
- Native PowerPoint vector shapes.
- No raster images, screenshots, embedded media, OLE objects, or external linked artwork.
- Chinese top-journal and bilingual modes are supported.

Palette strip preview / 配色彩条预览: `../examples/palette_strips.pptx`.
