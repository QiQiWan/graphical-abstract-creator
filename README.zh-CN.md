[中文](README.zh-CN.md) | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [繁體中文](README.zh-TW.md)

# 图形摘要创建器

图形摘要创建器用于生成可编辑矢量 PowerPoint 图形摘要，适用于英文论文图形摘要、中文顶级期刊图形摘要和中英双语图形摘要。输出以 `.pptx` 为核心格式，文本使用 PowerPoint 可编辑文本框，视觉元素优先使用 PowerPoint 原生矢量图元。

## 最低输入

开始生成前，需要提供图形摘要大致要展示的内容。内容越详细，图形摘要越稳定。建议包含主要流程、视觉对象、方法或模型、机制关系、关键结果、应用场景，以及需要矢量重绘的源图。

## 可选设置

- 输出语言：英文、简体中文、繁体中文、中英双语。
- 期刊风格：国际顶刊、中文顶级期刊、中英双语投稿、封面式图形摘要。
- 源图处理：仅作为概念依据、重绘为可编辑矢量图元、无源图。
- 输出内容：PPTX、JSON 规范、讲解备注、质量报告、配色彩条。
- 配色方案：可通过 `examples/palette_strips.pptx` 查看全部预设色彩组合。

## 核心流程

1. 输入图形摘要内容概要。
2. 选择语言、期刊风格、源图处理方式和输出内容。
3. 系统整理核心论断、版式方案、矢量重绘策略、配色方案和质量检查项。
4. 用户确认生成方案。
5. 生成可编辑矢量 PPTX。
6. 执行规范检查、可编辑性验证和质量审查。

## 输出标准

- 所有可见文字使用 PowerPoint 文本框。
- 图形摘要主体中的视觉元素使用 PowerPoint 原生形状、线条、箭头、连接线、表格和可编辑图表。
- 不在图形摘要主体中嵌入截图、位图、媒体文件、OLE 对象或外部链接素材。
- 中文模式使用克制、准确、证据驱动的学术表达。
- 双语模式保持主次语言层级清晰。
- 配色、字号、线宽、留白、对齐和视觉层级符合出版级图形摘要要求。

## 主要文件

- `SKILL.md`：Skill 入口说明。
- `references/`：交互、版式、配色、矢量图元、中文风格和质量规则。
- `scripts/`：PPTX 生成、规范检查、可编辑性验证、质量审查和配色彩条生成脚本。
- `examples/`：英文示例、中文顶刊示例和配色彩条示例。
- `docs/`：安装、使用、API、质量门控和配色说明。

## 其他语言文档

- [English README](README.en.md)
- [Español README](README.es.md)
- [Français README](README.fr.md)
- [日本語 README](README.ja.md)
- [한국어 README](README.ko.md)
- [Português README](README.pt.md)
- [العربية README](README.ar.md)
- [繁體中文 README](README.zh-TW.md)
