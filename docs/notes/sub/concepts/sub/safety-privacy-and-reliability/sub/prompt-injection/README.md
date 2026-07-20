# Prompt Injection

Prompt injection is input designed to manipulate an AI system into ignoring intended instructions, revealing protected information, or performing unauthorized actions.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A model processes instructions and data in the same general medium: tokens. An attacker can therefore place instruction-like text in a user message and attempt to override policy or redirect tool use. Prompt hierarchy helps, but it is not a complete security boundary.

## Common goals

- Override system or application rules.
- Exfiltrate hidden prompts, secrets, or retrieved data.
- Cause unsafe tool calls.
- Bypass content or business-policy restrictions.
- Manipulate the model's final answer.

## Mitigation

Use least-privilege tools, deterministic authorization, strong trust boundaries, schema validation, output filtering, and human approval for consequential actions. Keep secrets out of model-visible context. Treat model output as untrusted input to every tool.

## Trade-offs and limitations

Prompt-based defenses can reduce simple attacks but cannot guarantee isolation. Aggressive filtering may also block legitimate instructions. Security must be enforced in the surrounding application.

## Common mistakes

- Asking the model to “ignore malicious instructions” and considering the problem solved.
- Exposing unrestricted shell, database, or browser tools.
- Returning secrets in tool results visible to the model.
- Treating a refusal in tests as proof of security.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Indirect Prompt Injection](../indirect-prompt-injection/)
- [Trust Boundaries](../trust-boundaries/)
- [Least Privilege](../least-privilege/)
