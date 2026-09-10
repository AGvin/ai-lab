# Documentation Requirements

## Requirements

- Teach runtime human intervention as live operator control of an executing agent/workflow when automated authority, confidence, recovery, or policy is insufficient: pause, inspect, correct, constrain, redirect, take over, resume, cancel, or escalate under explicit state/authority rules.
- Distinguish live intervention from planned human review/approval. `ai-use-and-interaction/workflow-design/human-review-and-approval/` teaches practitioner-facing review placement; `workflows-and-orchestration/human-approval-gates/` teaches deterministic consequential-action gate contracts; this node owns intervention during active execution.
- Define intervention triggers where material: repeated failures or non-improvement, policy/permission conflicts, anomalous cost/resource growth, ambiguous external effects, low-confidence/unsupported decisions, stale/contradictory state, unexpected tool/system behavior, reviewer/operator request, or explicit runtime escalation.
- Persist enough authoritative runtime state before pausing/takeover to resume or terminate safely: current workflow/task state/version, in-flight actions, observed external effects, artifacts/evidence, leases/resources, approvals, deadlines/budgets, unresolved uncertainty, and the reason for intervention.
- Show the operator the material evidence needed to intervene: current objective/constraints, actual state/tool results, pending or ambiguous side effects, relevant artifacts/diffs, failures/retries, resource/cost exposure, uncertainty, and available actions. Do not rely only on a model-generated narrative.
- Do not expose private hidden chain-of-thought as operator evidence. Provide inspectable state, claims, evidence, assumptions, events, validations, and outcomes instead.
- Keep operator actions explicit and bounded: pause, cancel, retry eligible action, modify a plan/task/input, choose a fallback, grant/deny a declared approval, change resource envelope within policy, transfer ownership, request more evidence, or terminate safely. Free-form text must not become unlimited authority implicitly.
- Authenticate the operator and verify authority for the requested intervention. Taking over execution does not automatically grant access to every tool, secret, tenant, environment, or resource.
- After an operator changes material plan/input/state/permissions/resources, revalidate dependent work and fence/cancel stale automated actions before resume. Late results from the pre-intervention state must not overwrite newer authoritative state.
- Reconcile ambiguous external effects before retrying or undoing consequential operations. An operator request to "try again" does not prove the prior operation failed.
- Define resume criteria explicitly: corrected/validated state, updated plan/version, required approvals, eligible resources/permissions, consistent authoritative external state, and bounded next actions. Resume should not simply continue the old conversational narrative.
- Define cancellation/termination cleanup: handle in-flight work, durable artifacts, leases/resources, external effects, notifications, audit evidence, and retained state according to the applicable owners rather than abandoning operational responsibilities when a human stops the agent.
- Use escalation when the available operator lacks required expertise/authority or the situation exceeds the approved automated/manual recovery policy. Preserve why escalation happened and what remains unresolved.
- Account for operator availability and overload. Critical workflows need explicit behavior for unavailable humans, notification failure, response deadlines, queues/priority, and fail-closed/degraded outcomes rather than assuming a person will always respond.
- Evaluate intervention frequency/reasons, detection-to-intervention and intervention-to-safe-state latency, stale-action prevention, operator correction success, resume/recovery success, bypass/authority failures, repeated escalation, human workload, downstream adverse outcomes, and cost per safely completed result.
- Keep generic oversight taxonomy, human factors, and governance with Human-AI Interaction/Trustworthy AI; keep idempotency/recovery, resource lifecycle, and concrete incident/runbook policy with their selected engineering/project owners.

## Validation

- Runtime intervention is distinguished from preplanned review/approval and from generic human oversight terminology.
- Operator decisions use inspectable authoritative runtime state rather than only model summaries or hidden reasoning.
- Material operator changes invalidate/revalidate dependent automated work and fence stale actions.
- Ambiguous external effects are reconciled before retry/undo.
- Operator authority remains least-privilege and unavailable-human behavior is explicit where material.
- Resume and cancellation include state/resource/effect responsibilities rather than conversational continuation alone.
