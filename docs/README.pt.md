[中文](README.zh-CN.md) | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [繁體中文](README.zh-TW.md)

# Criador de resumo gráfico

Graphical Abstract Creator é uma obra do EatRice Lab. Cria resumos gráficos vetoriais editáveis em PowerPoint. Entrada mínima: descrever o que o resumo deve mostrar.

## Instalar no Codex

Prepare `skill.zip`, abra a gestão de Skills no Codex ou ChatGPT, carregue o arquivo e ative `graphical-abstract-creator`. Para atualizar, carregue o novo `skill.zip` e substitua a versão anterior.

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
