# Codex for Humans

小白也能用的 Codex 專案總控 Skills。

![Codex for Humans hero](docs/assets/tutorial-card-image2.png)

Codex for Humans is an unofficial workflow kit for nontechnical owners who want to use Codex to build software projects without reading code.

It is not a single magic prompt. It is a small system of Codex Skills, prompts, and templates that helps you:

- turn vague ideas into clear task contracts
- make Codex work in small, testable rounds
- separate building from delivery readiness auditing
- require evidence before calling work "done"
- use Web GPT as an outside reviewer without treating it as local proof
- recommend a cost-aware model tier without pretending to auto-switch providers
- avoid high-risk actions such as real payments, real trades, production deployment, real user data, secrets, and irreversible changes without explicit approval

## 10-Second Map

```mermaid
flowchart LR
    A["I have an idea or task"] --> K["Model cost routing<br/>cheap / Codex / premium"]
    K --> B{"What stage is it?"}
    B -->|Start / build / fix| C["Use Project Controller<br/>0-1 execution"]
    B -->|Mostly done| D["Use Readiness Auditor<br/>70-100 audit"]
    C --> E["Codex works locally<br/>files, tests, evidence"]
    D --> F["Find blockers<br/>untested items, risks, closeout tasks"]
    F -->|Need fixes| C
    E --> G{"High risk or final review?"}
    G -->|Yes| H["Send bounded packet<br/>to Web GPT"]
    H --> I["Import candidate opinion<br/>back to Codex"]
    I --> E
    G -->|No| J["Plain-language delivery<br/>and acceptance script"]
```

Simple rule:

```text
0-1: build with $nontechnical-codex-project-controller
70-100: audit with $nontechnical-project-readiness-auditor
Model routing: choose the cheapest safe tier, but never cheap-route high-risk proof
Web GPT: outside review only, never local proof
```

Codex executes locally.
Web GPT only gives candidate review.
Tests, builds, local evidence, and human approval decide whether something is actually ready.
Readiness score is only a summary. Blockers and evidence decide delivery.

## Safety First

Codex for Humans helps you structure Codex work. It does not guarantee that your software is correct, secure, legal, deployable, or safe for real money.

Before using this workflow with production systems, real user data, payments, trading, permissions, security settings, or irreversible operations:

- use sandbox, fake data, test accounts, dry run, or local simulation first
- do not paste secrets, API keys, tokens, cookies, passwords, or private keys into chat
- require explicit human approval before high-risk actions
- require a rollback or recovery plan before deployment, database changes, permissions changes, payments, trading, or destructive operations
- ask a qualified human reviewer when legal, financial, medical, security, or compliance risk exists

Web GPT review is only an outside opinion. It is not local test evidence, not approval, and not proof that the project is safe to ship.

Repo checks and GitHub Actions are guardrails for this workflow kit. They do not prove that your own software project is secure, legal, deployable, or production-ready.

Model cost routing is guidance only. This repo does not automatically switch providers, buy tokens, use paid APIs, or move work to another model. Any real provider switch, paid usage, production action, or account connection still needs explicit approval.

## Who This Is For

- You do not read code, but you want to build software with Codex.
- You get lost when Codex spends many tokens, fixes many bugs, and changes many files.
- You want a repeatable SOP for every project.
- You want to separate 0-1 building from 70-100 delivery checking.
- You want Web GPT or another model to review plans without replacing local evidence.

## Beginner Tutorial

If this is your first time using Codex Skills, start here:

```text
docs/BEGINNER_TUTORIAL.zh-TW.md
```

It includes beginner-friendly diagrams for:

- choosing the right Skill
- installing the Skills
- checking evidence instead of only asking for a score

## Agent Discipline Add-on

This repo now includes a lightweight belief-revision rule inspired by `soplint`:

```text
docs/SOPLINT_LESSONS.zh-TW.md
prompts/08-belief-revision-check.md
templates/BELIEF_REVISIONS.jsonl.example
```

Use it when Codex changes its mind, changes a score, or discovers that an earlier completion claim was wrong.

## Model Cost Routing Add-on

This repo also includes a lightweight model-routing rule:

```text
docs/MODEL_COST_ROUTING.zh-TW.md
prompts/09-model-cost-routing.md
templates/MODEL_ROUTING_LOG.md
```

Use it when you want Codex to decide whether a task should stay in normal Codex, be drafted by a cheaper/local model, or be escalated to Web GPT Pro / another premium reviewer. The rule is conservative: high-risk proof, delivery approval, secrets, trading, payments, deployment, and production work must not be delegated to cheap models as final authority.

## What Is Inside

```text
codex-for-humans/
+-- skills/
|   +-- nontechnical-codex-project-controller/
|   +-- nontechnical-project-readiness-auditor/
+-- prompts/
+-- templates/
+-- docs/
+-- examples/
```

## The Two Core Skills

### 1. 0-1 Project Controller

Use this when you want Codex to plan, build, debug, test, and deliver a project or feature.

Skill name:

```text
$nontechnical-codex-project-controller
```

Best for:

- New project
- New feature
- Bug fix
- Long Codex task
- High-risk task that needs approval gates
- Web GPT review packet before or after Codex work

### 2. 70-100 Readiness Auditor

Use this when a project is already mostly done and you want to know what is missing before delivery.

Skill name:

```text
$nontechnical-project-readiness-auditor
```

Best for:

- Delivery readiness audit
- Current score
- Untested item list
- High-risk gap list
- Final Web GPT review packet
- Nontechnical acceptance script
- Minimal closeout task list

## Quick Start

Visual install guide:

![Install flow](docs/assets/install-flow.svg)

