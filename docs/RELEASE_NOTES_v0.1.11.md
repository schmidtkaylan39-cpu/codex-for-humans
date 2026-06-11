# Codex for Humans v0.1.11

This release adds model cost routing.

## What Changed

- Added a Model Cost Routing rule to `nontechnical-codex-project-controller`.
- Added a Review Cost Routing rule to `nontechnical-project-readiness-auditor`.
- Added `prompts/09-model-cost-routing.md`.
- Added `templates/MODEL_ROUTING_LOG.md`.
- Added `docs/MODEL_COST_ROUTING.zh-TW.md`.
- Added a Web GPT-5.5 Pro review prompt for this release.

## Why This Matters

Nontechnical owners often waste expensive model time on small tasks, then under-review dangerous tasks.

This release gives Codex a simple rule:

```text
Use cheap/local models for drafts.
Use Codex for local execution and proof.
Use premium reviewers for high-risk or final review.
Require human approval for money, trades, production, secrets, and irreversible actions.
```

## Important Limit

This release does **not** automatically switch model providers, use paid accounts, buy tokens, or execute external paid tools.

It only makes the routing decision explicit so the human and Codex can avoid waste while keeping high-risk work protected.

## Upgrade Notes

If you already installed v0.1.10, reinstall the Skills to get the new routing rules.
