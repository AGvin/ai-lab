# Multi-Agent Systems

A multi-agent system coordinates several agents that may specialize, collaborate, compete, delegate, hand off, review, or approve one another's work.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Multiple agents are useful when tasks have genuinely different roles, tools, permissions, evidence, or parallel workstreams. Examples include a research agent gathering evidence, an implementation agent producing changes, and a reviewer checking the result. The agents still require explicit control flow, shared-state rules, termination, conflict resolution, and evidence boundaries.

Use the simplest pattern that meets the workload. Several named agents do not automatically create specialization, independence, safety, or better quality.

## Implemented architecture patterns

### Coordination and delegation

- [Orchestrator-Worker Architecture](./sub/orchestrator-worker/) — a central coordinator decomposes, delegates, tracks, verifies, and synthesizes bounded worker tasks.
- [Hierarchical Orchestration](./sub/hierarchical-orchestration/) — managers coordinate nested departments, teams, or workstreams under explicit authority and reporting contracts.
- [Supervisor-Specialist Architecture](./sub/supervisor-specialist/) — one stateful supervisor retains ownership and invokes bounded specialist agents as tools.
- [Router-Specialist Architecture](./sub/router-specialist/) — a bounded router classifies an input and dispatches it to predefined specialist routes.
- [Handoff or Swarm Architecture](./sub/handoff-swarm/) — the active agent transfers ownership to another approved specialist through a structured handoff.
- [Multi-Agent Group Chat](./sub/group-chat/) — several agents participate in a shared conversation under a speaker-selection and termination policy.

### Workflow control

- [Graph or DAG Workflow Architecture](./sub/graph-dag-workflow/) — explicit state, nodes, edges, branches, joins, loops, checkpoints, and terminal conditions govern execution.
- [Planner-Executor Architecture](./sub/planner-executor/) — a planner creates and revises an inspectable plan while executors perform bounded ready tasks.
- [Pipeline Architecture](./sub/pipeline/) — predefined stages transform validated artifacts through a fixed sequence.
- [Map-Reduce Agent Architecture](./sub/map-reduce/) — homogeneous partitioned map tasks emit structured records that are grouped and reduced into a verified result.
- [Evaluator-Optimizer Architecture](./sub/evaluator-optimizer/) — an optimizer revises an artifact from structured evaluator findings under a bounded correction loop.

### Shared state and distributed execution

- [Blackboard Architecture](./sub/blackboard/) — knowledge sources contribute evidence and hypotheses to a structured shared problem state under controller policy.
- [Event-Driven Agent Architecture](./sub/event-driven/) — typed events trigger asynchronous handlers with explicit delivery, ordering, idempotency, and terminal semantics.
- [Resource Lifecycle Controller Architecture](./sub/resource-lifecycle-controller/) — a deterministic control-plane role owns provisioning, readiness, leases, residency, teardown, and billing closure.

### Review and authority

- [Advisory Council, Jury, and Review Board Architecture](./sub/advisory-council-review-board/) — distinct reviewers provide structured findings, optional bounded deliberation, and a declared aggregation or decision process.
- [Human Approval Gate Architecture](./sub/human-approval-gates/) — a workflow pauses before a consequential transition and requires exact-scope authorization from an accountable person.

## Research candidates

- [Integrated Agent Organization and Resource Portfolio](./sub/integrated-agent-organization-and-resource-portfolio/) — repository-origin synthesis with an initial bounded literature review, no implementation or validation, and no novelty claim. It remains a research candidate for the exact integration of organization, model portfolio, quality control, resource lifecycle, and verified closure.

Research candidates are not implemented architecture patterns and should not be recommended as established designs without separately declared evidence.

## Practical use

- Parallelize independent document or repository analysis.
- Separate planning, execution, generation, review, and approval.
- Assign domain-specific tools, permissions, prompts, or models to specialized roles.
- Route work according to modality, risk, quality tier, and resource availability.
- Preserve workflow state across asynchronous jobs, interruptions, or failures.
- Share structured problem state without copying a complete conversation to every specialist.
- Simulate alternative proposals and retain disagreements before a decision.
- Place human authority before declared irreversible or high-risk actions.

