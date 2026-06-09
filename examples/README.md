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
