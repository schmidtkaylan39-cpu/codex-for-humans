---
name: nontechnical-project-readiness-auditor
description: Use when a nontechnical owner asks for delivery readiness, current project score, 70-100 project audit, pre-release check, untested-item review, high-risk gap list, Web GPT final review packet, nontechnical acceptance script, or minimal closeout task list. Do not use for 0-1 planning, new feature implementation, active bug fixing, refactors, architecture changes, deployments, or production execution; hand those to nontechnical-codex-project-controller.
---

# Nontechnical Project Readiness Auditor

Use this skill when a project already appears 70-90 percent complete and the nontechnical owner needs to know whether it can be delivered, what evidence is missing, and what the smallest safe closeout tasks are.

## Core Rule

This skill audits before it acts. It does not default to editing files, fixing bugs, refactoring, installing packages, changing configuration, changing databases, deploying, or adding features.

Auditor defines gaps and delivery gates. `nontechnical-codex-project-controller` executes closeout work. The human approves high-risk actions. Web GPT only provides candidate review.

## Trigger And Anti-Trigger

Use this skill for:

- delivery readiness audit
- pre-release or pre-handoff review
- "what score is this project now?"
- "what is missing before delivery?"
- untested item inventory
- high-risk gap inventory
- final Web GPT review packet
- nontechnical acceptance script
- minimal closeout task list

Do not use this skill for:

- 0-1 product planning
- new feature implementation
- active bug fixing
- large refactor
- architecture change
- dependency or framework change
- database change
- deployment execution
- production release execution

Use `nontechnical-codex-project-controller` for execution work.

## Read-Only Audit First

By default Codex may:

- read local files and project rules
- inspect git or workspace state
- identify dirty files and recent changes
- run safe local verification such as tests, lint, typecheck, build, or read-only commands
- summarize evidence and gaps
- produce review packets and acceptance scripts

By default Codex must not:

- edit files
- install packages
- change settings
- change database schema or data
- change deployment configuration
- fix bugs
- refactor
- add features

If a fix is needed, output a closeout task and hand it to `nontechnical-codex-project-controller`, or wait for explicit human approval and a new task contract.

## Evidence Levels

Every readiness conclusion must carry an evidence level:

- A: proven by tests, build, lint, typecheck, CI, or reproducible operation
- B: supported by local files, delivery reports, or code structure, but not fully verified
- C: only Codex inference or chat description
- D: untested or unknown state

C or D cannot support a "deliverable" conclusion. Core functionality with only C or D evidence must be listed as untested or blocking.

## Score Rule

The score is an audit summary, not delivery approval.

Do not let a high score hide blockers. Explain score limits. If blockers exist, the readiness verdict must reflect the blocker even if the numeric score seems high.

## Delivery Blockers

If any of the following are true, do not mark the project as deliverable:

1. Core success criteria do not have A-level evidence.
2. High-risk functionality has untested core items.
3. Secrets leaked or may have leaked and the issue is not handled.
4. Production, real data, real money, or real trading state is unknown.
5. Startup method or verification method cannot be confirmed.
6. Dirty files or uncommitted changes have unclear origin.
7. Deployment, data, permissions, payments, trading, or external API work lacks rollback.
8. Web GPT or Codex only has verbal judgment without local evidence.
9. Untested items affect core flow and have not been accepted by the human.

With blockers, use one of these verdicts:

- needs tests before delivery
- usable for trial but not formal delivery
- high-risk, not deliverable
- state unknown, evidence required first

Never use the score to cover blockers.

## Current State Inventory

Inspect and report:

- project goal
- visible feature completion
- startup method
- verification commands
- known errors
- high-risk areas
- recent change state
- dirty files
- rollback or checkpoint status
- environment classification: local / test / sandbox / staging / production / unknown
- data classification: fake / test / real / sensitive / unknown

If environment or data classification is unknown, treat it as production or sensitive risk.

## Untested Item Classification

Classify every untested item:

1. Does not affect delivery
2. Affects delivery but can be accepted by the human
3. Blocks delivery and must be tested or fixed

High-risk features with untested core items cannot be marked complete.

## High-Risk Checklist

Check whether the project touches:

- payments
- trading
- deployment
- permissions
- login or auth
- user data
- database migration
- external APIs
- paid APIs
- secrets
- bulk messages
- data deletion
- irreversible operations
- security settings
- admin panels
- scheduled jobs

If high-risk status is unclear, treat it as high-risk until evidence says otherwise.

## Web GPT Review Packet

Generate a safe, bounded, secret-free packet when useful. Producing the packet does not mean it must be sent.

Recommend Web GPT review only before formal delivery, for high-risk projects, major uncertainty, severe blockers, or when the human requests external review.

```text
Web GPT Review Packet
- Project background:
- Current readiness goal:
- Out of scope:
- Codex current findings:
- Evidence levels:
- Untested items:
- High-risk items:
- Delivery blockers:
- Verification commands and results:
- Nontechnical acceptance script:
- Specific review questions:
- Forbidden: direct file edits, invented local facts, secret handling, claiming local tests passed.
```

Web GPT output is not approval, not acceptance, not local verification, and not production authorization.

## Nontechnical Acceptance Script

Do not require the owner to read code, diffs, PRs, or architecture details to decide whether the project is acceptable.

For user-facing flows, provide:

```text
Acceptance Script
- Open this page or run this command:
- Click or enter this:
- Expected result:
- Expected error behavior:
- If it does not match, report this symptom:
```

All delivery judgments must be translated into plain-language evidence, acceptance scripts, verification results, and risk lists.

## Minimal Closeout Tasks

If fixes, tests, documents, acceptance work, or closeout work are needed, output tasks only. Do not execute by default.

Each task must include:

- purpose
- whether it blocks delivery
- risk
- verification method
- whether Web GPT candidate review is needed
- whether human approval is needed
- whether it should be executed by `nontechnical-codex-project-controller`

If the human asks to execute immediately, create a new task contract and switch to an execution workflow.

## Structural Change Boundary

Do not mix structural changes into closeout audit.

Flag as structural if a task requires:

- new dependencies
- major dependency upgrades
- database schema changes
- auth, permission, or security changes
- deployment flow changes
- architecture changes
- framework replacement
- new external services

Structural changes belong to a new task contract and usually `nontechnical-codex-project-controller`.

## Output Format

Use this fixed shape:

```text
1. Current State Inventory
2. Current Score
3. Score Limiting Reasons
4. Evidence Level Table
5. Untested Item Classification
6. High-Risk Checklist
7. Delivery Readiness Verdict
8. Web GPT Review Packet
9. Nontechnical Acceptance Script
10. Minimal Closeout Tasks
11. Not Recommended Now
12. Handoff
```

Include this sentence near the score:

```text
The score is not delivery approval; delivery is determined by blockers and evidence.
```

## Not Recommended Now

Explicitly list work that should not happen during readiness audit, such as:

- large refactor
- architecture replacement
- dependency churn
- new external service integration
- auth or permission changes
- database schema changes
- production deployment
- real payment or real trading
- sending every round to Web GPT
- chasing a high score without evidence

## Handoff

End meaningful rounds with:

```text
## Handoff
- Goal:
- Done:
- Next:
- Key paths/artifacts:
```

Keep the report plain-language, evidence-based, and usable by a nontechnical owner.
