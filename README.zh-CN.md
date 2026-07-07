[中文](README.md) | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [繁體中文](README.zh-TW.md)

# 图形摘要创建器

图形摘要创建器是 **EatRice Lab 作品**，用于创建适合论文投稿的图形摘要。Skill 采用“内容读取 → 风格确认 → 完整提示词 → 预览图生成 → 预览审查 → PowerPoint 包交付 → 一致性审查”的工作流。

## 安装到 Codex

1. 准备本目录打包得到的 `skill.zip`。
2. 打开支持 Skills 的 Codex 或 ChatGPT 环境，进入 Skills 或 Manage skills 页面。
3. 上传 `skill.zip`。
4. 启用 `graphical-abstract-creator`。
5. 在对话中提供图形摘要内容概要并要求创建图形摘要。

## 默认输出方式

默认采用 **精确显示 + 可编辑重建** 的 PowerPoint 包：

1. **第 1 页：精确显示页**  
   使用通过审查的预览图作为整页视觉锁定层，保证 PPT 打开和导出时与预览图一致。

2. **第 2 页：可编辑重建页**  
   使用 PowerPoint 文本框、形状、箭头、公式、指标表和图例重建图形摘要结构。复杂纹理、裂缝图、热力图、显微形貌等局部科学图像可以作为局部图片面板保留。

3. **可选第 3 页：编辑说明页**  
   说明哪些元素可编辑，哪些元素是局部科学图像面板，以及任何必要的简化。

这种方式解决两个目标之间的冲突：第 1 页保证显示效果与预览图一致，第 2 页保证主要结构和文字元素可编辑。

## 最低输入

请提供图形摘要大致要展示的内容。内容越详细越好，建议包含研究对象、主要流程或机制、方法或模型、关键结果、应用场景，以及参考图或论文摘要。

## 风格确认

Skill 会用四组字段快速确认：

- 语言与学术语气
- 视觉结构与复杂度
- 配色与信息密度
- 源图处理与输出方式

可以直接回复“使用默认设置”。

## 主要文件

- `SKILL.md`：Skill 总体逻辑。
- `references/exact-visual-parity-standard.md`：精确显示与可编辑重建的通用规则。
- `references/hybrid-reconstruction-standard.md`：可编辑重建页规则。
- `references/preview-to-ppt-consistency.md`：预览图到 PPT 的一致性规则。
- `docs/QUALITY_GATES.zh-CN.md`：质量门控。


## 预览一致与可编辑覆盖层

默认 PPT 包采用三层思路：第 1 页用于精确显示，保证导出外观与预览图一致；第 2 页用于编辑，通过覆盖替换的方式把标题、箭头、边框、小标题、公式、指标、图例和主要说明文字重建为 PowerPoint 可编辑对象；复杂科学示意图、裂缝、掩膜、概率图、纹理图和形貌图可以保留为高质量局部图像。
