# Human in the Loop

Legacy residual retained for practical approval, escalation, reviewer-context, and intervention-workflow guidance that is intentionally outside the canonical Oversight and Intervention concept owner.

> **Migration note:** Human-oversight identity, HITL/HOTL/HIC taxonomy variability, monitoring/review/approval/intervention distinctions, meaningful-oversight requirements, autonomy relationship, and reviewer failure modes are already preserved in `docs/sub/concepts/sub/human-ai-interaction/sub/oversight-and-intervention/`. The remaining material below stays here until its exact learning, workflow-control, governance, security, or project owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Approval-pattern residual

Human control points can be useful to:

- approve a proposed plan before consequential execution;
- review generated code or document changes before publication;
- resolve low-confidence or ambiguous classifications;
- confirm recipients, amounts, permissions, or scope before an external action; and
- handle repeated failures, policy conflicts, or escalations that exceed the automated workflow's authority.

These are procedural examples rather than a universal requirement that every AI workflow use approval gates.

## Reviewer-context and workflow residual

Place approval/intervention before the consequential transition, not after the effect has already occurred. Show the reviewer enough source evidence, proposed action, expected effect, material uncertainty, and relevant context to make the decision rather than only a model-generated summary.

Define explicit approve, reject, modify, request-more-information, timeout/default, and escalation behavior where the workflow requires those states. Persist the human decision as authoritative workflow state and ensure model/tool execution cannot bypass the gate through a different path.

Human review is not a substitute for deterministic validation that can directly establish the required property. Excessive alerts or poorly explained requests can create rubber-stamping and fatigue; reviewer competence, available time, evidence quality, and intervention authority determine whether the control is meaningful.

These approval and intervention practices remain migration source material until their exact learning, workflow-control, governance, security, or project owners are verified.
