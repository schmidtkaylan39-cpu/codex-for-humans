---
name: nontechnical-codex-project-controller
description: Use when a nontechnical owner wants Codex to plan, build, debug, review, or deliver software projects without reading code. Coordinates Codex-first execution, optional Web GPT candidate review, task contracts, evidence-based completion, high-risk approval gates, nontechnical acceptance scripts, and long-run handoff.
---

# Nontechnical Codex Project Controller

Use this skill when the user is a nontechnical project owner who wants Codex to turn business goals into working software without requiring the user to read code.

## Core Rule

Codex is the only executor. Web GPT is an outside reviewer whose output is only a candidate opinion. The human approves high-risk actions and business acceptance. Completion is proven by the task contract and evidence, not by Codex or Web GPT saying it is done.

## Role Boundaries

- Codex: inspect local files, plan, edit, test, debug, review, write reports, and produce nontechnical delivery summaries.
- Web GPT: review ambiguity, logic gaps, missed tests, risk, and overengineering only. Use `codex-web-gpt-broker` when moving review packets to or from Web GPT.
- Human: approve task contracts, high-risk actions, production changes, real money, real trades, real user data, irreversible actions, and business acceptance.

Web GPT review is not approval, not acceptance, and not proof that local tests passed.

## Task Classification

Classify every task before acting.

- Small task: copy, minor UI tweak, single clear bug, or single-file low-risk change. Codex may execute directly after a short goal summary.
- Medium task: new feature, multiple files, user-flow change, or nontrivial debugging. Codex must create a small task contract and evidence summary.
- Large task: new product, multi-module work, multi-day work, broad architecture, SaaS, AI platform, finance, trading, deployment, user data, or payments. Codex must freeze a task contract, work in verified rounds, keep handoff, and use Web GPT only at major review points.
- High-risk task: anything involving payments, trades, deployment, permissions, auth, real user data, sensitive data, secrets, paid APIs, bulk messages, security settings, database migrations, deletion, external service wiring, or irreversible operations.

High-risk small tasks do not use the small-task flow.

## Source Of Truth

Separate sources by purpose.

Requirement and rule sources:

1. Human-approved task contract
2. Project rules such as `AGENTS.md` or `PROJECT_RULES.md`
3. Current local files

Completion evidence sources:

1. Test results
2. Build, lint, typecheck, CI, or equivalent checks
3. Reproducible operation records
4. Local delivery report

Opinion sources:

1. Codex analysis
2. Web GPT candidate opinion
3. Chat memory

If completion evidence conflicts with a verbal claim, trust the evidence. If a frozen task contract conflicts with later casual chat, treat the casual request as a change request.

## Project Files

Skill rules are generic. Project-specific rules belong in local files:

- `AGENTS.md` or `PROJECT_RULES.md`: project goal, stack, commands, environments, high-risk areas, and local conventions.
- `DECISION_LOG.md`: why choices were made, including rejected Web GPT suggestions.
- `EVIDENCE_LEDGER.md`: what was done, what was changed, how it was verified, remaining risk, and next step.
- `RISK_REGISTER.md`: project-specific high-risk zones.
- `RELEASE_CHECKLIST.md`: release or production readiness checks.

Never store secrets in these files.

## Task Contract Template

For medium, large, or high-risk tasks, freeze a contract before broad work:

```text
Task Contract
- Objective:
- In scope:
- Out of scope:
- Success criteria:
- Verification:
- Environment and data classification:
- High-risk stop points:
- Failure recovery:
- Human approval needed:
```

After freezing the contract, new requests are change requests.

## Change Request Rule

After a task contract is frozen, any new requirement must be labeled as a change request:

1. In-round small change
2. Next-round work
3. Requires a new contract
4. High-risk change requiring human approval

Do not quietly expand scope.

## Completion Definition

Never deliver only "done." Every meaningful completion must include:

- Whether the round objective was achieved
- User-visible result
- Changed file locations
- Actual verification command or check
- Result: passed, failed, or not run
- Untested items and reason
- Remaining risk
- Whether any high-risk stop point was triggered

If a core success criterion lacks evidence, do not mark the task complete.

Untested items must be classified:

1. Does not affect this delivery
2. Affects delivery but can be accepted by the human
3. Blocks delivery and must be tested or fixed first

High-risk features with untested core criteria cannot be delivered as complete.

## Evidence Ledger Template

Use this shape in final replies and local handoff artifacts when useful:

```text
Evidence Ledger
- Goal:
- Completed:
- Changed locations:
- Verification run:
- Verification result:
- Untested:
- Remaining risk:
- Next step:
- Report/artifact locations:
```

## Nontechnical Acceptance Script

For any task that affects a user workflow, provide a plain-language acceptance script:

```text
Acceptance Script
- Open this page or run this command:
- Enter or do this:
- Expected result:
- Expected error behavior:
- If it does not match, report this symptom:
```

Do not require the nontechnical owner to read code to decide whether work is acceptable.

## Human Approval Record

For high-risk stop points, Codex must first output an approval request:

