# Codex for Humans v0.1.6

This release focuses on the final public-release packaging hardening recommended after the v0.1.5 external review.

## What Changed

- Hardened `scripts/package_release.py` so sensitive-looking path components are excluded, not only sensitive-looking filenames.
- Added exclusions for common private folders and files, including `.ssh/`, `.aws/`, `.azure/`, `.gcloud/`, `.config/`, `.npmrc`, `.pypirc`, `.netrc`, `id_rsa`, and `id_ed25519`.
- Expanded the GitHub Actions dirty packaging test with private, secrets, credentials, and SSH-style dummy files.
- Added a README reminder that readiness scores are only summaries. Blockers and evidence decide delivery.

## Why This Matters

v0.1.5 already blocked common local private files such as `.env`, `.codex/`, `.agents/`, logs, output folders, and old archives.

v0.1.6 makes the release packaging guardrail stricter by also catching paths like:

```text
secrets/data.txt
private/data.txt
credentials_folder/data.txt
.ssh/id_rsa
.npmrc
.pypirc
.netrc
```

This reduces the chance that a maintainer accidentally includes local private files in a public release zip.

## Upgrade Notes

If you already installed v0.1.5, you can reinstall v0.1.6 with the same install scripts.

Always run dry-run first:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -DryRun
```

```bash
bash ./scripts/install.sh --dry-run
```
