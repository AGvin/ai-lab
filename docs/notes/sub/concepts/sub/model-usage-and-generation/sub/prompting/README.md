# Prompting

<!--
ai_content:
  managed: true
  l10n: true
-->

Prompting is the practice of supplying instructions, context, examples, and constraints that guide a model toward a useful result.

## Core idea

A strong prompt defines the task clearly enough that the model does not need to infer essential requirements. It separates instructions from source material, states the desired output, and provides only the context needed to complete the task. Prompt quality matters, but it cannot compensate for missing knowledge, insufficient model capability, unavailable tools, or unreliable source data.

## Useful prompt components

- **Goal:** what must be accomplished.
- **Context:** facts and source material required for the task.
- **Constraints:** boundaries, exclusions, safety rules, and acceptance criteria.
- **Output contract:** format, length, language, schema, or audience.
- **Examples:** demonstrations when the desired pattern is difficult to describe.

## Practical use

- Put the most important requirement in direct language.
- Delimit untrusted documents or quoted content so they are not confused with instructions.
- Ask for explicit uncertainty when evidence is incomplete.
- Break complex work into verifiable stages or use an agentic workflow.
- Evaluate prompts against a fixed set of representative cases before treating them as production configuration.

## Trade-offs and limitations

Highly prescriptive prompts improve consistency but may reduce flexibility. Long prompts consume context and can introduce conflicting instructions. Prompt behavior also changes across model families and versions, so prompts require regression testing.

## Common mistakes

- Mixing task instructions with untrusted source text.
- Requesting vague qualities such as “better” without criteria.
- Adding many redundant rules that conflict with each other.
- Expecting prompting alone to provide current or private knowledge.

## Related concepts

- [Model Usage and Generation](../../)
- [System Prompts](../system-prompts/)
- [Few-Shot Prompting](../few-shot-prompting/)
- [Structured Output](../structured-output/)
