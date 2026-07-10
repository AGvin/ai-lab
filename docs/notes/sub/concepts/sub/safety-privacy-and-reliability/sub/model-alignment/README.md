# Model Alignment

Model alignment is the effort to shape model behavior toward intended goals, policies, values, and user expectations.

## Core idea

Alignment can involve instruction tuning, preference optimization, constitutional rules, safety training, system prompts, guardrails, and application controls. It is not one solved property; behavior may differ across tasks, languages, and adversarial conditions.

## Practical dimensions

- Helpfulness and instruction following.
- Honesty and uncertainty communication.
- Harmlessness and policy compliance.
- Respect for user intent and authorization.
- Resistance to manipulation.

## Trade-offs and limitations

Different stakeholders may disagree about preferred behavior. Optimizing broad safety can create over-refusal, while optimizing compliance can increase misuse risk. Model-level alignment does not replace permissions or secure application architecture.

## Common mistakes

- Treating alignment as identical to censorship.
- Assuming one preference dataset represents all users.
- Measuring only refusal rates.
- Relying on aligned behavior to protect secrets or tools.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Preference Optimization](../../../training-and-adaptation/sub/preference-optimization/)
- [Guardrails](../guardrails/)
- [Jailbreaking](../jailbreaking/)
