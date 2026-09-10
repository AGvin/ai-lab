# Documentation Requirements

## Requirements

- Teach prompt injection as instruction-like adversarial content that attempts to redirect model behavior away from the intended task or authority structure, including indirect injection through retrieved pages, emails, documents, screenshots, tool results, or other data.
- Keep stable system/developer instructions, task data, retrieved evidence, and untrusted content semantically separated where the application can preserve those roles.
- For systems that access data or cause consequential effects, pair model-facing instructions with actual application permission checks, validation, constrained capability scope, isolation/sandboxing, approval gates, or equivalent external controls appropriate to the risk.
- Do not store secrets in model-visible prompt/context merely because the channel is privileged, and do not rely on prompt wording as the sole defense against unauthorized actions.
- Re-evaluate defenses after model, provider interface, tool contract, or context-construction changes because effective attack/defense behavior can shift.
- Keep concrete vulnerabilities, provider mitigations, product controls, and incident evidence source-backed rather than universalizing them.

## Validation

- Retrieved/user-provided instruction-like text remains untrusted unless application authority explicitly says otherwise.
- Consequential actions are protected by controls outside free-form model compliance.
- Prompt injection is distinguished from ordinary conflicting instructions and from generic model hallucination.
