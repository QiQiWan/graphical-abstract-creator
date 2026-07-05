[中文](README.zh-CN.md) | [English](README.en.md) | [Español](README.es.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [繁體中文](README.zh-TW.md)

# 圖形摘要建立器

圖形摘要建立器是 EatRice Lab 作品，用於產生可編輯向量 PowerPoint 圖形摘要，適用於英文論文、中文頂級期刊與中英雙語視覺摘要。主要輸出格式為 `.pptx`，可見文字使用 PowerPoint 可編輯文字框，視覺元素優先使用 PowerPoint 原生向量圖元。

## 安裝到 Codex

1. 準備本目錄打包得到的 `skill.zip`。
2. 開啟支援 Skills 的 Codex 或 ChatGPT 環境，進入 Skills、Manage skills 或相應的技能管理入口。
3. 選擇上傳或匯入 Skill，並上傳 `skill.zip`。
4. 確認 Skill 名稱為 `graphical-abstract-creator`，顯示名稱為 `Graphical Abstract Creator`。
5. 啟用後，在 Codex 對話中輸入圖形摘要內容概要，例如「使用 Graphical Abstract Creator 生成一張中文頂刊圖形摘要，內容包括……」。
6. 更新時上傳新版 `skill.zip` 並替換舊版本，建議只保留一個啟用版本。

## 最低輸入

開始生成前，需要提供圖形摘要大致要展示的內容。內容越詳細，結果越穩定。建議包含主要流程、視覺物件、方法或模型、機制關係、關鍵結果、應用場景，以及需要向量重繪的來源圖。

## 核心流程

1. 輸入圖形摘要內容概要。
2. 選擇語言、期刊風格、來源圖處理方式和輸出內容。
3. 確認核心論斷、版式方案、向量重繪策略、配色方案和品質檢查項。
4. 生成可編輯向量 PPTX。
5. 執行規範檢查、可編輯性驗證和品質審查。
