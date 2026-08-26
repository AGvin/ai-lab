# Documentation Requirements

## Requirements

- Use the reader-facing title `Manager-Worker Orchestration` and introduce `orchestrator-worker` and `supervisor-specialist` as common variants/aliases whose exact implementation style can differ.
- Define the pattern by its control invariant: one manager/supervisor/orchestrator remains the overall task owner, decides when and how to delegate bounded work to specialists/workers, receives their results, integrates/validates them, and remains responsible for the terminal response or action.
- Keep the concept broader than one framework's `agents as tools`, subagent API, supervisor helper, or worker graph. Concrete APIs, tool wrappers, agent registries, prompts, model choices, graph nodes, and runtime implementations remain with their platform/catalog/project owners.
- Distinguish manager-worker orchestration from `agent-routing/`. A router performs a bounded classification/dispatch decision; a manager can repeatedly delegate, revise assignments, integrate several results, maintain global state, and decide terminal completion across the workflow.
- Distinguish manager-worker orchestration from `coordination-and-communication/handoffs/`. In manager-worker orchestration the manager retains authoritative/global ownership while a worker returns a bounded result; in a handoff the receiving agent becomes the active owner for the transferred task/conversation state.
- Distinguish manager-worker orchestration from a fixed pipeline or DAG. A manager can dynamically decide decomposition, specialist choice, ordering, parallelism, retries, or follow-up based on intermediate results; a fixed explicit workflow can implement equivalent behavior without requiring a model-directed manager.
- Distinguish manager-worker orchestration from generic multi-agent-system identity. Multiple agents can coordinate through peer communication, handoffs, shared state, markets, voting, or other structures without any central manager.
- Treat hierarchical orchestration as a composable manager-worker topology rather than a separate selected leaf. Managers can supervise workers or subordinate managers at several levels when scope/context/authority requires it, but additional hierarchy does not change the central retain-and-delegate invariant.
- Preserve the narrower supervisor-specialist variant: a stateful user-facing supervisor can retain conversation/global state and invoke focused specialists as tools, often with isolated context and bounded outputs. This remains a manager-worker specialization rather than a separate canonical concept.
- Preserve the broader orchestrator-worker variant: the manager can dynamically decompose an open-ended project into heterogeneous subtasks, create a work plan/graph, execute independent workers in parallel or sequence, collect artifacts, and synthesize the final result.
- Define the manager contract where material: authoritative objective/state, allowed worker/specialist registry, delegation policy, context/data boundary, tools/permissions, budgets/deadlines, retry/escalation policy, merge/contradiction rules, acceptance/terminal criteria, and human approval boundaries.
- Define worker contracts where material: supported task class, bounded input/output schema, required evidence/context, model/tools/permissions/data class, side-effect policy, timeout/retry/abstention behavior, artifact/provenance requirements, and explicit unsupported/failure states.
- Require capability validation rather than role-name trust. A manager must not infer tools, permissions, expertise, data access, or reliability from a specialist label alone; declared capabilities and measured behavior belong to concrete registry/evidence owners.
- Minimize delegated context according to the task while preserving required constraints. Do not copy the full conversation, secrets, unrelated tenant data, or unrestricted tool authority to every worker by default; record when broad shared context is actually required.
- Preserve authoritative-versus-derived state boundaries. The manager should distinguish user requirements, system policy, retrieved evidence, prior worker claims, proposed interpretations, accepted artifacts, and unresolved uncertainty rather than treating all accumulated text as equally authoritative.
- Treat worker results as untrusted decision inputs until validated according to consequence. A manager should not blindly forward specialist output or allow a worker result to create new permissions/routes/actions outside declared policy.
- Define parallel worker execution only for independent work whose mutable state/side effects do not conflict or whose isolation/merge policy is explicit. Track late, failed, duplicate, or partially completed workers and define cancellation/merge ownership.
- Define result integration explicitly: preserve evidence/artifact references, reconcile contradictions, separate facts/inferences/recommendations/unknowns, validate deterministic claims where practical, and surface unresolved disagreement rather than inventing consensus.
- Keep the manager accountable for terminal criteria. Worker completion does not imply global task completion; the manager must evaluate dependencies, artifacts, validations, approvals, budgets, and unresolved issues before accepting the workflow.
- Bound repeated delegation and recovery. Define maximum calls/attempts, repeated-failure detection, alternate specialist/model routes, escalation/human review, deadline/cost ceilings, and fail-closed behavior where required. Calling the same unsuitable specialist repeatedly is not recovery.
- Treat a model-directed manager as a probabilistic controller, not an authorization boundary. Validate generated worker names, tool arguments, resource requests, external actions, and permissions against deterministic policy/registries before execution.
- Explain centralized-control trade-offs: simplified ownership, context/permission isolation, unified synthesis, and auditability can come with manager bottlenecks, single-control failure domains, routing/synthesis errors, context growth, extra model calls, and correlated model failures.
- Evaluate the complete orchestration, not only individual workers. Useful measures include delegation precision, unnecessary/missing/repeated calls, worker task success, integration/contradiction errors, context leakage/omission, latency/concurrency, cost, escalation, terminal acceptance, and cost per accepted result.
- Keep concrete specialist registries, prompts, models, tools, permissions, framework configuration, workflow instances, evaluation runs, traces, and project-specific organization charts with their applicable catalog/evidence/project owners.
- Use the canonical entity references as research inputs for the shared manager-retains-control invariant while preserving differences among orchestrator-worker, agents-as-tools, subagent/supervisor, and hierarchical implementations.

## Validation

- The manager retains overall task/control ownership; otherwise the pattern may be routing, handoff, or another coordination form.
- Orchestrator-worker, supervisor-specialist, and hierarchical variants are preserved without creating duplicate canonical leaves.
- A worker result is not treated as authoritative merely because a specialist produced it.
- Worker names do not grant undeclared capability, tools, permissions, or trust.
- Manager-directed delegation is not confused with fixed pipelines/DAGs or generic multi-agent-system identity.
- Parallel workers have explicit independence/isolation and merge/failure semantics.
- Concrete framework APIs, specialist registries, prompts, models, and run results remain outside the reusable concept owner.
