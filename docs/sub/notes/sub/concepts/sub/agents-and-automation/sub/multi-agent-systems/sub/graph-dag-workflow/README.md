# Graph or DAG Workflow Architecture

A graph workflow represents an agent system as explicit state, executable nodes, and directed transitions with branches, joins, retries, loops, and terminal states.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established agent workflow pattern.

## Core idea

Each node performs a bounded operation. Edges determine which node may run next from inspectable state and declared conditions.

```text
input -> classify -> plan -> fan-out workers -> join -> verify -> approve | revise | stop
```

A directed acyclic graph (DAG) prohibits cycles. A general directed graph may include correction, recovery, or continuation loops, but every loop requires a bounded exit condition.

The graph owns control flow. Models may propose state updates or route recommendations, but deterministic workflow code should enforce permissions, dependency readiness, retry budgets, and terminal conditions where practical.

## Graph contract

Record:

```text
Graph ID and version:
Input schema:
State schema and state owner:
Nodes and node versions:
Edges and activation predicates:
Join semantics:
Loop and retry limits:
Side-effect policy:
Checkpoint and resume policy:
Failure and compensation paths:
Human approval points:
Terminal states and acceptance rules:
```

A diagram alone is insufficient. The executable graph and persisted state schema are the authoritative workflow definition.

## Node contract

Every node should define:

- stable node identifier and implementation version;
- purpose and acceptance criteria;
- required input state and produced state patch;
- model, tool, runtime, permissions, and data boundary;
- side effects and idempotency behavior;
- timeout, retry, escalation, and fallback;
- deterministic validators;
- checkpoint and artifact requirements;
- terminal success, failure, cancellation, and abstention states.

Avoid nodes with unrestricted responsibilities such as “solve everything.” A node should be small enough that its inputs, outputs, evidence, and failure can be understood independently.

## State model

Use typed structured state rather than an unbounded conversation transcript as the workflow database.

Separate:

- authoritative user requirements;
- immutable input references;
- derived observations and model claims;
- node status and attempt history;
- artifacts and checksums;
- budgets, deadlines, and resource leases;
- pending approvals;
- accepted decisions and remaining uncertainty.

State updates should be versioned and attributable to the node that produced them. Preserve rejected or superseded values when auditability matters.

## Edge and routing semantics

Edges may be:

- unconditional sequence;
- deterministic condition;
- model-assisted route validated against an allowed target set;
- success, failure, timeout, cancellation, or abstention path;
- fan-out to several independent nodes;
- join that waits for all, any, quorum, priority, or an explicit subset;
- retry or revision loop;
- escalation to a stronger model, specialist, or human.

A model-generated route should not create arbitrary node names, permissions, or destinations. Validate the decision against the graph and current state.

## Branches and joins

Before fan-out, define:

- whether branches operate on immutable snapshots or isolated workspaces;
- shared read and write sets;
- expected artifacts and completion criteria;
- cancellation behavior if one branch fails;
- join activation: all, any, quorum, first acceptable, or budget-bound selection;
- merge and conflict-resolution owner;
- treatment of late or duplicate branch results.

A join should not merely concatenate outputs. It should reconcile evidence, detect contradictions, enforce the output schema, and preserve minority or unresolved findings where relevant.

## Loops, retries, and termination

Every cycle should identify:

- the issue or state change that justifies another iteration;
- maximum attempts, elapsed time, and cost;
- minimum improvement or changed evidence;
- repeated-state and oscillation detection;
- escalation or accepted-limitation path;
- terminal failure or human-approval path.

Do not model an unlimited `while not good: retry` loop. Hash or version the material state so identical or alternating states can be detected.

## Side effects and idempotency

Classify nodes as:

- pure or read-only;
- idempotent write;
- compensatable write;
- irreversible or externally consequential action.

Checkpoint before consequential side effects. Use stable operation IDs, compare-and-set state, leases, and provider idempotency keys where available.

After timeout or controller restart, reconcile whether the side effect occurred before retrying. A transport error does not prove that an external operation failed.

Irreversible actions should normally require a [Human Approval Gate](../human-approval-gates/) or another explicit authority boundary.

## Persistence and recovery

Persist state at meaningful boundaries:

- graph start;
- before and after side effects;
- after every durable artifact;
- before human interruption;
- before resource teardown;
- after terminal disposition.

On resume:

1. load the exact graph and state versions;
2. reconcile active jobs, resources, and external side effects;
3. fence stale controllers;
4. validate pending approvals and deadlines;
5. resume only nodes whose prerequisites remain valid;
6. invalidate downstream work when an authoritative input changed.

A resumed graph must not silently run newer node logic against older state unless migration is explicit and tested.

## Suitable uses

- repository or document workflows with dependencies and parallel branches;
- research, evidence collection, synthesis, and verification;
- coding pipelines with plan, implementation, test, review, and approval;
- multimodal processing with separate preparation, perception, generation, and evaluation stages;
- asynchronous hosted jobs and on-demand resources;
- workflows requiring pause, resume, cancellation, or human approval;
- long-running processes where state must survive model or controller failure.

## Poor fits

Avoid or simplify this pattern when:

- the task is one deterministic operation;
- a short linear sequence has no meaningful branching or recovery;
- the state cannot be defined well enough to make transitions safe;
- orchestration overhead exceeds the value of explicit control;
- all nodes share the same unrestricted context and permissions, making graph boundaries cosmetic.

## Strengths

- makes dependencies, branches, joins, and terminal states explicit;
- supports deterministic control around probabilistic models;
- enables checkpointing, replay, recovery, and audit;
- permits parallelism without losing coordination;
- localizes retries, permissions, costs, and failures;
- supports human and resource lifecycle nodes.

## Limitations

- requires schema, state migration, and workflow-version discipline;
- graph complexity can become difficult to understand;
- model-driven routing can still be unstable or manipulated;
- side effects and external callbacks require reconciliation;
- excessive node granularity increases latency and maintenance;
- a well-structured graph cannot compensate for weak node capability or invalid acceptance criteria.

## Evaluation metrics

Record:

- terminal success, failure, cancellation, and timeout rates;
- node and edge activation accuracy;
- invalid transition attempts;
- branch parallelism and join wait time;
- duplicate work and side-effect incidents;
- retries, cycles, repeated states, and escalations;
- checkpoint, resume, and recovery success;
- state migration defects;
- resource leaks and orphaned jobs;
- total latency, cost, and cost per accepted result;
- human interventions and unresolved uncertainty.

## Evidence and established usage

LangGraph documents agents as graph-based workflows with state, nodes, and edges, including persistence and human interruption. AutoGen GraphFlow documents directed execution with sequential flows, parallel fan-out, conditional branching, joins, and loops with explicit termination conditions.

Sources:

- [LangGraph overview](https://langchain-ai.github.io/langgraph/concepts/low_level/)
- [LangGraph persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- [AutoGen GraphFlow](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/graph-flow.html)
- [AutoGen termination conditions](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/termination.html)

## Related concepts

- [Multi-Agent Systems](../..)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Evaluator-Optimizer Architecture](../evaluator-optimizer/)
- [Human Approval Gates](../human-approval-gates/)
- [Agent State](../../../agent-state/)
- [Task Decomposition](../../../task-decomposition/)
