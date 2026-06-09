# Codex for Humans v0.1.5

This release focuses on public-release safety hardening.

## What Changed

- Hardened `scripts/package_release.py` so release zips exclude local private and sensitive-looking files.
- Added a GitHub Actions dirty packaging test that creates local private files and confirms they are not included in the release zip.
- Added a GitHub Actions PowerShell dry-run check for the Windows install script.
- Added README and SECURITY wording that repo checks are guardrails, not proof a user's own software is secure, legal, deployable, or production-ready.
- Added a Traditional Chinese micro case showing why a high readiness score does not automatically mean delivery approval.

## Why This Matters

This repo is intended for nontechnical beginners. The release process should avoid accidentally packaging local `.env`, private Codex folders, logs, archives, or private reports when a maintainer prepares a public zip.

## Upgrade Notes

If you already installed v0.1.4, you can reinstall v0.1.5 with the same install scripts.

Always run dry-run first:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -DryRun
```

```bash
bash ./scripts/install.sh --dry-run
```
