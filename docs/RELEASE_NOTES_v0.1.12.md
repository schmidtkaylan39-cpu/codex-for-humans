# Codex for Humans v0.1.12

This release hardens model cost routing language after external review.

## What Changed

- Removed auto-sounding wording and replaced it with manual cost-tier recommendation wording.
- Added explicit limits: no automatic model switching, no provider switching, no paid-account use, and no guaranteed savings.
- Added budget cap, pricing-known, manual-switch, and external-data fields to routing templates.
- Clarified that human approval is a gate, not a model tier.
- Clarified that cheap cloud models are not the same as local models and must be treated as external review.
- Updated `prompts/09-model-cost-routing.md`, `templates/MODEL_ROUTING_LOG.md`, and both core Skills.

## Why This Matters

v0.1.11 was already safe enough to publish, but external review scored it 94/100 because some wording could still make beginners expect automatic model switching or guaranteed savings.

v0.1.12 makes the boundary harder:

```text
Codex recommends a cost tier.
Codex does not switch providers.
Codex does not spend money.
Codex does not guarantee a lower bill.
High-risk work still needs local evidence and human approval.
```

## Upgrade Notes

If you already installed v0.1.11, reinstall the Skills to get the stronger routing template fields and wording.
