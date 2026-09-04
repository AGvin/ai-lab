# Documentation Requirements

## Requirements

- Teach multi-agent architecture as the system-level arrangement of multiple bounded participants, their ownership/control relationships, communication/shared-state surfaces, evidence/authority boundaries, and terminal responsibility rather than as a synonym for any one workflow pattern.
- Use the canonical Multi-Agent Systems concept for reusable identity and system semantics. This learning node teaches architecture selection/composition, practical production consequences, and comparison against simpler single-agent/deterministic baselines.
- Start architecture selection from the workload and risk boundary rather than from a desired number of agents. Multiple named agents do not by themselves establish specialization, independence, safety, better quality, or useful parallelism.
- Prefer the simplest control structure that satisfies the requirement. Ask whether the work actually needs retained-owner delegation, bounded routing, ownership transfer, shared conversation or structured shared state, explicit graph/loop/checkpoint control, separate planning, fixed stages, homogeneous fan-out/fan-in, evaluator-driven revision, asynchronous events, dedicated resource-lifecycle control, independent review, or explicit human authorization before choosing/composing corresponding patterns.
- Treat patterns as composable but not free. Every additional controller, participant, model call, event, shared state object, transition, reviewer, or management layer should justify its latency, cost, permission surface, coordination state, observability burden, and new failure modes against a simpler architecture.
- Separate system topology from workflow control. A hierarchical, peer, swarm, or team arrangement can execute several workflow patterns; routing, handoff, graph/DAG, manager-worker, group-chat, blackboard, event-driven, evaluator-optimizer, approval, and similar patterns each retain their dedicated learning owners.
- Require explicit authoritative goal/requirements/acceptance ownership for non-trivial systems and identify which participant/controller owns terminal completion. Distributed contribution does not imply distributed final accountability.
- Define participant roles/capabilities, tools, permissions, data boundaries, state visibility, artifact/evidence ownership, and allowed side effects rather than assuming role names or separate prompts create meaningful specialization.
- Record coordination/control contracts where material: dependencies, routing/handoff/speaker/event/merge rules, shared-state ownership, retries/revisions/escalations/fallbacks, loop/cycle/time/cost limits, termination, validation/review, resource lifecycle, and human-authorization boundaries. Link the detailed mechanisms to their selected learning/operations owners.
- Distinguish independent evidence from merely multiple outputs. Shared model families, prompts, retrieved evidence, memory/state, tools, or conversation can correlate failures; conversational agreement or majority does not prove independent verification.
- Keep deterministic validation and authorization outside probabilistic agent agreement when the required property can be directly checked/enforced. Multi-agent structure is not a substitute for schemas, tests, permissions, idempotency, policy, or approval.
- Preserve externally inspectable state, artifacts, evidence, decisions, and transitions needed for debugging/audit without requiring exposure of private hidden chain-of-thought.
- Define failure ownership across participant loss, stale state, conflicting outputs, duplicated/abandoned work, unreachable specialists, partial results, context/evidence loss, resource leaks, and ambiguous side effects rather than assuming another agent will notice and repair them.
- Evaluate complete-system behavior: terminal accepted-result quality, useful specialization, coordination overhead, duplicate/omitted work, correlated-error exposure, state/evidence loss, invalid/unauthorized effects, retries/escalations/interventions, latency/cost/resource use, and recovery compared with simpler baselines.
- Link topology/role-allocation teaching to `topologies-and-roles/`, collaboration/debate/review to `collaboration-and-consensus/`, and concrete workflow/control patterns to their dedicated selected owners rather than duplicating their mechanics here.
- Treat repository-origin experimental/research architectures as research/provenance candidates until separately validated. Their existence in a legacy subtree does not make them an established architecture or recommendation.

## Validation

- Architecture selection begins from workload/control/risk needs rather than desired agent count or framework capabilities.
- Multi-agent architecture is distinguished from specific workflow patterns and from topology alone.
- Role names do not imply specialization, independence, permission, or authority without explicit contracts/evidence.
- Production contracts make terminal ownership, state/evidence, side effects, failure/recovery, and resource boundaries explicit where material.
- Complete-system evaluation includes coordination/correlation/cost/failure modes, not only individual agent output quality.
- Experimental repository-origin designs are not promoted to canonical truth without separate research validation.
