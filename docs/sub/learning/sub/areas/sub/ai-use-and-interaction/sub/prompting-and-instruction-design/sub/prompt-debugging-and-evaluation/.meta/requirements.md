# Documentation Requirements

## Requirements

- Teach Prompt Debugging and Evaluation as systematic iteration on behavior-affecting prompt configuration rather than ad-hoc wording changes judged from one example.
- Define representative cases and explicit acceptance criteria before relying on a prompt in production or another consequential workflow.
- Include ordinary, edge, invalid, ambiguous, and failure cases when they are material to the intended behavior.
- Compare simpler baselines when useful and change one material prompt/example/context variable at a time when isolation helps diagnose cause.
- Record recurring failure signatures and distinguish prompt-design limits from missing model capability, tools, state, retrieval, authorization, or workflow control.
- Re-run relevant regression checks after material model, provider, prompt, example-set, tool-contract, or context-construction changes.
- Escalate to Workflow Design, model selection/evaluation, or engineering controls when prompt changes alone cannot satisfy the acceptance contract reliably.

## Validation

- A single successful example is not treated as sufficient prompt validation.
- Material behavior changes trigger representative regression checks.
- Prompt iteration does not hide a capability or system-design gap behind unlimited rewrites.
