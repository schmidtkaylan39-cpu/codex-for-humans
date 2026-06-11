# Changelog

## 0.1.10

- Added soplint-inspired belief revision discipline without making soplint a required dependency.
- Added `prompts/08-belief-revision-check.md` for checking when Codex changed its mind.
- Added `templates/BELIEF_REVISIONS.jsonl.example`.
- Updated both core Skills with Belief Revision / Readiness Revision rules.
- Added `docs/SOPLINT_LESSONS.zh-TW.md` explaining what was adopted and why direct installation is optional.

## 0.1.9

- Replaced the first tutorial SVG visuals with Image 2 PNG visuals.
- Added correct Traditional Chinese text overlays to the instructional PNGs.
- Updated the beginner tutorial to reference the new polished image assets.

## 0.1.8

- Added a Traditional Chinese beginner tutorial for first-time Codex Skills users.
- Added four tutorial SVG images covering the overview, skill selection, install steps, and evidence loop.
- Added a README entry point for the beginner tutorial.

## 0.1.7

- Hardened release packaging to skip symlinks.
- Added a resolved-path guard so package inputs must remain inside the repository root.
- Added GitHub Actions coverage for symlink packaging exclusion.
- Replaced hard-coded local Windows paths in the GitHub upload guide with generic beginner-safe paths.

## 0.1.6

- Hardened release packaging to exclude sensitive-looking path components, not only filenames.
- Added packaging exclusions for common private folders and files such as `.ssh/`, `.aws/`, `.npmrc`, `.pypirc`, `.netrc`, `id_rsa`, and `id_ed25519`.
- Expanded dirty packaging tests with private, secrets, credentials, and SSH-style dummy files.
- Added a README reminder that readiness scores are summaries, not delivery approval.

## 0.1.5

- Hardened release packaging to exclude local private and ignored files.
- Added dirty packaging tests to GitHub Actions.
- Added PowerShell install dry-run CI check.
- Added README and SECURITY wording that repo checks are guardrails, not production safety proof.
- Added a Traditional Chinese readiness-audit micro case.

## 0.1.4

- Added dry-run support to both install scripts.
- Hardened PowerShell repeated install behavior.
- Added `scripts/package_release.py` for cross-platform release zips.
- Updated install docs to prefer one-click install and one selected Skills path.
- Added secret exposure incident response guidance to `SECURITY.md`.
- Expanded GitHub Actions checks for install scripts, Skill frontmatter, and release zip packaging.

## 0.1.3

- Added Quick / Full / High-Risk operating modes to the project controller Skill.
- Added prompt presets for daily small tasks, full tasks, and high-risk tasks.
- Updated the 0-100 router prompt to select modes more efficiently.
- Updated README and the first-10-minutes guide with "do not use the full workflow for everything" guidance.
- Added v0.1.3 release notes.

## 0.1.2

- Made Skill install paths safer for different Codex environments.
- Added stronger post-install verification instructions.
- Clarified Web GPT candidate-review authority.
- Added a README Safety First section and recommended project setup.
- Added `SECURITY.md` and a first-10-minutes beginner guide.
- Added lightweight GitHub repo checks for public-readiness guardrails.
- Added one-click install scripts for Windows and macOS/Linux.
- Added an English clinic booking system walkthrough.
- Added an animated GIF install demo and public Web GPT review prompt.

## 0.1.1

- Added a 10-second Mermaid workflow map to README.
- Added a visual install guide and install-flow SVG.
- Added a complete Traditional Chinese clinic booking system walkthrough.
- Replaced README directory tree with ASCII-safe formatting.

## 0.1.0

- Added `nontechnical-codex-project-controller`.
- Added `nontechnical-project-readiness-auditor`.
- Added beginner prompts for 0-1 work, 70-100 audits, Web GPT review, and Web-to-Codex import.
- Added templates for project rules, decision logs, evidence ledgers, risk registers, release checks, and Web review packets.
