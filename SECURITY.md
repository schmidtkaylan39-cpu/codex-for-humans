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

## If You Accidentally Expose A Secret

If you accidentally commit, paste, upload, or share a secret:

1. Stop using that secret immediately.
2. Revoke or rotate it in the original service.
3. Remove it from files, logs, prompts, screenshots, and review packets.
4. If it was committed to Git, clean Git history before making the repo public.
5. Do not paste the exposed secret into an issue, chat, Web GPT packet, support request, or public discussion.
6. Treat screenshots and logs as sensitive until you confirm the secret is gone.

Deleting the visible text is not enough if the secret was already committed, uploaded, or shared. Rotate or revoke first.

## Web GPT Review

Web GPT or another outside model can help find missed risks and missing tests.

It is not local evidence, not approval, and not proof that a project is safe to ship.

## Reporting Issues

If you find a security issue in this repo's public docs, prompts, or Skills, open a GitHub issue without posting secrets.

If your issue includes private information, remove the private content first and describe the problem in general terms.
