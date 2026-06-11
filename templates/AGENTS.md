# Project Agent Rules

## Owner Preference

The owner is nontechnical and should not be required to read code.

Use plain language. When a decision is needed, provide A/B/C choices with business tradeoffs.

## Source Of Truth

Local files, tests, builds, screenshots, and generated reports are the source of truth.

Chat history and outside model opinions are not proof.

## Workflow

1. Inspect current files before planning.
2. Freeze a task contract for medium, large, or high-risk work.
3. Make small targeted changes.
4. Run the closest useful verification.
5. Report evidence, untested items, and next step.

## Model Cost Routing

Use the cheapest safe model tier:

- Cheap / local / mini for drafts, summaries, wording, and low-risk read-only checks.
- Standard Codex for local execution, file edits, tests, debugging, and proof.
- Premium reviewer for high-risk review, final review, severe ambiguity, or repeated failures.
- Human approval for money, trades, production, secrets, paid tools, external account actions, or irreversible actions.

Do not claim automatic provider switching unless the environment supports it and the owner approved it.

## High-Risk Stop Points

Stop for explicit owner approval before:

- real money
- real trades
- production deployment
- real user data
- permissions or auth changes
- deletion or irreversible actions
- secrets or credentials
- paid external services

## Handoff

End meaningful work with:

```text
## Handoff
- Goal:
- Done:
- Next:
- Key paths/artifacts:
```
