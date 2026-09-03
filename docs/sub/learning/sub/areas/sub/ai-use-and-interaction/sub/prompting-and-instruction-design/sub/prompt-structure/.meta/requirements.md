# Documentation Requirements

## Requirements

- Teach Prompt Structure as composing a prompt from the minimum task-relevant elements needed to make intent and acceptance conditions clear.
- Cover explicit goal, important constraints, relevant context, instruction-versus-source-content separation, required output contract, language/audience/length where material, and uncertainty/evidence expectations when information may be incomplete.
- For durable/system-level instructions, define purpose, permitted scope, stable behavioral constraints, tool-use expectations, consequential-action validation expectations, and durable output/communication conventions while keeping rapidly changing task data, retrieved content, and examples separate.
- Prefer direct, internally consistent instructions over duplicated or mutually conflicting rules that obscure effective priority.
- Do not store secrets in prompt text merely because an interface treats the prompt as privileged; model-facing instructions are not an authorization boundary.
- Use examples only when they communicate a desired pattern or boundary more effectively than prose; route detailed example design to `../examples-and-few-shot/`.
- Link staged or multi-step execution to Workflow Design when the task needs checkpoints, tools, state, external validation, or recovery beyond one prompt.
- Treat prompt structure as model/task/context dependent and reverify important behavior after model, provider-interface, hidden-context, tool-contract, or context-construction changes.

## Validation

- The page does not prescribe one universal prompt template.
- Source material is not silently treated as instructions.
- Output requirements are explicit when machine or human consumers depend on them.
- Prompt text is not represented as a substitute for application permissions or external enforcement.
