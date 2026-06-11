# Examples

## Full Beginner Walkthrough

Traditional Chinese:

```text
examples/clinic-booking-system.zh-TW.md
```

English:

```text
examples/clinic-booking-system.en.md
```

Readiness audit micro case:

```text
examples/readiness-audit-micro-case.zh-TW.md
```

## Example 1: New Project

Use:

```text
prompts/01-start-new-project.md
```

Then describe the business goal:

```text
I want a simple booking system for a small clinic. Patients can choose a time, staff can confirm appointments, and the system should prevent double booking.
```

Expected Codex behavior:

- classify the task
- create a task contract
- identify high-risk areas
- build in small rounds
- verify with tests or live smoke checks
- report in plain language

## Example 2: Nearly Finished Project

Use:

```text
prompts/02-audit-70-to-100-project.md
```

Then describe the situation:

```text
The app can already open and most features work, but I do not know if it is ready to publish.
```

Expected Codex behavior:

- inspect current state
- avoid editing first
- classify untested items
- list delivery blockers
- prepare a Web GPT review packet
- produce a minimal closeout task list

## Example 3: Web GPT Review

Use:

```text
prompts/03-web-gpt-55-pro-final-review.md
```

Paste the Web result back into Codex with:

```text
prompts/04-import-web-review-to-codex.md
```

## Example 4: Model Cost Routing

Use:

```text
prompts/09-model-cost-routing.md
```

Then describe the task:

```text
I want to know whether this should stay in Codex, be drafted by a cheaper/local model, or be sent to Web GPT Pro for final review.
```

Expected Codex behavior:

- classify the task size and risk
- recommend the safest cost tier
- keep local execution and proof inside Codex
- require human approval before paid tools, production, secrets, money, or irreversible actions
