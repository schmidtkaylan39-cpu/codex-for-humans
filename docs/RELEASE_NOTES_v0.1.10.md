# Codex for Humans v0.1.10

This release adds a lightweight AI discipline layer inspired by `soplint`.

## What Changed

- Added a Belief Revision rule to `nontechnical-codex-project-controller`.
- Added a Readiness Revision rule to `nontechnical-project-readiness-auditor`.
- Added `prompts/08-belief-revision-check.md`.
- Added `templates/BELIEF_REVISIONS.jsonl.example`.
- Added `docs/SOPLINT_LESSONS.zh-TW.md` to explain what was adopted from soplint and why direct installation remains optional.
- Updated `templates/EVIDENCE_LEDGER.md` with a revision column.

## Why This Matters

The most useful lesson from soplint is simple:

```text
When an AI changes its mind, it should not quietly change the conclusion.
It should record what changed, why, and what evidence caused the change.
```

This helps nontechnical owners catch:

- "I said it was done, but it was not"
- "I changed the score without explaining why"
- "I downgraded risk after reading evidence"
- "A reviewer found something I missed"

## Install Notes

This release does **not** require installing soplint or PowerShell 7.

Codex for Humans adopts the belief-revision discipline as prompt and Skill behavior. Advanced users can still study soplint separately:

```text
https://github.com/zaxardery8011-design/soplint
```

## Upgrade Notes

If you already installed v0.1.9, reinstall the Skills to get the updated rules.
