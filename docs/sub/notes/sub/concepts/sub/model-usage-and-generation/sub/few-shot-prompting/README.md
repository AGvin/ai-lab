# Few-Shot Prompting

Few-shot prompting guides a model by including a small number of input-output examples that demonstrate the desired behavior.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Examples communicate patterns that are difficult to specify fully in prose, such as classification boundaries, formatting conventions, terminology, or transformation style. The model infers the task pattern from the demonstrations and applies it to a new input without updating its weights.

## Practical use

- Demonstrate a required output structure.
- Clarify edge cases in classification or extraction.
- Establish domain-specific terminology or labeling conventions.
- Show how to handle missing, ambiguous, or invalid input.

## Design guidance

Choose examples that are representative rather than merely easy. Include positive and negative cases when the distinction matters. Keep formatting consistent, and ensure examples do not contain accidental instructions that conflict with the task. For classification, balance labels enough that the model does not learn a misleading majority pattern.

## Trade-offs and limitations

Examples consume context and may anchor the model too strongly to superficial wording. Poor examples can reduce performance more than no examples. Few-shot prompting also does not provide durable knowledge or guarantee identical behavior across model versions.

## Common mistakes

- Providing examples that contradict the written instructions.
- Using only ideal cases and omitting important failures.
- Allowing the model to copy sensitive data from demonstrations.
- Assuming more examples always improve results.

## Related concepts

- [Model Usage and Generation](../../)
- [Prompting](../prompting/)
- [Context Window](../context-window/)
- [Evaluation Datasets](../../../evaluation-and-operations/sub/evaluation-datasets/)