# GitHub 上傳方式

建議先建立 private repo，再改 public。

## 方案 A：用 GitHub 網頁上傳

適合完全新手。

1. 到 GitHub 建立新 repo。
2. Repo 名稱填：

```text
codex-for-humans
```

3. Visibility 先選 Private。
4. 上傳 `C:\Users\Administrator\codex-for-humans` 內的檔案。
5. 檢查沒有敏感資料。
6. 再切換成 Public。

## 方案 B：用 GitHub 指令上傳

適合電腦已經登入 GitHub CLI 的人。

```powershell
cd C:\Users\Administrator\codex-for-humans
git status
git add .
git commit -m "Initial Codex for Humans release"
gh repo create codex-for-humans --private --source . --remote origin --push
```

確認安全後，再到 GitHub 網頁改成 public。

## 不建議

不要直接把整個 `C:\Users\Administrator\.codex` 上傳。

