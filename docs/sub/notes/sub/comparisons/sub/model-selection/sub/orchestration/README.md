# Choosing Models for Agent Orchestration

Select the model or model hierarchy that decomposes work, assigns agents and tools, controls execution order, manages resources, evaluates quality, and decides when a workflow is complete.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Implemented guidance verified on 2026-07-25. Concrete orchestrator assignments still require repeatable portfolio-level evaluation under the exact tools, permissions, models, workload, and resource constraints.

## Terminology

A **generalist model** has useful capability across several domains. It describes breadth, not system authority.

An **orchestrator** or **manager agent** owns workflow coordination. It may use a generalist, a reasoning specialist, or a hierarchy of manager models. The best worker is not automatically the best orchestrator.

## Orchestrator contract

Evaluate whether the orchestrator can:

- translate a goal into deliverables and acceptance criteria;
- decompose work into bounded tasks;
- identify dependencies, shared state, and conflict risks;
- select models, agents, tools, permissions, quality tiers, and retry policies;
- decide which tasks may run concurrently and which must remain sequential;
- monitor progress, failures, cost, and resource state;
- validate worker reports against observable evidence;
- request targeted correction without discarding valid work;
- escalate or stop when retries, cost, or quality limits are reached;
- preserve concise state, evidence, decisions, and unresolved risks;
- verify that external and billable resources actually stopped.

The orchestrator is a control function, not merely a router.

## Execution graph

### Parallel work

Use parallel execution only when tasks are independent or safely isolated. Before launch, record:

- inputs and dependencies;
- files, records, services, and resources each task may modify;
- collision and ordering risks;
- branch, workspace, namespace, or output isolation;
- merge, consolidation, and conflict-resolution ownership.

### Sequential work

Use sequential execution when one result feeds another, tasks modify the same state, or later decisions require validated earlier output.

### Graph workflow

Represent substantial work as a directed graph with explicit nodes, dependencies, branches, joins, conditions, bounded loops, retries, checkpoints, and terminal states. Launch a node only when dependencies, permissions, and resources are ready.

Avoid false parallelism that creates merge conflicts, inconsistent assumptions, duplicate work, or repeated cost.

## Model and agent assignment

For every candidate, record:

- demonstrated quality for the exact role and task class;
- modalities, tools, language, context, and structured-output requirements;
- omission, premature-completion, and tool-failure risk;
- expected retries and independent-review requirements;
- residency, startup latency, throughput, and concurrency;
- privacy, provider, license, policy, and permission constraints;
- total cost per accepted result.

Use a cheaper or smaller route when it reliably meets the requested tier. Reserve stronger or specialist models for declared capability gaps, repeated failure, high-risk work, or final review.

## Quality and stopping

Use the shared quality tiers:

1. **Exploration** — feasibility and alternatives.
2. **Concept draft** — coherent intermediate result for discussion.
3. **Working result** — functionally acceptable with known limitations.
4. **Production quality** — verified, maintainable, documented, and ready for use.
5. **Exceptional quality** — additional depth or polish justified by value.

Define the tier before assignment. Stop when:

- every required criterion passes;
- accepted limitations are documented;
- the retry or review budget is exhausted;
- revisions no longer improve measured quality;
- the requirement is impossible or contradictory;
- human judgment has higher expected value than another model round.

## Reliability and retry control

Attach a [Reliability Profile](../reliability-profiles/) to each exact worker assignment. Include common failures, useful retry count, escalation route, quality ceiling, unsuitable tasks, and degraded-operation behavior.

Retry only failures likely to improve under the same assignment. Use issue identifiers, revision comparison, repeated-criticism detection, and cycle detection. Repeating the same prompt to the same unsuitable model is not a recovery strategy.

The worker must not be the sole authority on its own completion. Prefer deterministic verification; use independent model or human review when judgment is required.

## Resource lifecycle

Classify each component as:

- always running and resident;
- reachable but lazy-loaded;
- retained for a bounded idle timeout;
- launched temporarily for one task;
- remote hosted service;
- mutually exclusive with another local service because of memory constraints.

