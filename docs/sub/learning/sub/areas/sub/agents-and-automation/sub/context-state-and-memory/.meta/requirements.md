# Documentation Requirements

## Requirements

- Present Context, State, and Memory as the Agents and Automation learning group for the information an agent can use now, explicit execution/task/workflow state, and short-/long-term memory/persistence strategies.
- Keep the canonical `concepts/agents-and-autonomy/state-and-memory/` owner for reusable state-versus-memory semantics; this group teaches practical agent implementation/operation consequences and progressive depth.
- Distinguish working context, explicit agent state, short-term memory, long-term memory, memory strategies, and persistence rather than treating conversation history or a large context window as one universal memory mechanism.
- Explain that the current materialized subset focuses on `agent-state/` because the legacy Agent State source has source-backed schema/transition/artifact/recovery pedagogy ready for migration.
- Do not imply that unmaterialized selected siblings `working-context/`, `short-term-memory/`, `long-term-memory/`, `memory-strategies/`, or `persistence/` are absent from the logical architecture; standard navigation reflects only physical children.
- Treat authoritative workflow/execution state separately from model-visible context. State can be persisted and validated even when only a selected projection is supplied to a model.
- Keep generic database/distributed-system consistency, privacy/retention law, reliability/idempotency, and concrete storage/product behavior with their applicable Engineering/Trustworthy AI/Catalog/Project owners while teaching their agent-specific implications here.

## Validation

- State, context, memory, and persistence remain distinct learning concepts.
- Conversation/model context is never treated as the sole authoritative workflow state when durable execution semantics matter.
- Current navigation exposes only materialized selected children.
- Generic infrastructure/storage/privacy mechanisms are linked rather than duplicated as agent-only truth.
