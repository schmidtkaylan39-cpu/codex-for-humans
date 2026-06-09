# Real Example: Clinic Booking System

This walkthrough is for nontechnical users. You do not need to read code. You only need to know what to ask Codex to do, what evidence to expect, and when to switch from building to delivery auditing.

## Scenario

You want to build a small clinic booking system.

Goal:

```text
Patients can choose a date and time.
Clinic staff can see the booking list.
The same time slot cannot be booked twice.
If a patient enters invalid information, the system should show a clear error message instead of breaking.
```

## Step 1: Start From 0-1

Use:

```text
$nontechnical-codex-project-controller
```

Paste this into Codex:

```text
I am a nontechnical owner and I cannot read code.
I want to build a clinic booking system.

Core goals:
1. Patients can choose a date and time.
2. Clinic staff can see the booking list.
3. The same time slot cannot be booked twice.
4. Invalid patient input should show a clear error message.

Do not start coding immediately.
First, create a current-state inventory, task classification, task contract, success criteria, verification plan, high-risk stop points, and the smallest executable next step.
```

## Step 2: Expect A Task Contract First

Codex should respond in plain language, roughly like this:

```text
Task Contract
- Objective: Create a small booking system with booking, listing, duplicate prevention, and error messages.
- In scope: booking form, booking list, duplicate time-slot prevention, input validation.
- Out of scope: payments, SMS reminders, user login, production deployment.
- Success criteria: new booking works; duplicate time slots are blocked; invalid input shows a message.
- Verification: open the local page and test booking, duplicate booking, and invalid input.
- High-risk stop points: payments, SMS, real patient data, production deployment, login, or external services require a new approval.
```

If Codex immediately changes many files without a task contract, ask it to stop and create the task contract first.

## Step 3: Let Codex Execute The Smallest Version

After you agree with the task contract, say:

```text
I approve this task contract.
Please build the smallest working version.
When finished, give me test results and a nontechnical acceptance script.
```

Do not accept only:

```text
Done.
```

Ask for:

- changed files
- how to open or run it
- what verification was run
- what remains untested
- what failure would look like

## Step 4: Use The Acceptance Script

Codex should give you a script like this:

```text
Acceptance Script
1. Open the booking page.
2. Enter name, phone, date, and time.
3. Submit the booking.
4. Expected result: the booking appears in the booking list.
5. Try booking the same date and time again.
6. Expected result: the system says the time slot is already booked.
7. Submit with the name field empty.
8. Expected result: the system says the name is required.
```

You do not need to read code. You only need to check whether the visible behavior matches the script.

## Step 5: When It Looks 70-90 Percent Done, Switch To Audit

Use:

```text
$nontechnical-project-readiness-auditor
```

Paste this into Codex:

```text
This clinic booking system looks mostly complete.
Do not make major changes. Do not fix bugs yet.
First, do a read-only delivery readiness audit.

Please output:
1. Current state inventory
2. Current score
3. Untested item classification
4. High-risk checklist
5. Delivery readiness verdict
6. Web GPT review packet
7. Nontechnical acceptance script
8. Minimal closeout tasks
```

## Step 6: How To Read The Audit Result

A good audit is not just a high score.

A useful result looks like this:

```text
Current score: 86/100
The score is not delivery approval.

Proven:
- Local page opens.
- Creating a booking was tested.
- Duplicate time-slot prevention was tested.

Must close before delivery:
- Invalid input behavior has not been tested.
- Mobile screen size has not been checked.
- It is unknown whether bookings persist after refresh.

Minimal closeout tasks:
1. Test invalid input.
2. Check mobile layout.
3. Add a short operation guide.
```

## Step 7: When To Use Web GPT

For a small local demo, Web GPT may not be necessary.

If you want to use the system with real clinic staff, real patient data, payments, SMS, login, or production deployment, ask for outside review first.

Web GPT should review:

- missed risks
- missing tests
- unclear instructions
- overengineering

Web GPT must not claim that it ran your local tests.

## Key Rule

```text
0-1: build with Project Controller.
70-100: audit with Readiness Auditor.
Web GPT: outside review only.
Local evidence decides delivery.
```

