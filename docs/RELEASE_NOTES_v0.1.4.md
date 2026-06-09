# Codex for Humans v0.1.4

This release hardens the public install and release packaging flow based on GPT-5.5 Pro file-review feedback.

## What Changed

- Added dry-run support to install scripts:
  - `scripts/install.ps1 -DryRun`
  - `scripts/install.sh --dry-run`
- Updated PowerShell install behavior to remove existing Skill folders before copying, matching the bash behavior.
- Changed install fallback to prefer `~/.agents/skills` when no existing Skills folder is found, with explicit target-path guidance.
- Updated README and install docs to recommend one-click install first and manual install only for one selected Skills path.
- Added secret incident response guidance to `SECURITY.md`.
- Added `scripts/package_release.py` to create cross-platform release zips with forward-slash paths.
- Expanded GitHub Actions checks for Skill frontmatter, install scripts, and release zip packaging.

## Why

The prior release was usable, but GPT-5.5 Pro found public-preview friction:

- Windows-created release zips could include backslash path separators.
- Manual install commands could fail if the target directory did not exist.
- Repeated PowerShell installs could leave stale copied folders.
- New users needed a dry-run install path.
- `SECURITY.md` needed secret leak response steps, not just prevention.

## Safety Reminder

This is still an unofficial workflow kit. It does not guarantee software correctness, security, legality, deployment readiness, or safe use with real money, real trades, production systems, or real user data.

