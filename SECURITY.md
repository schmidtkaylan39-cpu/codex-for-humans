# Security Policy

Codex for Humans is an unofficial workflow kit. It helps structure Codex work, but it does not guarantee that generated software is secure, legal, deployable, or safe for production.

## Do Not Share Secrets

Never paste or commit:

- API keys
- passwords
- access tokens
- refresh tokens
- cookies
- private keys
- session data
- full private account IDs
- production logs with sensitive data
- real user data

## High-Risk Work

Before using Codex for Humans with production systems, real user data, payments, trading, permissions, security settings, database changes, or irreversible operations:

- use sandbox, fake data, test accounts, dry runs, or local simulation first
- require explicit human approval
- define a rollback or recovery plan
- keep least-privilege access
- ask a qualified human reviewer for legal, financial, medical, security, or compliance risk

## Web GPT Review

Web GPT or another outside model can help find missed risks and missing tests.

It is not local evidence, not approval, and not proof that a project is safe to ship.

## Reporting Issues

If you find a security issue in this repo's public docs, prompts, or Skills, open a GitHub issue without posting secrets.

If your issue includes private information, remove the private content first and describe the problem in general terms.

