# 质量门控

Q0 内容概要充分性：如果缺少图形摘要内容概要，禁止生成 PPTX。严格生成模式要求内容充分性评分不低于 5/8。

Q1 论断可追溯：所有可见论断必须来自用户输入、上传材料，或明确标记为假设。严格模式要求每个模块都有 `claim_source`。

Q2 视觉叙事一致性：一张图只围绕一个核心论断展开，避免仪表盘式堆砌，不添加未经验证的机制修饰。

Q3 可编辑矢量构造：所有文字必须为文本框，所有视觉元素应尽量为 PowerPoint 原生图元。

Q4 字体与语言规范：标签简洁，避免段落化；中英双语层级受控；中文顶刊模式下遵守克制、可证据支撑的表述。

Q5 配色与对比度：只使用一套批准配色，语义颜色克制，文字对比度可读，不随意混用不同配色方案。

Q6 PowerPoint 技术纯净性：不得包含媒体文件夹、图片对象、OLE、音视频或外部链接资源。

Q7 输出包完整性：按用户要求交付 PPTX、JSON spec、备注页和质量报告。

Q8 配色预览：当用户需要选择风格时，提供或生成可编辑矢量彩条预览。


## Q9 Composition compactness

Publication composition check:

- Use one dominant core frame when the story has a central method, model, mechanism, or result.
- Keep support frames smaller and visually subordinate.
- Avoid five or more equal workflow cards unless the paper is explicitly a workflow paper.
- Keep module text short enough for manuscript-scale viewing.
- Keep title band and bottom key-message band compact.
- Reserve red or orange for defects, risks, warnings, or explicit scientific meaning.


## Q10 信息密度

严格生成时必须声明或推断信息密度档位：`compact`、`standard` 或 `rich`。审查内容包括语义信息单元、可见文字预算、连接线数量、标签数量、视觉对象数量和证据提示。

- Compact：7-12 个语义信息单元；45-110 个中文字符或 22-60 个英文词。
- Standard：9-16 个语义信息单元；70-170 个中文字符或 35-95 个英文词。
- Rich：12-20 个语义信息单元；100-230 个中文字符或 55-130 个英文词。

如果图形摘要视觉上精致但科学信息不足，或科学信息过载导致缩小后不可读，均不能通过出版级审查。
