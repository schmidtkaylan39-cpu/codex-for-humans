# Web GPT 審查迴圈

Web GPT 適合當外部審查者，不適合當本機執行證明。

## 正確分工

```text
Codex：本機讀檔、改檔、測試、除錯、交付。
Web GPT：審查需求、風險、邏輯漏洞、測試缺口。
人類：批准高風險操作與最後商業驗收。
```

## 什麼時候送 Web GPT

建議送審的情況：

- 大型專案
- 高風險專案
- 金流、交易、權限、部署、真實資料
- Codex 已經做完一輪，但你不確定是否漏風險
- 專案要從 80-90 分推到 95 分以上

## Web GPT 不能做什麼

Web GPT 不能證明：

- 本機測試真的通過
- 本機畫面真的正常
- 本機沒有漏檔
- 本機環境真的可部署
- Codex 改的檔案一定安全

所以 Web GPT 回答只能視為候選意見。

## 建議流程

1. Codex 產出送審包。
2. 人類把送審包貼給 Web GPT。
3. Web GPT 找缺口、風險、矛盾。
4. 人類把 Web GPT 結論貼回 Codex。
5. Codex 分類：
   - 接受並執行
   - 接受但排到下一輪
   - 不採用並記錄理由
   - 需要人類批准
6. Codex 用本機證據驗證結果。

## 送審 Prompt

使用：

```text
prompts/03-web-gpt-55-pro-final-review.md
```

## 回填 Prompt

使用：

```text
prompts/04-import-web-review-to-codex.md
```