GIF install demo:

![Install demo](docs/assets/install-demo.gif)

1. Find your Codex Skills folder.

Codex Skills 的安裝路徑可能因 Codex 版本或環境不同而不同。

請優先依你目前 Codex 版本的官方文件或 `/skills` 說明確認 Skills 路徑。

Common paths may include:

- `~/.agents/skills/`
- `~/.codex/skills/`

If one path does not work, use the Skills directory shown by your Codex app or CLI.

2. Install the two Skill folders.

New users should prefer one-click install:

Only run these scripts from a repo you trust. If unsure, use dry-run first and confirm the target path.

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

macOS / Linux:

```bash
bash ./scripts/install.sh --dry-run
bash ./scripts/install.sh
```

Manual install is also possible, but choose only one Skills path.

Windows:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills"
Copy-Item -Recurse -Force .\skills\* "$env:USERPROFILE\.agents\skills\"
```

macOS / Linux:

```bash
mkdir -p ~/.agents/skills
cp -R ./skills/* ~/.agents/skills/
```

If your Codex shows `.codex/skills` instead, use that path instead. Do not blindly install to both paths.

3. Restart Codex and verify the Skills are visible.

可嘗試使用 `/skills` 或輸入 `$` 查看可用 Skills。確認能看到：

- `nontechnical-codex-project-controller`
- `nontechnical-project-readiness-auditor`

If you cannot see them, check:

1. Skill 是否放在正確的 Codex Skills 目錄
2. 每個 Skill 資料夾內是否有 `SKILL.md`
3. 是否重新啟動 Codex
4. 是否放錯到 repo 內，而不是 Codex 的 Skills 目錄

4. Open Codex in your target project.

5. Use one of the prompts in `prompts/`.

For a brand-new project, use:

```text
prompts/01-start-new-project.md
```

For daily small tasks, use:

```text
prompts/05-quick-daily-task.md
```

For medium or large tasks, use:

```text
prompts/06-full-project-task.md
```

For high-risk tasks, use:

```text
prompts/07-high-risk-task.md
```

When Codex changes its mind or changes a score, use:

```text
prompts/08-belief-revision-check.md
```

When you want Codex to choose the cheapest safe model tier, use:

```text
prompts/09-model-cost-routing.md
```

For a nearly finished project, use:

```text
prompts/02-audit-70-to-100-project.md
```

For a real beginner walkthrough, read:

```text
examples/clinic-booking-system.zh-TW.md
examples/clinic-booking-system.en.md
```

For a visual install guide, read:

```text
docs/INSTALL_VISUAL.zh-TW.md
```

For one-click install, read:

```text
docs/ONE_CLICK_INSTALL.zh-TW.md
```

For the GIF install guide, read:

```text
docs/INSTALL_GIF.zh-TW.md
```

For your first 10 minutes, read:

```text
docs/FIRST_10_MINUTES.zh-TW.md
```

## Simple Operating Rule

Use this split:

```text
Small low-risk task: Quick Mode with $nontechnical-codex-project-controller
0-1: build with $nontechnical-codex-project-controller
70-100: audit with $nontechnical-project-readiness-auditor
Model cost: cheap/local for drafts, Codex for execution, premium for high-risk review
High-risk: stop first with High-Risk Mode
```

If the audit finds work that must be fixed, hand that task back to the project controller.

## Do Not Use The Full Workflow For Everything

Codex for Humans is meant to prevent rework and risk, not to make every tiny task heavy.

Use the lightest safe mode:

- Quick Mode: small low-risk tasks, copy edits, tiny UI changes, simple docs updates, single clear bugs
- Full Mode: new features, multi-file changes, product flows, long-running debugging, meaningful integrations
- High-Risk Mode: API keys, payments, deployment, auth, real data, CMS publishing, outreach email, paid tools, deletion, permissions, or irreversible actions

Small tasks only need short classification, focused action, and acceptance.
Medium, large, and high-risk tasks need stronger contracts and evidence.
Do not paste or repeat the full SOP every round.

## Recommended Project Setup

For each software project you manage with Codex:

1. Copy `templates/AGENTS.md` into your target project root.
2. Fill in your project goal, test commands, risk areas, and handoff rules.
3. Keep project-specific details in your project files, not inside the reusable Skills.

Recommended files inside your own project:

- `AGENTS.md`: project-level Codex instructions
- `PROJECT_RULES.md`: project-specific rules
- `DECISION_LOG.md`: why decisions were made
- `EVIDENCE_LEDGER.md`: what was changed and how it was verified
- `RISK_REGISTER.md`: known risks and high-risk areas

The Skills provide the workflow.
Your project files provide the project-specific facts.

`AGENTS.md` can point Codex to the other files, or you can explicitly ask Codex to read them.

## Web GPT Review Loop

Web GPT can help review plans, risks, missing tests, and logic gaps.

But Web GPT does not prove the local project works.

Use this rule:

```text
Codex executes locally.
Web GPT reviews as an outside opinion.
Tests, builds, screenshots, logs, and local artifacts are the proof.
```

See:

```text
docs/WEB_GPT_REVIEW_LOOP.zh-TW.md
```

## Safety

Do not publish secrets.

Never upload:

- API keys
- passwords
- access tokens
- cookies
- private Discord or exchange credentials
- production logs containing sensitive data
- account IDs or private user data

Before making this repo public, follow:

```text
docs/PUBLICATION_CHECKLIST.zh-TW.md
```

## Suggested Repo Description

```text
Unofficial Codex Skills and prompts for nontechnical owners to plan, build, audit, and ship software projects with evidence, not code reading.
```

## License

MIT. See `LICENSE`.
