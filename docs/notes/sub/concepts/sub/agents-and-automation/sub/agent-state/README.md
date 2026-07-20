# Agent State

Agent state is the explicit data that records a workflow's current position, intermediate results, decisions, pending actions, and execution metadata.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

State should not exist only inside a model conversation. Explicit state makes an agent resumable, inspectable, testable, and safer to retry. It may be stored in memory for short tasks or persisted in a database, workflow engine, or event log for long-running work.

## Common state fields

- Task identifier and current stage.
- Inputs, validated outputs, and tool results.
- Completed and pending actions.
- Retry counters and error details.
- Human approvals or rejected actions.
- Model, prompt, and configuration versions.

## Practical use

Use typed state objects and validate every transition. Store references to large artifacts instead of repeatedly placing them in model context. Separate authoritative application state from model-generated notes or summaries.

## Trade-offs and limitations

Persisted state improves recovery and auditability but introduces schema evolution, privacy, retention, and concurrency concerns. State may become inconsistent if external side effects occur without corresponding updates.

## Common mistakes

- Using chat history as the only source of truth.
- Storing secrets or unnecessary personal data in state.
- Updating state before confirming an external action succeeded.
- Allowing several workers to modify the same task without coordination.

## Related concepts

- [Agents and Automation](../../)
- [Agent Memory](../agent-memory/)
- [Failure Recovery](../failure-recovery/)
- [Tracing](../../../evaluation-and-operations/sub/tracing/)
