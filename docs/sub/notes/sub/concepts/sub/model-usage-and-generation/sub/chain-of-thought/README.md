# Chain of Thought

Legacy residual retained for decomposition, external verification, audit-artifact, and sensitive-trace handling guidance that are intentionally outside the canonical Chain of Thought concept owner.

> **Migration note:** Chain-of-thought identity, trace-versus-prompting distinction, model/task-dependent performance effects, non-faithfulness and post-hoc limitations, visible-versus-hidden computation boundaries, and separation from externally verifiable workflow artifacts are already preserved in `docs/sub/concepts/sub/models/sub/behavior-and-failure-modes/sub/reasoning/sub/chain-of-thought/`. The remaining material below stays here until its exact learning, evaluation, agent-workflow, privacy, or audit owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Decomposition and verification residual

For difficult multi-step work, prefer decomposition that produces independently checkable subproblems or intermediate results when that improves correctness or diagnosis. Ask for material assumptions, calculations, evidence, and a final conclusion when those artifacts are useful to verify the result.

Use deterministic or externally verifiable tools for arithmetic, code execution, retrieval, validation, or other operations where a tool result provides stronger evidence than additional free-form reasoning text.

## Audit-artifact residual

When auditability matters, preserve structured plans, state transitions, tool calls/results, retrieved evidence, calculations, approvals, or other externally inspectable workflow artifacts rather than treating a verbose rationale as proof of what internally caused the answer.

A detailed reasoning-like narrative can still contain speculation or errors. Material intermediate claims should therefore be checked under the same evidence standard as the final conclusion.

## Sensitive-trace and efficiency residual

Avoid requiring unrestricted visible reasoning merely for completeness. Long traces consume context and can expose sensitive prompt, policy, source, or intermediate information. For production workflows, concise explanations plus verifiable calculations, evidence, structured state, or tool traces may provide a better audit surface than unrestricted reasoning prose.

These decomposition, audit, privacy, and verification practices remain migration source material until their exact learning, evaluation, workflow, privacy, or audit owners are verified.
