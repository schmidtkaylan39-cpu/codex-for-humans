# 一鍵安裝

這個 repo 提供兩個一鍵安裝腳本：

```text
scripts/install.ps1
scripts/install.sh
```

它們只會複製 `skills/` 裡的兩個公開 Skill：

- `nontechnical-codex-project-controller`
- `nontechnical-project-readiness-auditor`

它們不會複製 `.codex` 聊天紀錄、logs、token、cookie、API key 或私人資料。

## Windows

在 repo 資料夾中執行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

如果你知道自己的 Codex Skills 目錄，也可以指定：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -TargetPath "$env:USERPROFILE\.agents\skills"
```

## macOS / Linux

在 repo 資料夾中執行：

```bash
bash ./scripts/install.sh
```

如果你知道自己的 Codex Skills 目錄，也可以指定：

```bash
bash ./scripts/install.sh ~/.agents/skills
```

## 安裝後驗證

重新開啟 Codex 後，請確認能看到：

- `nontechnical-codex-project-controller`
- `nontechnical-project-readiness-auditor`

可嘗試使用 `/skills` 或輸入 `$` 查看可用 Skills。

如果看不到，請回到 `docs/INSTALL.zh-TW.md` 檢查路徑。

