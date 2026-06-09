# 圖片式安裝教學

這份教學是給完全不懂程式的新手看的。

![Install flow](assets/install-flow.svg)

## Step 1：取得這份 repo

你可以用 GitHub 下載 zip，或用 git clone。

新手建議先下載 zip。

## Step 2：複製兩個 Skill

把這兩個資料夾：

```text
skills/nontechnical-codex-project-controller
skills/nontechnical-project-readiness-auditor
```

放進你的 Codex Skills 資料夾。

Codex Skills 的安裝路徑可能因 Codex 版本或環境不同而不同。

請優先依你目前 Codex 版本的官方文件或 `/skills` 說明確認 Skills 路徑。

常見路徑可能包含：

```text
~/.agents/skills/
~/.codex/skills/
```

Windows 常見位置可能是：

```text
C:\Users\你的使用者名稱\.codex\skills
C:\Users\你的使用者名稱\.agents\skills
```

如果其中一個路徑無效，請依 Codex 顯示的 Skills 目錄為準。

## Step 3：重新打開 Codex 並驗證

重新開啟 Codex 後，請確認能看到：

- `nontechnical-codex-project-controller`
- `nontechnical-project-readiness-auditor`

可嘗試使用 `/skills` 或輸入 `$` 查看可用 Skills。

如果看不到，通常是：

1. 放錯 Skills 目錄
2. 忘記重新啟動 Codex
3. Skill 資料夾內沒有 `SKILL.md`
4. 把 Skill 放在這個 repo 內，沒有放進 Codex 的 Skills 目錄

打開你真正要做的專案資料夾，不是打開這個 repo。

## Step 4：選對 Prompt

如果你要從 0 開始做：

```text
prompts/01-start-new-project.md
```

如果你的專案已經快完成：

```text
prompts/02-audit-70-to-100-project.md
```

## Step 5：不要做的事

不要把整個 `.codex` 資料夾上傳到 GitHub。

不要公開：

- API key
- 密碼
- token
- cookie
- 聊天紀錄
- 私人 logs
- 交易所或 Discord 憑證
