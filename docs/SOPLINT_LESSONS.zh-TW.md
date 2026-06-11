# 從 soplint 借來的 AI 紀律概念

來源：

```text
https://github.com/zaxardery8011-design/soplint
```

`soplint` 是 MIT 授權的開源工具。它不是檢查程式碼風格，而是檢查 AI agent 有沒有遵守工作紀律。

本專案採用的不是直接安裝整套工具，而是吸收三個概念。

## 1. 悔過書制度：Belief Revision

AI 最危險的地方之一，不是犯錯，而是偷偷改口。

所以當 Codex 改變以下判斷時，要留下紀錄：

- 原本以為已完成，後來發現沒完成
- 原本以為低風險，後來發現高風險
- 原本以為可以交付，後來發現缺測試
- 原本相信某個需求，後來被使用者或檔案證據推翻
- Web GPT 或 reviewer 找到漏掉的需求

建議格式：

```text
Belief Revision
- Previous belief:
- New belief:
- Trigger:
- Evidence:
- Impact on next step:
```

## 2. 分數改變也要解釋

如果 Codex 或 Auditor 把專案從 90 分改成 75 分，或從「不可交付」改成「可交付」，不能只改結論。

要說明：

```text
Readiness Revision
- Previous score or verdict:
- New score or verdict:
- Trigger:
- Evidence:
- Delivery impact:
```

這可以避免新手被分數誤導。

## 3. soplint 可以當進階外掛，但不設為必備

目前不建議把 `soplint` 變成 Codex for Humans 的必備依賴，原因：

- 它需要 PowerShell 7+ 的 `pwsh`
- 非技術新手安裝門檻會上升
- 我們的核心目標是低門檻、可直接理解
- 它比較適合已經有長跑 agent、記憶資料夾、夜間巡檢流程的人

建議定位：

```text
新手：使用 Codex for Humans 內建的 Belief Revision 規則
進階使用者：可以額外研究 soplint，把紀律檢查接到 CI 或每日巡檢
```

## 實務用法

當你覺得 Codex 前後說法不一致，可以直接貼：

```text
使用 prompts/08-belief-revision-check.md
幫我檢查你是否改變過判斷。
如果有，請寫出 Previous belief、New belief、Trigger、Evidence、Impact。
```

## 我們採用的部分

Codex for Humans 採用：

- Belief Revision Rule
- Readiness Revision Rule
- Evidence Ledger 補上 revision 欄位
- `BELIEF_REVISIONS.jsonl.example`
- `prompts/08-belief-revision-check.md`

Codex for Humans 暫不採用：

- 強制安裝 soplint
- 強制使用 PowerShell 7
- 強制每日 cron / CI 巡檢
- PreToolUse hook

這樣可以保留它最有價值的「AI 不能偷偷改口」精神，又不增加新手安裝難度。
