# 高風險任務 Prompt

使用 `$nontechnical-codex-project-controller`

這個任務可能涉及高風險，請使用 High-Risk Mode。

高風險包含但不限於：

- API key
- 金流
- 真實交易
- 正式部署
- 登入或權限
- 真實使用者資料
- 資料庫改動
- CMS 發布
- 寄信或 bulk message
- 付費工具
- 外部服務串接
- 刪除或不可逆操作

請先停止直接執行，先輸出：

1. 風險分類
2. 環境分類：local / test / sandbox / staging / production / unknown
3. 資料分類：fake / test / real / sensitive / unknown
4. 是否涉及真錢、真實交易、真實使用者、正式上線
5. 沙盒或 dry run 方案
6. rollback / recovery plan
7. 需要我批准的明確句子
8. 不批准時的替代方案

規則：

1. 不要讀取、輸出、要求我貼 secrets、token、cookie、密碼、私鑰。
2. 環境或資料未知時，先當成 production / sensitive。
3. 沒有明確批准，不要執行高風險動作。
4. Web GPT 只能做外部審查，不是批准。

我的高風險任務：

```text
貼上你的任務
```

