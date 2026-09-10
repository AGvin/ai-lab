# Documentation Requirements

## Requirements

- Teach a graph workflow as explicit executable state plus bounded nodes and directed transitions. Distinguish a DAG, which forbids cycles, from a general directed graph that can include revision/recovery loops.
- Make clear that a workflow diagram alone is not the executable contract. The runnable graph/state schema should define workflow/schema version, stable node identities, edge predicates, joins, terminal states, persistence/checkpoint behavior, and recovery semantics.
- Teach node design around bounded contracts: inputs, outputs/state patches, evidence/artifact references, permissions, side effects, failure behavior, acceptance criteria, and resource/time/cost assumptions should be understandable without giving every node unrestricted context/responsibility.
- Separate authoritative workflow state from immutable input/artifact references, derived observations/model claims, node/attempt status, budgets/deadlines, pending approvals, accepted decisions, and unresolved uncertainty. Attribute state updates to producer node/version when audit or recovery depends on lineage.
- Before fan-out, require explicit branch independence/isolation, shared read/write sets, artifacts/completion criteria, cancellation behavior, and a join policy such as all, any, quorum, first acceptable, or bounded subset.
- Teach joins as reconciliation points rather than string concatenation: reconcile evidence/conflicts, define ownership of late/duplicate results, and handle merge conflicts against authoritative state.
- For every cycle, require an explicit reason to iterate, evidence of changed state, attempt/time/cost limits, repeated-state or oscillation detection, and escalation/terminal behavior. Do not teach unbounded `while not good` loops as a valid orchestration strategy.
- Classify consequential nodes by side-effect semantics such as read-only/pure, idempotent, compensatable, or irreversible, and choose checkpoint/retry/reconciliation behavior accordingly.
- After timeout, crash, or restart, teach reconciliation against authoritative external state before retrying a consequential write; transport failure is not evidence that the side effect did not occur.
- On resume, validate graph and persisted-state version compatibility, reconcile active jobs/resources/external effects, fence stale controllers where relevant, revalidate approvals/deadlines, and invalidate downstream work whose authoritative prerequisites changed.
- Teach graph/DAG orchestration when explicit dependency, branch/join behavior, pause/resume, human approval, asynchronous work, resource lifecycle, long-running recovery, or inspectable state transitions materially justify it.
- Prefer a simpler deterministic operation or short linear pipeline when graph state/branch/recovery machinery adds no material value.
- Use LangGraph and AutoGen only as framework examples/evidence. Keep framework-specific APIs and mutable implementation behavior source-backed; do not redefine graph/DAG semantics from one framework's current API.
- Link generic workflow/state/retry/authorization/reliability semantics to their canonical concept/AI-engineering owners rather than duplicating them as graph-specific theory.

## Validation

- A DAG is never described as allowing cycles.
- A visual graph is never treated as sufficient evidence of executable state/recovery semantics.
- Every example with loops or consequential side effects includes explicit stopping/reconciliation behavior.
- Branch joins define an actual merge/acceptance policy rather than merely combining text.
- Framework examples do not become timeless protocol/API facts.
