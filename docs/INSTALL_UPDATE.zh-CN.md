# 图形摘要创建器 - 安装与更新

图形摘要创建器是 EatRice Lab 作品，Skill 包名称为 `graphical-abstract-creator`。

## 安装到 Codex

1. 准备 `skill.zip`。
2. 打开支持 Skills 的 Codex 或 ChatGPT 环境，进入 Skills、Manage skills 或对应的技能管理入口。
3. 选择上传或导入 Skill，并上传 `skill.zip`。
4. 确认 Skill 名称为 `graphical-abstract-creator`，显示名称为 `Graphical Abstract Creator`。
5. 启用后，在 Codex 对话中输入图形摘要内容概要并开始生成。

## 更新

上传新版 `skill.zip` 并替换旧版本。建议只保留一个启用版本，避免多套说明同时生效。

## 烟雾测试

```bash
python tests/run_smoke_tests.py
```

测试会检查示例规范、生成 PPTX、验证可编辑性，并执行质量审查。
