# 新手前 10 分鐘

這份文件給第一次打開 `Codex for Humans` 的人。

你不用看程式碼。你只要先判斷自己是哪一種狀況。

## 第 1 分鐘：選對 Skill

如果你要做小任務、改文案、小 bug、文件微調：

```text
prompts/05-quick-daily-task.md
```

如果你要從 0 開始做，或要讓 Codex 修比較大的 bug、加功能、跑測試：

```text
$nontechnical-codex-project-controller
```

如果你的專案看起來已經 70-90 分，想知道能不能交付：

```text
$nontechnical-project-readiness-auditor
```

## 第 2-3 分鐘：貼對 Prompt

從 0 開始：

```text
prompts/01-start-new-project.md
```

中大型任務：

```text
prompts/06-full-project-task.md
```

高風險任務：

```text
prompts/07-high-risk-task.md
```

快完成要檢查：

```text
prompts/02-audit-70-to-100-project.md
```

## 第 4-6 分鐘：看 Codex 有沒有先定範圍

好的 Codex 回覆應該會先講：

- 目標
- 範圍內
- 範圍外
- 成功標準
- 測試方式
- 高風險停止點

如果 Codex 一開始就大改很多檔案，你可以要求它先補「任務合約」。

如果只是小任務，請不要要求完整任務合約。小任務只需要短分類、最小修改、簡短驗收。

## 第 7-8 分鐘：不要用分數代替證據

不要只問：

```text
現在幾分？
```

要問：

```text
哪些核心流程已經測過？
哪些還沒測？
哪些沒測會影響交付？
如果失敗，我會看到什麼現象？
```

## 第 9 分鐘：Web GPT 只做外部審查

Web GPT 可以幫你找風險和漏測。

但 Web GPT 不能證明你的本機專案真的能跑。

## 第 10 分鐘：高風險先停

如果牽涉以下事情，請先停下來要求 Codex 建立批准點：

- 真錢
- 真實交易
- 正式上線
- 真實客戶資料
- 權限或登入
- 刪除資料
- 付費 API
- API key、token、cookie、密碼

一句話：

```text
先用假資料和本機測試，證據夠了再談正式上線。
```
