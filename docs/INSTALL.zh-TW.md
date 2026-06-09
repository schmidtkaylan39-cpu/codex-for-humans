# 安裝方式

這份 repo 目前提供兩個 Codex Skill。安裝方式是把 `skills/` 下面的資料夾放進你的 Codex skills 資料夾。

## Windows

在 `codex-for-humans` 資料夾內執行：

```powershell
Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.codex\skills\"
```

## macOS / Linux

在 `codex-for-humans` 資料夾內執行：

```bash
cp -R ./skills/* ~/.codex/skills/
```

## 安裝後怎麼確認

重新開啟 Codex，然後在新對話輸入：

```text
使用 $nontechnical-codex-project-controller
幫我把這個專案整理成可執行任務。
```

或：

```text
使用 $nontechnical-project-readiness-auditor
幫我檢查這個專案離交付還差什麼。
```

如果 Codex 能讀到 Skill 名稱，就代表安裝成功。

## 不要複製什麼

不要把整個 `.codex` 資料夾丟到 GitHub。

不要公開：

- 聊天紀錄
- 附件
- API key
- 密碼
- token
- cookie
- 私人專案 logs
- 交易所、Discord、雲端服務憑證

