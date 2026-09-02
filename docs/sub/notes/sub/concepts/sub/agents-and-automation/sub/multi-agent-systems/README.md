# Multi-Agent Systems

Legacy residual retained for migration-time pattern navigation, practical architecture-selection guidance, production-control guidance, and research-candidate provenance that are intentionally outside the canonical Multi-Agent Systems concept owner.

> **Migration note:** MAS identity, the distinction from multiple model calls/ensembles, cooperation-versus-competition, topology/coordination dimensions, correlations between agents, role/authority/state/termination/side-effect boundaries, complete-system evaluation, and the distinction between MAS and workflow/coordination patterns are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/multiagent-systems/`. Selected workflow and coordination concepts retain their own canonical owners. The remaining material below stays here until the linked legacy pattern pages and the practical learning/decision/research fragments have exact dispositions.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Legacy pattern navigation

The following legacy pattern sources remain separate migration inputs and must be dispositioned against their selected workflow, coordination, system-design, oversight, learning, or project owners rather than being promoted automatically as MAS children:

### Coordination and delegation

- [Orchestrator-Worker Architecture](./sub/orchestrator-worker/)
- [Hierarchical Orchestration](./sub/hierarchical-orchestration/)
- [Supervisor-Specialist Architecture](./sub/supervisor-specialist/)
- [Router-Specialist Architecture](./sub/router-specialist/)
- [Handoff or Swarm Architecture](./sub/handoff-swarm/)
- [Multi-Agent Group Chat](./sub/group-chat/)

### Workflow control

- [Graph or DAG Workflow Architecture](./sub/graph-dag-workflow/)
- [Planner-Executor Architecture](./sub/planner-executor/)
- [Pipeline Architecture](./sub/pipeline/)
- [Map-Reduce Agent Architecture](./sub/map-reduce/)
- [Evaluator-Optimizer Architecture](./sub/evaluator-optimizer/)

### Shared state and distributed execution

- [Blackboard Architecture](./sub/blackboard/)
- [Event-Driven Agent Architecture](./sub/event-driven/)
- [Resource Lifecycle Controller Architecture](./sub/resource-lifecycle-controller/)

### Review and authority

- [Advisory Council, Jury, and Review Board Architecture](./sub/advisory-council-review-board/)
- [Human Approval Gate Architecture](./sub/human-approval-gates/)

## Pattern-selection residual

Use the simplest control structure that satisfies the workload and risk boundary. Multiple named agents do not by themselves establish specialization, independence, safety, or higher quality.

Practical selection questions include whether the work actually requires:

- dynamic delegation with one retained owner;
- bounded dispatch among predefined specialists;
- transfer of active ownership between participants;
- shared conversational or blackboard-style coordination;
- explicit dependency/branch/loop/checkpoint state;
- a separately inspectable planning stage;
- fixed artifact-processing stages;
- homogeneous fan-out/fan-in aggregation;
- bounded evaluator-driven revision;
- asynchronous event handling;
- authoritative resource-lifecycle control;
- multiple independent review perspectives; or
- explicit human authority before consequential actions.

Patterns can be composed, but every additional controller, reviewer, model call, event, shared state object, or transition should justify its latency, cost, permissions, coordination burden, and failure modes against a simpler baseline.

## Production-control residual

A production design should make the following operational contracts explicit where relevant:

- authoritative goal, requirements, and acceptance criteria;
- participant roles, authority, tools, permissions, and data boundaries;
- state schema, artifact ownership, and evidence provenance;
- dependency, routing, handoff, speaking, event, and merge rules;
- retry, revision, escalation, and fallback budgets;
- loop, cycle, timeout, and terminal conditions;
- mutable-resource and side-effect coordination;
- resource residency/lifecycle and cleanup;
- deterministic validation and appropriately independent review;
- human approval for declared high-risk actions; and
- inspectable externally observable decisions/state without relying on private hidden chain-of-thought.

Evaluate coordination overhead and system-level failure modes, not only the quality of individual agents. Shared models, evidence, prompts, or state can create correlated errors; conversational agreement is not independent verification.

## Research-candidate residual

[Integrated Agent Organization and Resource Portfolio](./sub/integrated-agent-organization-and-resource-portfolio/) remains a repository-origin research candidate with an initial bounded literature review, no implementation or validation, and no novelty claim. It must not be promoted into canonical concept truth or recommended as an established architecture until its research/provenance disposition is separately resolved.

These selection, operational, navigation, and research/provenance fragments remain migration source material until their exact learning, decision, system-design, project, or research owners are verified.
