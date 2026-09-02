# System Prompts

Legacy residual retained for system-prompt design, maintenance, tool-policy, and security-implementation guidance that are intentionally outside the canonical System Prompts concept owner.

> **Migration note:** System-prompt identity, provider/interface variability, instruction-hierarchy separation, stable-instruction versus dynamic-data boundaries, non-security-boundary semantics, conflict/injection/update limitations, and the need for external authorization enforcement are already preserved in `docs/sub/concepts/sub/models/sub/interaction/sub/prompting/sub/system-prompts/`. The remaining material below stays here until its exact learning, trustworthy-AI, application-engineering, or operational-policy owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Design and maintenance residual

Useful system-prompt design practices include:

- define the assistant's purpose, permitted scope, and durable behavioral constraints explicitly;
- keep stable policy separate from rapidly changing task data, retrieved documents, and examples;
- state tool-use expectations and consequential-action validation rules when they are part of the application contract;
- keep durable output and communication conventions internally consistent;
- avoid unnecessary rule duplication and conflicting instructions that make maintenance and effective priority harder to reason about;
- do not store secrets in prompt text merely because the prompt is supplied through a privileged interface.

These are implementation and maintenance practices rather than universal System Prompts semantics.

## Security and enforcement residual

Treat retrieved web pages, emails, documents, tool results, and user-provided data as untrusted inputs even when they contain instruction-like text. For systems that can access data or perform consequential actions, pair model-facing instructions with actual application permissions, authorization checks, validation, isolation, or sandboxing as appropriate.

Do not use the system prompt as the sole defense against prompt injection or unauthorized actions.

## Regression and operational residual

System-prompt behavior can change when the model, provider interface, hidden platform context, tool contract, or context-construction pipeline changes. Re-evaluate important prompt behavior after such changes instead of assuming prior compliance remains unchanged.

These design, security, and maintenance practices remain migration source material until their exact learning, trustworthy-AI, application-engineering, or operational-policy owners are verified.
