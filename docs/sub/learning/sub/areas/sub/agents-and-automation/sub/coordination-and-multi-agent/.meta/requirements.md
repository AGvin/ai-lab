# Documentation Requirements

## Requirements

- Present Coordination and Multi-Agent as the learning group for how multiple agents/participants share or transfer ownership, context, structured state, roles, and decisions while collaborating on one broader objective.
- Distinguish coordination from orchestration: `workflows-and-orchestration/` owns control-flow patterns and workflow execution structure, while this group owns interaction/ownership/communication structures among multiple participants.
- Teach the currently materialized children as distinct coordination mechanisms: `handoffs/` for transfer of active ownership/context, `group-chat/` for shared conversational coordination and speaker/turn policies, and `blackboard/` for shared structured problem-state coordination.
- Do not imply that unmaterialized selected siblings such as `multi-agent-architectures/`, `topologies-and-roles/`, or `collaboration-and-consensus/` are absent from the logical architecture; standard navigation reflects only physical children.
- Compare coordination mechanisms using explicit ownership, context sharing/minimization, authority/permissions, concurrency/order, conflict handling, termination, side-effect ownership, traceability, latency/cost, and failure/recovery implications rather than by framework branding.
- Keep reusable handoff/group-chat/blackboard semantics with their canonical concept owners; learning pages teach practical selection, configuration, operational consequences, examples, and evaluation.
- Keep concrete framework APIs, mutable implementation behavior, current compatibility, and dated evidence source-backed in entity metadata/evidence owners rather than freezing them as timeless learning facts.
- Prefer the simplest coordination form that satisfies the task. Do not introduce multi-agent interaction when one agent, deterministic operation, or simpler workflow already meets the requirement.

## Validation

- Handoffs, group chat, and blackboard are not treated as synonyms or interchangeable topologies.
- Coordination ownership/context/authority boundaries are explicit in examples.
- Current navigation exposes only materialized selected children.
- Framework-specific behavior is clearly separated from reusable coordination teaching.
- The group does not duplicate workflow-control semantics owned by `workflows-and-orchestration/`.
