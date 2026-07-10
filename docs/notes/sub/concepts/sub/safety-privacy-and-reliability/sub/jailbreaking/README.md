# Jailbreaking

Jailbreaking is an attempt to bypass a model's configured safety, policy, or behavior restrictions through crafted inputs or interaction patterns.

## Core idea

Jailbreaks may use role-play, obfuscation, translation, encoding, fictional framing, multi-turn pressure, or conflicting instructions. They target the model's behavior layer, but successful jailbreaks become operationally dangerous only when the surrounding system grants sensitive data or tools.

## Defensive use

- Red-team prompts and interaction flows.
- Measure refusal consistency.
- Test multilingual and encoded inputs.
- Evaluate whether tool permissions remain protected after policy bypass.

## Trade-offs and limitations

No static prompt filter blocks every jailbreak. Stronger refusal behavior may reduce useful responses in legitimate safety, research, or educational contexts. Continuous evaluation is required as models and attacks change.

## Common mistakes

- Testing only famous public jailbreak prompts.
- Treating model refusal as protection for external systems.
- Ignoring indirect and multimodal attack paths.
- Publishing sensitive bypass details without a clear defensive purpose.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Prompt Injection](../prompt-injection/)
- [Model Alignment](../model-alignment/)
- [Evals](../../../evaluation-and-operations/sub/evals/)
