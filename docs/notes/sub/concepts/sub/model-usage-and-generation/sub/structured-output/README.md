# Structured Output

<!--
ai_content:
  managed: true
  l10n: true
-->

Structured output is model-generated data that follows a defined machine-readable format, such as JSON, a JSON Schema, XML, CSV, or a typed function-call argument object.

## Core idea

Applications often need values that can be parsed and validated rather than prose that merely looks structured. Reliable structured output combines a clear schema, model or decoder support, validation, and error handling. The schema describes shape and types; it does not guarantee that the values are factually correct.

## Practical use

- Extract entities, classifications, or action parameters.
- Produce inputs for APIs and workflow steps.
- Enforce required fields and enumerated values.
- Separate machine-readable results from user-facing explanations.
- Validate output before executing any consequential action.

## Implementation considerations

- Prefer native schema-constrained generation when the provider supports it.
- Keep schemas small and avoid deeply ambiguous unions.
- Define optional fields intentionally instead of accepting arbitrary missing data.
- Reject or repair invalid output through a bounded retry policy.
- Apply domain validation after syntax validation, such as date ranges or permitted identifiers.

## Trade-offs and limitations

Strict schemas improve integration reliability but can make nuanced answers harder to represent. Large schemas consume context and may reduce model accuracy. A syntactically valid object may still contain invented IDs, unsupported claims, or unsafe values.

## Common mistakes

- Parsing free-form prose with fragile regular expressions.
- Executing generated arguments without validation.
- Treating schema compliance as factual verification.
- Requesting both unrestricted prose and strict JSON in the same output channel.

## Related concepts

- [Model Usage and Generation](../../)
- [Constrained Generation](../constrained-generation/)
- [Function Calling](../../../agents-and-automation/sub/function-calling/)
- [Guardrails](../../../safety-privacy-and-reliability/sub/guardrails/)
