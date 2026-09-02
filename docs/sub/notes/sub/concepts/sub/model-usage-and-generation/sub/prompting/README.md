# Prompting

Legacy residual retained for procedural prompt-writing, task decomposition, uncertainty handling, and prompt-evaluation guidance that are intentionally outside the canonical Prompting concept owner.

> **Migration note:** Prompting identity, inference-time conditioning, distinction from training/adaptation, supported input-form variability, instruction-versus-source-content boundaries, prompt-pattern scope, capability/security limitations, and model/task/context/version dependence are already preserved in `docs/sub/concepts/sub/models/sub/interaction/sub/prompting/`. The remaining material below stays here until its exact learning, trustworthy-AI, workflow, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Prompt-writing residual

Useful prompt-writing practices include:

- state the goal and the most important acceptance criteria directly;
- provide only task-relevant context and distinguish source material from instructions;
- define the required output contract when format, language, schema, length, or audience matters;
- use examples when a desired pattern is easier to demonstrate than describe;
- request explicit uncertainty or evidence boundaries when the available information is incomplete;
- avoid redundant or mutually conflicting rules that make the effective instruction set harder to maintain.

These are procedural techniques rather than universal Prompting semantics and should be evaluated for the concrete model and task.

## Decomposition and workflow residual

For complex work, split the task into verifiable stages or use an agent/workflow structure when staged execution improves correctness, observability, or recovery. Prompting alone does not replace missing tools, state management, external validation, or workflow control.

## Evaluation and maintenance residual

Treat important prompts as configuration that requires representative evaluation. Test against a stable set of realistic cases before relying on a prompt in production, and repeat relevant regression checks after material model, provider, context-construction, or prompt changes.

These procedural and evaluation practices remain migration source material until their exact learning, evaluation, workflow, or decision-support owners are verified.
