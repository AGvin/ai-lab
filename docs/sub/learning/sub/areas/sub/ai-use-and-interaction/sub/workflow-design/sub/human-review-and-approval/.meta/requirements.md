# Documentation Requirements

## Requirements

- Teach human review and approval as practical workflow design for placing qualified human judgment where it can materially validate, correct, authorize, clarify, or stop AI-assisted work before a consequential or quality-critical transition.
- Use examples such as reviewing generated code or document changes before publication, resolving low-confidence/ambiguous classifications, checking source evidence and uncertainty, confirming recipients/amounts/permissions/scope, or approving a proposed plan before consequential execution.
- Do not imply every AI workflow requires human approval. Use human review when the reviewer adds evidence, judgment, authority, accountability, or risk control that simpler deterministic validation/automation cannot provide sufficiently.
- Place review/approval before the transition it is intended to control. Review after an irreversible effect can support audit/learning but cannot retroactively function as preventive authorization.
- Give the reviewer enough inspectable source evidence, proposed action/artifact or diff, expected effect, material uncertainty, relevant constraints/context, deterministic validation results, alternatives/rollback where relevant, and the exact decision being requested. A model-generated summary alone is not adequate reviewer context when source inspection matters.
- Do not expose private hidden model chain-of-thought as reviewer evidence. Surface claims, source/evidence pointers, assumptions, uncertainty, validations, artifacts, and consequences that can be independently inspected.
- Define decision states appropriate to the workflow, such as approve, reject, modify/correct, request more information, defer, escalate, timeout/expire, or cancel. The exact system-state binding for consequential agent actions belongs to Human Approval Gates.
- Persist the human decision and reviewed artifact/version/scope where later execution or audit depends on it; do not let later generation silently reinterpret an approval as broader permission.
- Keep deterministic validation for properties it can directly establish. Human review should not replace tests, schema checks, authorization, policy enforcement, exact arithmetic, or other machine-checkable controls merely because a reviewer is present.
- Match reviewer competence and authority to the decision. A person without enough evidence, time, expertise, permission, or intervention capability cannot provide meaningful oversight simply by clicking an approval control.
- Design requests to reduce fatigue/rubber-stamping: reserve review for material decisions, explain why intervention is needed, show important changes and consequences clearly, avoid default approval or hidden recipients/material diffs, and avoid alert volume that makes careful review unrealistic.
- Define what happens when a reviewer is unavailable, evidence is insufficient, reviewers disagree, the request expires, requirements/state changes before action, or the reviewer requests escalation/more information. Do not silently default to consequential execution unless explicit policy authorizes that behavior.
- Treat human review as one workflow component rather than proof of system correctness. Preserve verification, authorization, least privilege, logging/evidence, and rollback/recovery controls independently.
- Compare human review with deterministic automation, one qualified reviewer, multi-review/advisory approaches, and fully manual handling based on consequence, uncertainty, evidence quality, latency/cost, and available authority.
- Evaluate reviewer decision latency, approval/rejection/modification/escalation rates, evidence insufficiency, disagreement, missed defects, unnecessary review volume, override/bypass attempts, fatigue indicators, downstream defects/adverse outcomes, and human time/cost per accepted result.
- Link `agents-and-automation/workflows-and-orchestration/human-approval-gates/` for deterministic consequential-action gate contracts and `operations-and-control/runtime-human-intervention/` for live agent takeover/correction/escalation.

## Validation

- Human review is placed where it can still influence or authorize the controlled outcome.
- Reviewer context is inspectable and evidence-backed rather than only a model summary.
- Human judgment does not replace deterministic validation or authorization that can be enforced directly.
- Decision authority, unavailability/expiry/escalation, and persistence are explicit where material.
- Review volume and interface design account for fatigue/rubber-stamping risk.
- Consequential agent gate semantics are linked rather than redefined here.
