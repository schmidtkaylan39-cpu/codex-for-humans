# Codex for Humans v0.1.7

This release applies the final packaging guardrail recommended after the v0.1.6 external review.

## What Changed

- `scripts/package_release.py` now skips symlinks instead of following them.
- The package script now verifies that resolved file paths stay inside the repository root.
- GitHub Actions now includes a dirty packaging test for a symlink pointing outside the repo.
- `docs/GITHUB_UPLOAD.zh-TW.md` now uses generic beginner-safe paths instead of a maintainer's local Windows path.

## Why This Matters

v0.1.6 already excluded common local private files and sensitive-looking path components.

v0.1.7 closes a remaining edge case: a normal-looking symlink inside the repo pointing to a private file outside the repo.

The release zip should contain project files only, not symlink target contents.

## Upgrade Notes

If you already installed v0.1.6, you can reinstall v0.1.7 with the same install scripts.

Always run dry-run first:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -DryRun
```

```bash
bash ./scripts/install.sh --dry-run
```
