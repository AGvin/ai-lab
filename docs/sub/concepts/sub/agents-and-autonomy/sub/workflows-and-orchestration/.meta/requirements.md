# Documentation Requirements

## Requirements

- Use the reader-facing title `Workflows and Orchestration`.
- Define a workflow as an explicit composition of processing steps, decisions, transitions, and control boundaries used to move a task from inputs toward outputs; define orchestration as the coordination of those components, dependencies, execution paths, participants, resources, and state transitions.
- Explain that AI-enabled workflows can place models/agents inside otherwise deterministic or explicitly coded control structures for classification, generation, routing, extraction, planning, delegation, review, evaluation, or other bounded decisions.
- For this documentation, distinguish workflows whose principal control paths are explicitly orchestrated from agents that dynamically direct more of their own process/tool selection, while acknowledging hybrids and avoiding a claim that the industry uses one universal boundary.
- Keep `manager-worker-orchestration/`, `evaluator-optimizer/`, and `agent-routing/` as the selected reusable child patterns whose agent-specific semantics justify independent concept nodes.
- Define `manager-worker-orchestration/` as the centralized-control family where a manager/supervisor/orchestrator retains overall task ownership and global responsibility while delegating bounded work and integrating returned results. Treat `orchestrator-worker/`, `supervisor-specialist/`, and hierarchical supervisor variants as legacy/source variants of this family unless a later architecture decision proves a distinct reusable child.
- Define `evaluator-optimizer/` as a bounded candidate-generation/revision and evaluation-feedback loop with explicit criteria, issue/evidence transfer, stop conditions, and escalation. Keep the workflow architecture distinct from generic verification/reflection, evaluation methods, evaluator model identity, and concrete evaluation results.
- Define `agent-routing/` as a bounded classification/dispatch decision that selects one or more declared specialist agents/routes according to an explicit routing policy. Distinguish it from ongoing manager/supervisor control and from handoffs where active ownership transfers between agents.
- Distinguish agent routing from `ai-engineering/architectures-and-patterns/model-routing/`. Agent routing selects specialist agent/workflow participants; model routing selects model/provider/backend execution routes. A system can use both layers independently or together.
- Preserve sequential, parallel, fan-out/fan-in, pipeline, graph/DAG, event-driven, MapReduce, loop, approval-gated, and other control-flow forms as parent-level workflow patterns rather than automatically creating AI-native leaves. Models or agents occupying stages/nodes/handlers do not by themselves make a generic software/distributed-systems pattern a distinct agent concept.
- Explain fixed pipeline semantics: predefined stages and artifact contracts are appropriate when the process is stable; model stages do not require autonomous-agent ownership, and stage validation/retry/side-effect policy can remain deterministic.
- Explain graph/DAG semantics: nodes/edges/state can encode branches, joins, loops, retries, approvals, and terminal states; a DAG forbids cycles while a general graph can include bounded loops. Graph representation is a workflow-control form rather than a separate multi-agent identity by itself.
- Explain event-driven semantics: typed events/queues/brokers can trigger decoupled handlers or agents asynchronously; delivery, ordering, idempotency, replay, backpressure, terminal workflow state, and durable authoritative state remain engineering concerns rather than emergent model behavior.
- Explain MapReduce/fan-out-fan-in semantics: partition independent work under a bounded map contract and combine normalized results through declared reduction/join logic; generic partitioning/aggregation remains a workflow pattern even when map/reduce stages are model- or agent-powered.
- Treat `planner-executor` as a split pattern rather than a selected workflow child. Generic plan representation, task decomposition, dependencies, and replanning belong to `reasoning-and-decision-making/planning-and-scheduling/`; execution-state, gating, orchestration, and recovery semantics belong here. Do not duplicate planning identity merely because a workflow separates planner and executor roles.
- Treat human approval gates as a composition of workflow control plus `human-ai-interaction/oversight-and-intervention/` and concrete project/policy rules. The workflow owns the pause/transition/resume placement; accountable human authority and intervention semantics remain with oversight, and step-by-step approval design belongs to learning/project owners.
- Treat resource lifecycle control as primarily AI-engineering system-design/reliability work. A workflow may invoke resource allocation, readiness, teardown, reconciliation, and billing-closure stages without making resource lifecycle a dedicated agent-orchestration child.
- Distinguish manager-worker orchestration from handoffs. A manager remains the active/global owner and receives delegated results; a handoff transfers task/conversation/control ownership to another participant and belongs to `coordination-and-communication/handoffs/`.
- Distinguish orchestration from multi-agent system identity. A workflow can contain one agent, many agents, deterministic services, tools, humans, or combinations; `multiagent-systems/` owns system-level multi-agent composition and topology rather than every control-flow pattern.
- Distinguish orchestration logic from model reasoning. A workflow engine or application can own sequencing, retries, branching, approvals, budgets, resource transitions, and recovery even when models provide decisions within particular stages.
- Keep workflow state, transition conditions, side effects, retries, idempotency, authorization, validation, deadlines, cancellation, and human approvals explicit where material; do not treat model-generated text as authoritative execution state by default.
- Require bounded loops to define why another iteration is justified, maximum attempts/time/cost, repeated-state or oscillation detection, escalation, and terminal outcomes. `while not good: retry` is not a complete control contract.
- Require branches/joins to define readiness, input snapshots/shared-state rules, branch outputs, cancellation/partial failure, join condition, merge/conflict owner, and treatment of late/duplicate results when these matter.
- Explain persistence/checkpoint/resume for long-running workflows where state, external jobs, approvals, or side effects survive one model call/process. Resume must reconcile authoritative state rather than simply continue a stale conversational narrative.
- Avoid claiming structured workflows are automatically reliable, auditable, cheaper, faster, or safer than more model-directed agents; those outcomes depend on design, task, controls, observability, and evaluation.
- Keep concrete orchestration frameworks, provider APIs, project DAGs/graphs, event schemas, retry policies, broker configurations, specialist registries, prompts, concrete routes, benchmark/evidence results, and task-specific workflow recipes with their applicable catalog, engineering, evidence, learning, or project owners.
- Render direct-child navigation from the validated materialized selected child set when reader-facing rendering is activated.
- Use the canonical entity references as research inputs for the explicit-orchestration versus model-directed-control boundary and for manager, router, and evaluator workflow distinctions.

## Validation

- The page does not equate every multi-step model application with an autonomous agent or every workflow with a multi-agent system.
- Manager-worker, evaluator-optimizer, and agent-routing remain distinct selected patterns with explicit control/ownership boundaries.
- Agent routing is not conflated with model/provider routing, a stateful supervisor, or an ownership-transferring handoff.
- Pipeline, graph/DAG, event-driven, MapReduce, sequential/parallel, approval-gated, and planner-executor source material is preserved without creating redundant AI-native leaves.
- Planning/decomposition, human oversight, and resource/system lifecycle retain their selected owners where their primary semantics lie outside workflow control.
- Workflow and orchestration are distinguished from model reasoning and intrinsic model architecture.
- Deterministic control-flow ownership is not hidden inside conversational context as the universal design.
- No specific orchestration framework or flow pattern is required by definition.
- Concrete implementations, routes, graphs, prompts, registries, and measured results remain outside the reusable concept owner.
- Direct-child navigation contains only currently materialized selected descendants.
