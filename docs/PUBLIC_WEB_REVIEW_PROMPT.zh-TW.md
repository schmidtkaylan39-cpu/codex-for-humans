# 給 GPT-5.5 Pro 的公開頁面審查 Prompt

把 repo 改成 Public 後，可以把下面這段貼給 GPT-5.5 Pro。

```text
請審查這個公開 GitHub repo 是否適合給非技術新手使用：

https://github.com/schmidtkaylan39-cpu/codex-for-humans

背景：
這是一套非官方 Codex Skill 工作流程包，目標是幫助看不懂程式碼的人，用 Codex 有系統地規劃、開發、測試、交付軟體專案。

它不是單一 prompt，而是一套 repo：

1. nontechnical-codex-project-controller
   用於 0-1：需求、任務合約、開發、測試、除錯、交付、風險批准、handoff。

2. nontechnical-project-readiness-auditor
   用於 70-100：只讀稽核快完成的專案，檢查未測項目、高風險點、交付阻塞、Web GPT 送審包、非技術驗收腳本、最小收尾任務。

請你直接檢查公開 GitHub 頁面、README、docs、prompts、skills、templates、examples、install scripts、SECURITY.md、GitHub Actions。

限制：
1. 不要要求、讀取、輸出 secrets、token、API key、cookie、密碼、私鑰。
2. 不要假裝你跑過本機測試。
3. 不要假裝這個 repo 可以保證安全、合法、可上線。
4. Web GPT 只能做外部審查，不是本機證據，也不是交付批准。
5. 請以非技術新手能不能理解和安全使用為最高標準。

請輸出：

1. 總分 0-100
2. 是否適合公開給新手
3. README 清楚度評分
4. 安裝流程評分
5. 兩個 Skill 分工是否清楚
6. 一鍵安裝 script 是否會誤導或有風險
7. GIF / 圖片導覽是否有幫助
8. 中文案例與英文案例是否足夠
9. Safety First / SECURITY 是否足夠
10. Web GPT 權限邊界是否清楚
11. GitHub Actions 檢查是否合理
12. 公開後最容易被新手誤解的地方
13. 必修清單
14. 可選優化清單
15. 若要提升到 99-100 分，最小修改方案

請嚴格評分，但建議要務實。
```