## Pattern selection

Prefer:

- a **single agent or deterministic workflow** when one bounded process is sufficient;
- **orchestrator-worker** when one coordinator should dynamically decompose and retain global project ownership;
- **hierarchical orchestration** when several coherent units require local management and cross-unit coordination;
- **supervisor-specialist** when one stateful user-facing agent should repeatedly call isolated specialists;
- **router-specialist** when one bounded classification or policy decision can dispatch the task;
- **handoff or swarm** when direct specialist ownership should move between agents;
- **group chat** when shared discussion is central and turn selection is controlled;
- **graph or DAG** when dependencies, branching, persistence, retries, and side effects require explicit execution state;
- **planner-executor** when a dynamic versioned plan should be inspected and revised separately from task execution;
- **pipeline** when fixed stages and artifact contracts fully describe the process;
- **map-reduce** when a complete workload can be partitioned into contract-compatible independent units and aggregated through a declared reducer;
- **evaluator-optimizer** when clear criteria support measurable iterative correction;
- **blackboard** when specialists should contribute opportunistically to a structured shared problem state;
- **event-driven** when asynchronous decoupled handlers and external callbacks are central;
- a **resource lifecycle controller** when model or infrastructure residency, cost, and teardown require authoritative control-plane state;
- an **advisory council or review board** when several distinct review perspectives materially improve a decision;
- a **human approval gate** when accountable authority must remain human before a consequential action.

Patterns may be composed, but every additional controller, reviewer, event, shared object, or transition must justify its latency, cost, permissions, and failure modes.

## Required controls

A production design should define:

- authoritative goal, requirements, and acceptance criteria;
- roles, authority, tools, permissions, and data boundaries;
- state schema, artifact ownership, and evidence provenance;
- dependency, routing, handoff, speaking, event, and merge rules;
- retry, revision, escalation, and fallback budgets;
- loop, cycle, and terminal conditions;
- resource residency and lifecycle;
- deterministic validation and independent review;
- human approval for declared high-risk actions;
- inspectable decisions without private hidden chain-of-thought.

## Trade-offs and limitations

Multi-agent systems multiply model calls, coordination overhead, state, and failure modes. Agents can reinforce one another's errors because they share similar models, evidence, or context. More agents do not automatically produce independent evidence.

A complex architecture may reduce quality when:

- responsibilities overlap or ownership is ambiguous;
- state is copied through summaries rather than preserved authoritatively;
- agents modify shared resources without isolation;
- review loops are unbounded;
- routing is less reliable than the workers;
- agreement is mistaken for verification;
- events or contributions are duplicated, stale, or unordered;
- infrastructure remains active after model work completes.

## Common mistakes

- Using multiple agents for a task that can be a simple deterministic operation or loop.
- Giving every agent the same role, model, evidence, and information.
- Allowing agents to modify shared state without coordination or idempotency.
- Treating agent agreement, debate, or majority vote as proof of correctness.
- Omitting termination, cycle detection, or human escalation.
- Letting a worker approve its own high-risk output.
- Relying on model-generated prose as the authoritative workflow or resource state.
- Hiding orchestration, review, latency, infrastructure, and retry cost from evaluation.

## Related concepts and guidance

- [Agents and Automation](../../)
- [Task Decomposition](../task-decomposition/)
- [Agent State](../agent-state/)
- [Verification and Reflection](../verification-and-reflection/)
- [Agents and Automation Model Selection](../../../../../../../../catalog/sub/models/sub/selection/sub/agents-and-automation/)
- [Model Role Portfolios](../../../../../../../../catalog/sub/models/sub/selection/sub/model-teams/sub/role-based-portfolios/)
- [Model Teams](../../../../../../../../catalog/sub/models/sub/selection/sub/model-teams/)
