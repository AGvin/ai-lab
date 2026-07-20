# Constrained Generation

Constrained generation restricts which tokens a model may emit so the output follows a grammar, schema, regular language, or permitted value set.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Instead of asking the model to imitate a format, the decoder masks invalid token choices during generation. This can ensure syntactically valid JSON, match a formal grammar, or restrict a field to known values. The constraint controls form, not factual accuracy or business validity.

## Practical use

- JSON or typed API payloads.
- SQL or domain-specific languages with a defined grammar.
- Enumerated classifications.
- Configuration files that must parse reliably.
- Tool arguments that will be validated before execution.

## Design considerations

Keep the grammar aligned with the tokenizer and runtime implementation. Avoid schemas with excessive nesting or ambiguous alternatives. Apply semantic validation after decoding, because a structurally valid date, path, or identifier may still be invalid or unsafe.

## Trade-offs and limitations

Constraints reduce formatting failures but can slow decoding or force the model into an allowed structure even when it lacks enough information. Very strict grammars may also prevent useful explanations or uncertainty fields.

## Common mistakes

- Treating valid syntax as verified meaning.
- Allowing unrestricted strings in fields later used as commands or paths.
- Using a schema so complex that the model cannot populate it reliably.
- Omitting fallback behavior when generation cannot satisfy the constraint.

## Related concepts

- [Model Usage and Generation](../../)
- [Structured Output](../structured-output/)
- [Function Calling](../../../agents-and-automation/sub/function-calling/)
- [Guardrails](../../../safety-privacy-and-reliability/sub/guardrails/)