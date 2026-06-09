# Codex for Humans v0.1.3

This release adds mode routing based on real use feedback from an SEO Autopilot implementation.

## What Changed

- Added three operating modes to `nontechnical-codex-project-controller`:
  - Quick Mode for small low-risk tasks
  - Full Mode for medium and large tasks
  - High-Risk Mode for API keys, deployment, auth, real data, CMS publishing, outreach, paid tools, destructive work, and other high-risk operations
- Added three new prompt presets:
  - `prompts/05-quick-daily-task.md`
  - `prompts/06-full-project-task.md`
  - `prompts/07-high-risk-task.md`
- Updated the 0-100 router prompt to classify Quick / Full / Readiness Audit / High-Risk.
- Updated README and first-10-minutes guide to explain when not to use the full workflow.
- Updated public-readiness checks to verify the new prompt files.

## Why

The workflow helps medium, large, long-running, and high-risk tasks by reducing rework, missed evidence, and unsafe execution. But small tasks should not pay the full process cost.

## Core Rule

```text
Small low-risk tasks: Quick Mode.
Medium and large tasks: Full Mode.
Any high-risk task: High-Risk Mode.
Near-delivery projects: Readiness Auditor.
```

Do not repeat the full SOP every round.

