# Verification and Reflection

Verification checks whether a result satisfies evidence and acceptance criteria. Reflection is a model-driven review of the approach, assumptions, or likely errors before continuing.

## Core idea

The two concepts are related but not equivalent. Verification should use objective checks where possible: tests, schemas, calculations, source comparison, or permission rules. Reflection is useful for discovering omissions or proposing revisions, but it remains another model output and can repeat the original mistake.

## Practical use

- Run tests after generating code.
- Compare claims against retrieved evidence.
- Validate structured output against a schema and domain rules.
- Ask a second pass to identify missing cases or contradictions.
- Require human review for high-impact changes.

## Trade-offs and limitations

Additional review increases latency and cost. Self-review is correlated with the original generation and is weaker than independent evidence. Repeated reflection can also cause unnecessary changes to an already correct result.

## Common mistakes

- Using “check your work” as the only validation.
- Treating a second model answer as independent proof.
- Failing to define what success means.
- Re-running generation instead of inspecting deterministic test failures.

## Related concepts

- [Agents and Automation](../../)
- [Planning](../planning/)
- [Evals](../../../evaluation-and-operations/sub/evals/)
- [Human in the Loop](../human-in-the-loop/)