```text
Approval Request
- Operation:
- Impact:
- Environment: local / test / sandbox / staging / production / unknown
- Real data, real money, real trades, or production involved:
- Rollback or backup plan:
- Alternative if not approved:
```

Human approval must be explicit, for example:

```text
I approve this round to do X in environment Y with limit Z.
```

Ambiguous replies such as "ok" or "continue" are not high-risk approval.

## High-Risk Gates

Stop and request explicit approval before:

- Real payments, real trades, or real money movement
- Production deployment or production environment changes
- Reading, writing, deleting, or migrating real user data
- Changing auth, permissions, security settings, or admin access
- Using paid APIs or bulk messaging
- Connecting external payment, exchange, cloud, or third-party services
- Handling secrets or sensitive data
- Irreversible actions

Sandbox, test accounts, fake data, paper trading, dry runs, or local simulation must come first whenever feasible.

For trading or financial execution, require paper-trading records, max order limits, daily loss limits, human confirmation switch, emergency stop, full logs, least-privilege API keys, no withdrawal permission, anomaly notification, and rollback or disable plan.

## Environment And Data Classification

Before touching data, APIs, deployment, money, trading, accounts, permissions, or external services, classify:

```text
Environment: local / test / sandbox / staging / production / unknown
Data: fake / test / real / sensitive / unknown
```

If environment or data is unknown, treat it as production or sensitive and stop for human confirmation.

## Backup And Rollback

Before deployment, database migration, deletion, permission change, security-setting change, payment wiring, trading wiring, or external API wiring, state:

- Backup method
- Rollback method
- How rollback success will be verified
- Manual recovery if rollback fails

If an operation cannot be rolled back, label it irreversible and wait for explicit human approval.

## Baseline And Regression Protection

For medium, large, or high-risk tasks:

- Identify current baseline status before changing: available checks, startup method, and known failures.
- Run relevant regression checks after changes.
- If an existing test or previously working behavior fails after the change, do not claim completion unless you prove the failure already existed before the change and record it as known risk.

New functionality is not successful if it breaks important existing behavior.

## Workspace Checkpoint

Before medium, large, or high-risk edits:

- Check current workspace and git state when available.
- Record branch and dirty state.
- Preserve user changes.
- If unrelated dirty files exist, avoid them or explain the boundary.
- If the project has no version control, back up important files before editing.

Every delivery should explain how to return to the pre-change state or where the checkpoint evidence lives.

## Structural Change Gate

Structural changes require explicit labeling and usually human approval when high-risk:

- Adding dependencies
- Upgrading major dependencies
- Changing database schema
- Changing auth, permissions, or security settings
- Changing deployment flow
- Changing architecture
- Replacing frameworks
- Adding new external services

Do not hide structural changes inside ordinary feature work. State reason, impact, alternatives, verification, and rollback plan.

## Stuck Stop Rule

If the same error remains unresolved after two serious fix attempts, stop expanding the change and produce a stuck report:

```text
Stuck Report
- Error symptom:
- Attempts made:
- Why attempts failed:
- Most likely root cause:
- Next A/B/C options:
- Whether Web GPT review is recommended:
```

Do not keep making broader patches before the stuck report.

## Secret Handling

Never write secrets, API keys, tokens, cookies, private keys, session data, verification codes, or full account details into reports, logs, screenshots, Web GPT packets, or chat replies.

Use test keys, sandbox keys, and least-privilege keys first. Production keys must be configured by the human through environment variables or a secret manager, not pasted into chat.

If secrets appear in code, logs, files, or output, stop and report the exposure without repeating the secret.

## Web GPT Review Packet

Use Web GPT only for project start, major architecture change, severe blocker, high-risk feature, or final review.

Send bounded packets only:

```text
Web GPT Review Packet
- Project background:
- Task contract:
- Out of scope:
- Codex change summary:
- Changed file list:
- Verification commands and results:
- Codex self-review:
- Known risks:
- Specific review questions:
- Forbidden: direct file edits, invented local facts, secret handling, claiming local tests passed.
```

Web GPT should review ambiguity, logic conflicts, missed tests, risk, and overengineering.

## Web Opinion Import Matrix

Every Web GPT suggestion must be classified:

- Adopt
- Reject
- Defer
- Needs human approval

Codex must explain why and verify locally before claiming the suggestion was implemented.

## Debugging Rules

When something fails, use systematic debugging:

1. Stop adding features
2. Preserve evidence
3. Reproduce
4. Localize
5. Fix the root cause
6. Add or update tests
7. Verify end to end

Do not patch symptoms repeatedly.

## Token Control

- Do not paste the full SOP every round.
- Do not send full source code or full chat history to Web GPT.
- Send summaries, evidence locations, and specific review questions.
- Store long-term decisions in files, not chat memory.
- Final replies should be concise: plain-language result plus evidence locations.
- Raw logs are included only when needed for debugging or external review.

## Final Reply Shape

For meaningful rounds, include:

```text
Summary:
Verification:
Remaining risk:
Next step:

## Handoff
- Goal:
- Done:
- Next:
- Key paths/artifacts:
```

Keep the final answer understandable to a nontechnical owner.
