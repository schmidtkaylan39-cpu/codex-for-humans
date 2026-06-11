# Web GPT-5.5 Pro Review Prompt for v0.1.12

把下面整段貼給 Web GPT-5.5 Pro，並附上公開 GitHub 連結或 release zip 內容。

```text
請你以「外部產品審查者 + AI agent workflow 審查者 + 非技術新手使用者保護者」身份，複審 Codex for Humans v0.1.12。

公開 repo：
https://github.com/schmidtkaylan39-cpu/codex-for-humans

Release：
https://github.com/schmidtkaylan39-cpu/codex-for-humans/releases/tag/v0.1.12

上一輪你給 v0.1.11：94/100。

本次 v0.1.12 已針對你的主要建議修正：
1. 刪除 / 改寫容易讓人以為會自動切換的措辭，改成 manual cost-tier recommendation。
2. 加強聲明：不自動切換模型、供應商、帳號、付費方案或 API。
3. 加強聲明：不保證實際帳單下降，也不即時計算模型價格。
4. 在 routing template 補上：
   - Budget cap / spend limit
   - Pricing known or unknown
   - Manual model/account switch required
   - External data allowed: none / redacted / synthetic / approved
5. 說明「人工批准」是 gate，不是模型層級。
6. 說明「便宜」不等於「本機」；便宜雲端模型要當外部審查處理。
7. 加上未知狀態規則：價格、資料敏感度、環境、供應商、帳號權限或付費授權未知時，不准宣稱省錢，預設選更安全層級或人工批准。

請你重點複審：
1. 現在是否仍會讓新手誤以為能自動切模型？
2. 現在是否仍會讓新手誤以為一定會省錢？
3. 「人工批准是 gate」是否足夠清楚？
4. cheap/local/cloud 的資料風險是否講清楚？
5. routing template 是否足以支援預算上限與外部資料限制？
6. 是否和 0-1 Project Controller、70-100 Readiness Auditor、Web GPT outside review loop 打架？
7. 這版是否可從 94 提升到 98-99？

請輸出：
- 總分 0-100
- 是否建議發布 v0.1.12
- 還有沒有必修問題
- 若未達 98 分，請列出最小修改
- 若可達 98-99 分，請明確說原因

限制：
- 不要假設你能看到本機測試結果，除非我提供。
- 不要要求 Codex 直接處理 secrets。
- 不要把外部審查當成 local proof。
- 如果 GitHub 讀不到，請明確說「無法遠端驗證」，改用我提供的檔案內容審查。
```
