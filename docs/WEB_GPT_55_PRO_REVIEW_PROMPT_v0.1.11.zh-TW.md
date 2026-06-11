# Web GPT-5.5 Pro Review Prompt for v0.1.11

把下面整段貼給 Web GPT-5.5 Pro，並附上公開 GitHub 連結或 release zip 內容。

```text
請你以「外部產品審查者 + AI agent workflow 審查者 + 非技術新手使用者保護者」身份，審查 Codex for Humans v0.1.11。

公開 repo：
https://github.com/schmidtkaylan39-cpu/codex-for-humans

Release：
https://github.com/schmidtkaylan39-cpu/codex-for-humans/releases/tag/v0.1.11

本次 v0.1.11 重點：
1. 加入 Model Cost Routing，不讓新手每件事都用最貴模型。
2. 明確分成：
   - 便宜 / 本機 / mini：草稿、摘要、低風險檢查
   - 標準 Codex：本機執行、改檔、測試、證據
   - 高階審查：Web GPT Pro / Claude / 其他大模型做外部審查
   - 人工批准：真錢、真交易、正式上線、secrets、付費工具、不可逆操作
3. 明確聲明：本 repo 不會自動切換供應商、不會自動買 token、不會自動用付費帳號。
4. 外部模型只能當 candidate review，不能取代 Codex 本機證據。

請你重點審查：
1. 這套「模型成本分流」是否誠實？有沒有讓新手誤以為它會自動省錢或自動切模型？
2. 便宜 / Codex / 高階審查 / 人工批准四層是否清楚？
3. 高風險任務是否有被保護住？是否仍可能被便宜模型誤導？
4. 是否和原本 0-1 Project Controller、70-100 Readiness Auditor、Web GPT outside review loop 打架？
5. 是否增加太多流程，讓小任務變慢？
6. 是否還需要補「預算上限」「升級條件」「模型選擇紀錄」或「人類批准格式」？
7. README、Skill、prompt、template、release notes 對新手是否看得懂？
8. 有沒有任何資安、法規、金融、交易、付費工具、secrets 的風險描述不足？

請輸出：
- 總分 0-100
- 是否建議發布 v0.1.11
- 最多 10 個必修問題
- 最多 10 個可選優化
- 最重要的 5 條修改建議
- 你認為它離 98-99 分還差什麼

限制：
- 不要假設你能看到本機測試結果，除非我提供。
- 不要要求 Codex 直接處理 secrets。
- 不要把外部審查當成 local proof。
- 如果 GitHub 讀不到，請明確說「無法遠端驗證」，改用我提供的檔案內容審查。
```
