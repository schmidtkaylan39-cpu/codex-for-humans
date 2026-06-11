# Model Cost Routing Check

Use this when you want Codex to reduce wasted premium-model time while keeping safety and proof standards.

```text
使用目前專案規則，幫我做一次 Model Cost Routing Check。

請用白話回答：
0. 本次是否允許外部模型或付費模型？預算上限是多少？如果未知，預設不允許。
1. 這個任務屬於小型、中型、大型，還是高風險？
2. 建議使用哪一層模型？這只是建議，不是自動切換。
   - 便宜 / 本機 / mini：只做草稿、摘要、低風險檢查
   - 標準 Codex：本機執行、改檔、測試、除錯、證據整理
   - 高階審查：Web GPT Pro / Claude / 其他大模型做最終外部審查
   - 人類批准：真錢、真交易、正式上線、secrets、付費工具、不可逆操作
3. 哪些部分可以交給便宜模型？資料是否需要 redaction 或 synthetic packet？
4. 哪些部分必須留給 Codex 本機執行？
5. 什麼情況要升級到高階審查？
6. 是否需要人工批准？
7. 是否需要人手動切換模型、帳號、供應商或付費方案？若需要，先停止。
8. 是否需要更新 MODEL_ROUTING_LOG.md 或 EVIDENCE_LEDGER.md？

禁止假裝可以自動切換模型、供應商、帳號或付費方案。
禁止輸出任何 secrets、API key、token、cookie、密碼、私鑰或完整帳號識別。
高風險任務不能把便宜模型當成最終判斷依據。
如果模型價格、資料敏感度、執行環境、供應商、帳號權限或付費授權未知，不准宣稱會省錢；預設選擇較安全層級或人工批准。
「便宜」不等於「本機」。如果便宜模型是外部雲端模型，只能使用 redacted、synthetic 或已批准的送審資料。
```
