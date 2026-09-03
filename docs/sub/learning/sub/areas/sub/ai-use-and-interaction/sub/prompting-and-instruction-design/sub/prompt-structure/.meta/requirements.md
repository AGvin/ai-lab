# Documentation Requirements

## Requirements

- Teach Prompt Structure as composing a prompt from the minimum task-relevant elements needed to make intent and acceptance conditions clear.
- Cover explicit goal, important constraints, relevant context, instruction-versus-source-content separation, required output contract, language/audience/length where material, and uncertainty/evidence expectations when information may be incomplete.
- Prefer direct, internally consistent instructions over duplicated or mutually conflicting rules that obscure effective priority.
- Use examples only when they communicate a desired pattern or boundary more effectively than prose; route detailed example design to `../examples-and-few-shot/`.
- Link staged or multi-step execution to Workflow Design when the task needs checkpoints, tools, state, external validation, or recovery beyond one prompt.
- Treat prompt structure as model/task/context dependent and verify important behavior on representative cases.

## Validation

- The page does not prescribe one universal prompt template.
- Source material is not silently treated as instructions.
- Output requirements are explicit when machine or human consumers depend on them.
