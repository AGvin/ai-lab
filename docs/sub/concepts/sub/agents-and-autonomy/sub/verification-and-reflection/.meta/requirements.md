# Documentation Requirements

## Requirements

- Use the reader-facing title `Verification and Reflection`.
- Define verification as checking a claim, artifact, state transition, or action result against explicit evidence, constraints, acceptance criteria, or authoritative observations; define reflection as model- or agent-driven review of prior reasoning, actions, assumptions, feedback, or outcomes to propose corrections or future changes.
- Keep verification and reflection related but non-equivalent. Reflection can generate hypotheses, critiques, or revisions, but model self-review is not independent proof that the original or revised result is correct.
- Prefer direct or deterministic verification when the target property can be established by tests, schemas, parsers, calculations, tool/environment state, source evidence, permissions, checksums, or other authoritative observations; use model judgment only for properties that genuinely require semantic judgment and scope its evidence accordingly.
- Explain that external feedback can make reflection more informative, but the reliability of reflection still depends on the feedback source, model, task, prompts/context, and correction procedure.
- Acknowledge that self-refinement/self-correction can improve some tasks while intrinsic self-correction without new evidence can fail or degrade results; do not present repeated reflection as a monotonic quality-improvement guarantee.
- Distinguish verification from regeneration. Producing another answer, asking the same model to agree, or using several highly correlated model outputs does not automatically create independent evidence.
- Distinguish verification/reflection from hidden chain-of-thought disclosure. Systems can verify externally observable artifacts, tool results, state transitions, sources, and acceptance conditions without requiring private internal reasoning traces.
- Explain that failed verification should feed explicit error/evidence state into the workflow or agent, while recovery, retries, escalation, and human approval remain separate control mechanisms with their own owners.
- Keep concrete test suites, evaluator models, model-as-judge methods, benchmark results, review prompts, retry loops, CI pipelines, and task-specific acceptance policies with their applicable evaluation, engineering, learning, or project owners.
- Use the canonical entity references as research inputs for self-refinement benefits and intrinsic self-correction limitations when reader-facing rendering is activated.

## Validation

- Reflection/self-critique is not presented as equivalent to independent verification.
- A second model response or majority agreement is not treated as proof without an evidence/independence contract.
- Verification does not require exposing hidden chain-of-thought.
- Self-correction is not claimed to monotonically improve correctness across models/tasks.
- Deterministic or authoritative checks remain preferred when they directly establish the required property.
- Legacy operational examples are preserved as verification-boundary semantics rather than universal workflow recipes.
