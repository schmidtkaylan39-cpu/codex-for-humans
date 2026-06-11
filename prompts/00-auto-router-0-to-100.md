# 0-100 自動判斷 Prompt

請先判斷這個任務屬於哪一種：

A. Quick Mode：小任務、低風險、可快速修改和驗收
B. Full Mode：0-1 建造、中大型功能、修 bug、測試、交付
C. Readiness Audit：專案已經大致完成，需要檢查離交付還差什麼
D. High-Risk Mode：涉及金流、交易、部署、權限、真實資料、外部服務、敏感資訊
E. Model Cost Routing：需要先判斷便宜模型、標準 Codex、高階審查或人工批准

規則：

1. 如果是 A，使用 `$nontechnical-codex-project-controller` 的 Quick Mode。
2. 如果是 B，使用 `$nontechnical-codex-project-controller` 的 Full Mode。
3. 如果是 C，使用 `$nontechnical-project-readiness-auditor`。
4. 如果是 D，使用 `$nontechnical-codex-project-controller` 的 High-Risk Mode，先停下來建立高風險批准點，不可直接執行。
5. 如果是 E 或任務可能花很多 token，先做 Model Cost Routing Check。
6. 不要要求我看程式碼。
7. 所有回報用白話文。
8. 有分歧時給 A/B/C 方案。
9. 完成時只回報：結果、測試證據、檔案位置、啟用方式、未測風險、下一步。
10. 不要假裝可以自動切換模型、供應商、帳號或付費方案；需要花錢或高風險操作時先停下來。

我的任務如下：

```text
貼上你的任務
```
