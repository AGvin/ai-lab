# Documentation Requirements

## Requirements

- Teach a human approval gate as a control that pauses **before** a declared consequential transition and persists a deterministic pending-action record. Approval authorizes the exact reviewed action under the exact reviewed state; it is not blanket permission for the model, workflow, or future actions.
- Where material, define the pending-action record with approval/workflow/task/state version; exact action and normalized arguments; target system/account/environment/resource identifiers; user-visible effect and reversibility; evidence/validation results; privacy/rights/consent class; expected cost/duration/resource lifetime; known risks/uncertainty/alternatives; requester/executor identity; required approver role and separation-of-duty rules; creation/expiry/deadline; allowed decisions/modification schema; and post-approval verification/rollback or compensation plan.
- Bind approval deterministically to action type, normalized arguments, target identifiers, artifact revision/checksum, authoritative state version, cost/quantity bounds, execution deadline, and approver authority. Any material change after review invalidates the approval and requires revalidation/reapproval.
- Do not expose private hidden chain-of-thought as reviewer context. Surface the material facts, evidence, assumptions, source content/diff, consequences, and uncertainty needed for accountable authorization.
- Teach explicit decision states rather than interpreting arbitrary free-form text as broad permission: Approve, Reject, Modify, Defer, Escalate, Expire, and Cancel. Define the semantics of each state and make timeout/default/conflicting-approver behavior explicit.
- Treat Modify as a constrained change path: after material modification, rerun validation and normally require a new approval bound to the changed action/state.
- Before pausing, persist workflow/pending-action state, prevent duplicate execution, release unnecessary resources, deliberately retain or expire required leases, establish notification/escalation, and define expiry/fail-closed behavior.
- On resume, authenticate the approver and verify authority; load the exact approval/workflow record; revalidate authoritative state, inputs, artifacts, permissions, costs, and deadlines; fence stale controllers/duplicate execution; rerun deterministic checks; execute using stable operation identity/idempotency where possible; verify the external effect; and record actual effect, cost, and residual risk.
- Make clear that approval acknowledgement does not prove the external action completed. After timeout/lost acknowledgement/ambiguous write outcome, reconcile authoritative external state before requesting another approval or retrying the consequential operation.
- Teach separation of duty as risk- and policy-dependent rather than universal. High-risk policies may require approver independence from proposal generation, evaluated-system control, target-resource ownership, bypass incentives, or final verification; two-person approval and threshold/specialist rules are governance decisions.
- A second model is not a human approver when policy requires accountable human authorization.
- Apply least privilege to approval/execution: authorize only the minimum operation, target/environment, amount, duration, and scope; use short expiry; keep reusable credentials out of model context; prevent approval from minting broader authority; enforce authorization independently from model prompts.
- Design the approval interface so the reviewer can inspect the material action, destination/recipient, content or diff, approval reason, cost/irreversibility, source evidence/validation, alternatives/rollback, uncertainty, and exact decision options. Avoid hidden recipients, collapsed material changes, ambiguous/default-approve controls, or summaries that prevent source inspection.
- Reserve human attention for material decisions. Reduce low-value approval volume without silently widening autonomous authority; explicitly account for fatigue/rubber-stamping risk.
- Define failure behavior for unavailable approvers, expired approval, state change while paused, notification failure, insufficient authority, conflicting approvers, execution timeout after approval, side-effect success with lost acknowledgement, unavailable rollback, or unavailable approval/audit storage. Consequential actions should normally fail closed while authorization state is unresolved.
- Teach approval-gate fit for consequential tool calls, publishing/release, provisioning/teardown, deployment/merge, high-value financial actions, consent/identity-sensitive operations, exceptional escalation, and similar transitions requiring accountable human authority.
- Prefer deterministic policy without a human gate for harmless/easily reversible actions when a reviewer adds no meaningful information or authority. A gate placed after an irreversible effect, or used instead of validation/security/least privilege, is not meaningful control.
- Evaluate approval/rejection/modification/escalation/expiry/cancellation rates, state-change invalidations, decision latency, unauthorized/bypass attempts, stale/duplicate execution, post-approval validation/adverse outcomes, rollback/compensation success, approver workload/disagreement/fatigue, and cost per safely completed action.
- Use OpenAI Agents SDK and LangGraph references as framework examples/evidence only. Keep mutable framework APIs source-backed; approval semantics are not defined by one framework implementation.
- Link generic workflow pause/resume, human authority/oversight, authorization, idempotency/recovery, and governance semantics to their canonical concept/AI-engineering/trustworthy owners rather than duplicating them here.

## Validation

- Approval is always bound to a specific action/state scope and is invalidated by material drift.
- Free-form reviewer text is never interpreted as unlimited authorization.
- Resume examples revalidate current authoritative state before execution.
- Ambiguous external effects are reconciled before retry or reapproval.
- High-risk examples enforce approval independently of model prompts and preserve least privilege.
- Framework examples do not become timeless API facts.
