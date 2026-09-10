# Documentation Requirements

## Requirements

- Teach manager-worker orchestration around one invariant: a manager retains ownership of the user/global objective and terminal result while delegating bounded work to workers or subordinate managers under explicit contracts.
- Distinguish three useful variants without treating them as unrelated patterns: a stable supervisor-specialist form, a broader dynamic orchestrator-worker form, and hierarchical manager-worker orchestration with multiple management levels.
- Use the supervisor-specialist form when one stateful user-facing supervisor should repeatedly invoke a relatively stable set of focused specialists as bounded tools while retaining conversation/global state, user intent, and final synthesis responsibility.
- Teach that specialists may often remain stateless between calls, but durable specialist state can be introduced deliberately when the workload requires it. State ownership must remain explicit rather than emerging accidentally from repeated calls.
- Use the broader orchestrator-worker form when the coordinating owner must dynamically decompose an open-ended objective into heterogeneous subtasks, select workers/tools/models, manage dependencies/artifacts, run independent work in parallel where safe, and synthesize a validated terminal result.
- Explain that the orchestrator does not need to be the strongest model for every worker task, but it must reliably preserve requirements, dependency state, acceptance criteria, worker capability boundaries, and terminal responsibility. Weak decomposition or synthesis can waste otherwise capable workers.
- Teach hierarchical orchestration as a composable extension of the same retained-ownership invariant: a manager may delegate bounded scopes to subordinate managers that own their local workers while the top-level manager retains global objective, cross-scope dependencies, budget, and final acceptance.
- Introduce another management level only for a concrete reason such as reducing context overload, isolating materially different policies/tools/permissions/infrastructure, creating meaningful parallel ownership of large work areas, or allowing local decisions while preserving explicit global dependency/acceptance control.
- Do not add hierarchy merely because many agents exist. Prefer one manager-worker loop or an explicit workflow graph when it remains easier to inspect, test, operate, and attribute responsibility.
- Teach manager/worker contracts with bounded task purpose, authoritative inputs, required artifacts/evidence, acceptance criteria, permissions/tools, budgets/timeouts, allowed side effects, retry/escalation behavior, and return/terminal-state semantics.
- Minimize worker context to what the bounded task requires. Context isolation can reduce cost and leakage risk but creates omission risk, so managers must pass authoritative constraints/evidence deliberately rather than either broadcasting all state or over-minimizing blindly.
- Keep worker permissions and side-effect authority bounded independently from prompts. Delegation of a task does not automatically delegate all manager credentials or decision authority.
- Make dependency and parallelism rules explicit. Parallelize only genuinely independent work or work with a defined merge/conflict contract; preserve artifact identity/version and prevent two workers/managers from silently owning the same mutable state.
- Require the manager to validate and integrate worker results rather than treating worker completion as terminal success. Preserve source evidence and unresolved uncertainty needed for final acceptance.
- Define bounded retry, replacement, fallback, escalation, and partial-failure behavior. Repeated worker failure may require a different worker/model/tool, plan change, human review, or terminal failure rather than identical retries.
- Prefer a one-step router when bounded dispatch is the only required decision; use handoff when active ownership genuinely transfers; use graph/pipeline/workflow control when the sequence/dependencies are known and deterministic control is clearer than model-directed decomposition.
- In hierarchical forms, make cross-team resource/dependency ownership, read/write boundaries, handoff artifacts, version/snapshot rules, merge/conflict responsibility, and escalation paths explicit instead of relying on managerial summaries alone.
- Teach hierarchy trade-offs: each added layer consumes latency/cost, can hide evidence in summaries, propagate errors upward, duplicate/abandon work when scopes overlap, and obscure accountability when local optimization conflicts with the global objective.
- Evaluate the complete system, including decomposition quality, worker selection/utilization, context omission/leakage, parallelism/duplication/conflicts, worker failure/retry/escalation, evidence loss during synthesis, manager bottlenecks, hierarchy overhead, terminal acceptance, latency/cost/resource use, and cost per accepted result.
- Use the exact Anthropic, LangChain/LangGraph, and AutoGen references preserved in entity metadata as framework/evidence examples only. Stable manager-worker semantics are canonical in the concept owner; mutable framework APIs and historical URLs must remain source-backed.

## Validation

- The manager always retains explicit terminal ownership unless the workflow intentionally switches to a handoff pattern.
- Supervisor-specialist, orchestrator-worker, and hierarchical forms are taught as variants of one retained-ownership family.
- Added hierarchy requires an explicit benefit and is not justified only by agent count.
- Worker context/permissions are bounded without omitting authoritative task constraints.
- Parallel work has explicit dependency, artifact, and conflict ownership.
- Evaluation measures decomposition/integration and system outcomes, not worker quality in isolation.
