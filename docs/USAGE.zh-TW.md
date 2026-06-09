# 使用方式

這套流程的核心是分工。

## 0-1：從想法做到可運作

使用：

```text
$nontechnical-codex-project-controller
```

適合：

- 開新專案
- 加新功能
- 修 bug
- 整理需求
- 建測試
- 做交付說明

做法：

1. 先貼 `prompts/01-start-new-project.md`
2. 讓 Codex 讀取專案
3. 讓 Codex 產出任務合約
4. 確認範圍後再執行
5. 完成後看測試結果與白話驗收腳本

## 70-100：快完成時檢查能不能交付

使用：

```text
$nontechnical-project-readiness-auditor
```

適合：

- 專案已經 70-90 分
- 不確定還缺什麼
- 不想再大改功能
- 想知道是否能交付
- 要整理 Web GPT 送審包

做法：

1. 先貼 `prompts/02-audit-70-to-100-project.md`
2. 讓 Codex 做只讀檢查
3. 看「未測項目」「高風險點」「交付阻塞」
4. 把最小收尾任務交回 0-1 Skill 執行

## 一句話規則

```text
要做事，用 Project Controller。
要判斷能不能交付，用 Readiness Auditor。
```

## 對新手最重要的心法

不要問「程式碼對不對」。

要問：

- 能不能打開？
- 核心流程能不能跑？
- 錯誤時會不會亂做？
- 有沒有測試證據？
- 還有哪些沒測？
- 這些沒測會不會影響交付？

