# Agent State

Legacy residual retained for practical state-schema, transition-validation, artifact-reference, and recovery guidance that is intentionally outside the canonical State and Memory concept owner.

> **Migration note:** Agent-state identity, distinction from memory/model context/conversation history, authoritative-current-state semantics, resumability boundary, persistence-versus-recovery caveat, and consistency with external side effects are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/state-and-memory/`. The remaining material below stays here until its exact learning, workflow-engineering, reliability, privacy, or project owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## State-schema residual

A practical workflow state can record fields such as:

- task or execution identity and current stage;
- validated inputs and outputs;
- references to tool results or larger artifacts;
- completed, pending, and blocked actions;
- retry counters and error state;
- human approvals, rejections, or escalation state; and
- model, prompt, tool, schema, or configuration versions when they affect continuation or auditability.

These are implementation examples rather than one universal state schema.

## Transition and recovery residual

Prefer explicit typed or otherwise validated state transitions over treating free-form model prose as the workflow ledger. Keep large artifacts in their authoritative stores and place stable references/identifiers in state when repeated copying into model context would be wasteful or ambiguous.

Persisted state introduces schema evolution, privacy/retention, concurrent-update, and consistency concerns. Update state and external effects under an explicit consistency/reconciliation contract: a model or worker must not mark a consequential action complete merely because it proposed the action or lost the acknowledgement from the external system.

When several workers can modify related state or side effects, define ownership, conflict/locking/idempotency/reconciliation rules appropriate to the system rather than relying on conversational coordination.

These state-engineering and recovery practices remain migration source material until their exact learning, engineering, reliability, privacy, or project owners are verified.
