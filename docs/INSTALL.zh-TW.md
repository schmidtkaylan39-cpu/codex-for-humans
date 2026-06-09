# 安裝方式

這份 repo 目前提供兩個 Codex Skill。安裝方式是把 `skills/` 下面的資料夾放進你的 Codex Skills 資料夾。

Codex Skills 的安裝路徑可能因 Codex 版本或環境不同而不同。

請優先依你目前 Codex 版本的官方文件或 `/skills` 說明確認 Skills 路徑。

常見路徑可能包含：

- `~/.agents/skills/`
- `~/.codex/skills/`

如果其中一個路徑無效，請依 Codex 顯示的 Skills 目錄為準。

## 圖片版

![Install flow](assets/install-flow.svg)

更完整的圖片式教學請看：

```text
docs/INSTALL_VISUAL.zh-TW.md
docs/INSTALL_GIF.zh-TW.md
docs/ONE_CLICK_INSTALL.zh-TW.md
```

## Windows

建議新手優先使用一鍵安裝：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

如果你要手動安裝，請只選一個 Codex 實際使用的 Skills 目錄。

範例 A：使用 `.agents\skills`

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills"
Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.agents\skills\"
```

範例 B：使用 `.codex\skills`

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.codex\skills\"
```

請選擇你電腦上存在、且 Codex 實際使用的路徑。不需要兩個都複製。

## macOS / Linux

建議新手優先使用一鍵安裝：

```bash
bash ./scripts/install.sh --dry-run
bash ./scripts/install.sh
```

如果你要手動安裝，請只選一個 Codex 實際使用的 Skills 目錄。

範例 A：使用 `.agents/skills`

```bash
mkdir -p ~/.agents/skills
cp -R ./skills/* ~/.agents/skills/
```

範例 B：使用 `.codex/skills`

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/* ~/.codex/skills/
```

請選擇你電腦上存在、且 Codex 實際使用的路徑。不需要兩個都複製。

## 安裝後驗證

重新開啟 Codex 後，請在 Codex 中確認能看到以下兩個 Skill：

- `nontechnical-codex-project-controller`
- `nontechnical-project-readiness-auditor`

可嘗試使用 `/skills` 或輸入 `$` 查看可用 Skills。

如果看不到，請檢查：

1. Skill 是否放在正確的 Codex Skills 目錄
2. 每個 Skill 資料夾內是否有 `SKILL.md`
3. 是否重新啟動 Codex
4. 是否放錯到 repo 內而不是 Codex 的 Skills 目錄

你也可以在新對話輸入：

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
