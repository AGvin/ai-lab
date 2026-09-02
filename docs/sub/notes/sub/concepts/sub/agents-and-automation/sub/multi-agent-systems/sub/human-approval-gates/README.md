# Human Approval Gate Architecture

Legacy residual retained for approval-gate-specific workflow pedagogy, authorization-state design, and exact legacy framework evidence because the selected learning owner is not yet materialized on the active branch.

> **Migration note:** Generic pause/transition/resume workflow semantics are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/`; human authority, oversight/intervention capacity, reviewer limitations, and HITL taxonomy boundaries are preserved in `docs/sub/concepts/sub/human-ai-interaction/sub/oversight-and-intervention/`. The readiness design selects `learning/areas/agents-and-automation/workflows-and-orchestration/human-approval-gates/` for deeper procedural teaching, but that node is currently absent on the active AI Lab ref. Preserve the approval-specific material below until that exact owner is materialized and verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Pending-action and approval-scope residual

A human approval gate should pause **before** a declared consequential transition and persist a deterministic pending-action record. Approval authorizes the exact reviewed action under the exact reviewed state; it is not blanket permission for the model, workflow, or future actions.

Where material, the pending record should identify:

- approval/workflow/task/state version;
- exact action, normalized arguments, target system/account/environment/resource IDs;
- user-visible effect, reversibility, evidence and validation results;
- privacy/rights/consent classification, expected cost/duration/resource lifetime;
- known risks, uncertainty, alternatives, requester/executor identity;
- required approver role and any separation-of-duty rule;
- creation/expiry/deadline, allowed decisions/modification schema;
- post-approval verification and rollback/compensation plan.

Bind approval deterministically to the action type, normalized arguments, target identifiers, artifact revision/checksum, authoritative state version, cost/quantity bounds, execution deadline, and approver authority. A material change after review invalidates the approval and requires revalidation/reapproval.

Do not expose private hidden chain-of-thought. Show the material facts, evidence, assumptions, diff/content, consequences, and uncertainty needed to make an accountable decision.

## Decision-state residual

Use explicit decision states rather than interpreting arbitrary free-form text as broad permission:

- **Approve** — authorize the exact pending action;
- **Reject** — prohibit execution;
- **Modify** — apply constrained changes, then revalidate and normally reapprove;
- **Defer** — retain the request until a bounded deadline without execution;
- **Escalate** — transfer to a more qualified/privileged authority;
- **Expire** — invalidate automatically when time/state constraints fail;
- **Cancel** — withdraw before execution.

The workflow should make timeout/default and conflicting-approver behavior explicit rather than silently continuing.

## Pause, resume, and ambiguous-effect residual

Before pausing, persist workflow/pending-action state, prevent duplicate execution, release unnecessary resources, deliberately retain/expire required leases, establish notification/escalation, and define expiry/fail-closed behavior.

On resume:

1. authenticate the approver and verify authority;
2. load the exact workflow/approval record;
3. revalidate authoritative state, inputs, artifacts, permissions, cost, and deadlines;
4. fence stale controllers/duplicate execution;
5. rerun required deterministic checks;
6. execute with a stable operation identity/idempotency contract where possible;
7. verify the external effect;
8. record actual effect, cost, and residual risk.

Approval acknowledgement does not prove the external action completed. After timeout or lost acknowledgement, reconcile authoritative external state before asking for another approval or retrying a consequential write.

## Separation-of-duty and least-privilege residual

For sufficiently high-risk actions, policy may require the approver to be independent from identities that generated the proposal, control the evaluated system, own the target resource, benefit from bypassing the gate, or perform final verification. Two-person approval, role/value/environment thresholds, specialist review, or other separation rules are project/governance decisions rather than universal requirements.

A second model is not a human approver when policy requires accountable human authorization.

Approval should grant only the minimum authority needed for the pending action: one operation, bounded target/environment/amount/duration/scope, short expiry, no reusable credentials in model context, and no ability to mint broader approvals. Enforcement belongs to the execution/authorization layer independently from model prompts.

## Approval-interface, fatigue, and failure residual

The approval interface should make the material action, destination/recipient, content or diff, approval reason, cost/irreversibility, source evidence/validation, alternatives/rollback, uncertainty, and exact decision options inspectable. Avoid hidden recipients, truncated/collapsed material changes, ambiguous buttons, default approval, or summaries that prevent source inspection.

Reserve human attention for material decisions. Excessive low-value prompts create fatigue and rubber-stamping; reducing prompt volume must not silently widen autonomous authority.

Define behavior when no approver is available, approval expires, workflow state changes while paused, notification fails, authority is insufficient, approvers conflict, execution times out after approval, a side effect succeeds but acknowledgement is lost, rollback is unavailable, or the approval/audit store is unavailable. Consequential actions should normally fail closed when authorization state is unresolved.

## Pattern-fit and evaluation residual

Approval gates fit consequential tool calls, publication/release, provisioning/teardown, deployment/merge, high-value financial actions, consent/identity-sensitive operations, exceptional escalation paths, and other transitions where accountable human authority must remain explicit.

Prefer deterministic policy without a human gate for harmless/easily reversible actions when the reviewer would add no meaningful information or authority. A gate placed after an irreversible effect, or one used as a substitute for validation/security/least privilege, is not meaningful control.

Evaluate approval/rejection/modification/escalation/expiry/cancellation rates, state-change invalidations, decision latency, unauthorized/bypass attempts, stale/duplicate execution incidents, post-approval validation/adverse outcomes, rollback/compensation success, approver workload/disagreement/fatigue, and cost per safely completed action.

## Legacy evidence-provenance residual

The legacy source cited:

- [OpenAI Agents SDK: Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [LangGraph interrupts](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/)
- [LangGraph persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)

Preserve these exact framework references until the selected human-approval-gates learning owner is materialized and their current/historical evidence disposition is verified.

These approval-specific pedagogical, operational, and evidence fragments remain migration source material until their exact learning owner is ready.
