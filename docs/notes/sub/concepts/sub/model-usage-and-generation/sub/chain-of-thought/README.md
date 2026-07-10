# Chain of Thought

<!--
ai_content:
  managed: true
  l10n: true
-->

Chain of thought refers to intermediate reasoning steps used to support multi-step problem solving. These steps may appear as generated text, remain internal to a reasoning model, or be represented through explicit workflow state.

## Core idea

Breaking a difficult problem into intermediate steps can improve planning and error detection. However, a fluent reasoning trace is not proof that the conclusion is correct. Some systems deliberately do not expose private internal reasoning and instead provide concise explanations, calculations, evidence, or verifiable intermediate results.

## Practical use

- Decompose a task into independently checkable subproblems.
- Ask for assumptions, calculations, evidence, and a final conclusion.
- Use external tools for arithmetic, code execution, retrieval, or validation.
- Preserve an auditable workflow trace rather than relying on hidden reasoning.

## Trade-offs and limitations

Long visible reasoning consumes tokens and may reveal sensitive prompt details or provide an unreliable post-hoc narrative. For production systems, structured plans and tool traces are often more useful than unrestricted reasoning text.

## Common mistakes

- Treating a detailed rationale as guaranteed correctness.
- Requiring disclosure of hidden internal reasoning as a security or audit mechanism.
- Allowing intermediate speculation to be presented as established fact.
- Using verbose reasoning where a deterministic calculation would be safer.

## Related concepts

- [Model Usage and Generation](../../)
- [Reasoning Models](../reasoning-models/)
- [Planning](../../../agents-and-automation/sub/planning/)
- [Verification and Reflection](../../../agents-and-automation/sub/verification-and-reflection/)
