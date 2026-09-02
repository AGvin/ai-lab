# Graph or DAG Workflow Architecture

Legacy residual retained for graph/DAG-specific workflow pedagogy, executable-state/recovery guidance, and exact legacy framework evidence because the selected learning owner is not yet materialized on the active branch.

> **Migration note:** Generic workflow/orchestration semantics, deterministic control around model decisions, explicit state/transitions, retry/failure/authorization/validation boundaries, human interruption, persistence/resume, and bounded loops are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/`. The readiness design selects `learning/areas/agents-and-automation/workflows-and-orchestration/graph-and-dag-workflows/` for deeper pedagogy, but that node is currently absent on the active AI Lab ref. Preserve the graph-specific material below until that exact owner is materialized and verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Graph/DAG distinction residual

A graph workflow represents explicit executable state, bounded nodes, and directed transitions. A DAG forbids cycles; a general directed graph can include revision/recovery loops, but each loop needs explicit exit, budget, and repeated-state handling.

The executable graph/state schema — not a diagram alone — should define the workflow version, node identities, edge predicates, joins, terminal states, and recovery behavior.

## Node and state-design residual

Graph nodes should be bounded enough that inputs, outputs/state patches, evidence, permissions, side effects, failure, and acceptance can be understood independently. Avoid cosmetic graph boundaries where every node has unrestricted context and responsibility.

Keep structured workflow state separate enough to distinguish authoritative requirements, immutable input/artifact references, derived observations/model claims, node/attempt status, budgets/deadlines, pending approvals, accepted decisions, and unresolved uncertainty. Attribute state updates to the producing node/version when audit or recovery depends on that lineage.

## Branch/join residual

Before fan-out, define branch independence or isolation, shared read/write sets, artifacts/completion criteria, cancellation behavior, and the join rule (`all`, `any`, quorum, first acceptable, bounded subset, or another explicit policy).

A join should reconcile evidence and contradictions rather than merely concatenate branch outputs. Define ownership for late/duplicate results and merge conflicts.

## Loop, side-effect, and recovery residual

For every cycle, define what changed enough to justify another iteration, attempt/time/cost limits, repeated-state or oscillation detection, and escalation/terminal behavior. Do not encode an unbounded `while not good` loop.

Classify consequential nodes according to their effect semantics (read-only/pure, idempotent, compensatable, irreversible) and checkpoint/reconcile accordingly. After timeout/restart, verify authoritative external state before retrying a write; a transport failure does not prove the effect did not occur.

On resume, load compatible graph/state versions, reconcile active jobs/resources/external effects, fence stale controllers, revalidate approvals/deadlines, and invalidate downstream work whose authoritative prerequisites changed. Do not silently execute newer node logic against incompatible persisted state.

## Pattern-fit residual

Graph/DAG orchestration is useful when dependencies, branches/joins, pause/resume, human approval, asynchronous work, resource lifecycle, or long-running recovery must be explicit. Prefer a simple deterministic operation or short linear pipeline when branching/recovery/state machinery adds no material value.

## Legacy evidence-provenance residual

The legacy source cited:

- [LangGraph overview](https://langchain-ai.github.io/langgraph/concepts/low_level/)
- [LangGraph persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- [AutoGen GraphFlow](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/graph-flow.html)
- [AutoGen termination conditions](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/termination.html)

Preserve these exact framework references until the selected graph/DAG learning owner is materialized and their current/historical evidence disposition is verified.

These graph-specific pedagogical and evidence fragments remain migration source material until their exact learning owner is ready.