For every on-demand resource:

1. confirm need, authorization, data eligibility, and budget;
2. select the exact service, model, hardware, storage, and timeout;
3. start with idempotency and ownership records;
4. verify provider state and endpoint readiness;
5. execute bounded work and persist artifacts outside ephemeral storage;
6. verify results before release;
7. request shutdown, termination, or scale-to-zero;
8. independently confirm provider and billing state;
9. retry cleanup or escalate when teardown fails.

A successful start request is not readiness, and a worker completion report is not proof that a billable resource stopped.

Use [Resource Lifecycle Orchestration](./sub/resource-lifecycle/) for leases, fencing, readiness proof, artifact persistence, teardown, billing reconciliation, cleanup recovery, metrics, and fault injection.

## Hierarchical orchestration

Use hierarchy when it reduces context overload, separates policies, or enables meaningful parallel work:

- top-level orchestrator owns global scope, budget, dependencies, and acceptance;
- department or domain manager owns a coherent workstream;
- team lead coordinates a smaller specialist unit;
- worker executes a bounded task and reports evidence upward.

Every managed unit needs an explicit scope, authority, budget, quality target, escalation path, and reporting contract. Do not add management layers when a simple graph is clearer.

## Councils and review boards

Several independent models may advise or review a proposal:

- **advisor or council** — non-binding options, risks, or specialist analysis;
- **review board** — acceptance, rejection, or correction authority;
- **jury or vote** — structured comparison under an explicit rule;
- **human gate** — final authorization for consequential work.

Preserve concise proposals, evidence, disagreements, decision, requested corrections, responsible authority, and residual uncertainty. Do not expose or depend on private hidden chain-of-thought.

Bound review rounds. Escalate when repeated revisions do not improve the result. Permit acceptance with known limitations only when the selected tier and authorized decision-maker allow it.

## Conflict and failure handling

The orchestrator must distinguish:

- correctable execution defect;
- unsuitable worker or model;
- missing input or unavailable dependency;
- conflicting concurrent changes;
- impossible or contradictory requirement;
- reviewer preference outside the approved scope;
- resource, network, provider, or budget failure.

Use immutable inputs, versioned artifacts, idempotent actions, checkpoints, leases, fencing, rollback where possible, and explicit terminal states. Do not hide partial failure behind a narrative success message.

## Evaluation suite

Evaluate complete workflows requiring:

- decomposition and dependency-graph construction;
- conflict-aware parallelization;
- role and tool assignment under cost and hardware constraints;
- recovery when a worker or service fails;
- selective escalation rather than universal flagship use;
- resource startup, readiness, persistence, teardown, and billing verification;
- state retention across retries and model changes;
- correct quality-tier and stopping decisions;
- concise auditable decision records;
- termination without unnecessary loops.

Report portfolio completion, criterion coverage, dependency and conflict errors, assignment accuracy, unnecessary expensive calls, retries, repeated feedback cycles, resource leaks, peak RAM and VRAM, total API and infrastructure cost, wall-clock time, human interventions, and final quality tier.

## Decision record

```text
Workflow, scope, acceptance criteria, quality tier, and risk:
Graph, dependencies, parallelism, shared state, and isolation:
Models, agents, tools, permissions, roles, and evidence:
Residency, readiness, lifecycle, budget, and concurrency:
Retry, review, escalation, fallback, and stopping rules:
Completion, quality, latency, cost, resource, and failure outcomes:
Known limitations, responsible authority, verified date, and triggers:
```

## Related pages

- [AI Model Selection and Team Design](../..)
- [Agent Models](../agents/)
- [Agent Role Selection](../agent-role-selection/)
- [Combined Workloads](../combined-workloads/)
- [Reliability Profiles](../reliability-profiles/)
- [Resource Lifecycle Orchestration](./sub/resource-lifecycle/)
- [Multi-Agent Systems](../../../../../concepts/sub/agents-and-automation/sub/multi-agent-systems/)
- [Agent Orchestration Tools](../../../../../../../software/sub/agent-orchestration/)
- [General repository disclaimer](../../../../../../../disclaimer/)
