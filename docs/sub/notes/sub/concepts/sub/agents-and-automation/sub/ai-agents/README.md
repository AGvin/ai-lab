# AI Agents

Legacy residual retained for application examples and practical model-versus-deterministic-control guidance that is intentionally outside the canonical Agents and Autonomy concept owner.

> **Migration note:** Agent identity, the distinction between an agent and a single model/multi-step pipeline, the complete-system boundary, observations/state/tools/feedback, autonomy versus mere repetition, and the requirement for separate authorization/validation/stopping controls are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/`. The remaining material below stays here until its exact learning, workflow-design, engineering, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Agent-style control can be useful when later actions genuinely depend on earlier observations or tool results, for example:

- repository maintenance and bounded implementation workflows;
- evidence-gathering research;
- administration across several external systems;
- multi-stage data processing; and
- customer-support or operations workflows whose next step depends on validated state.

These are application examples rather than part of the canonical definition of an agent.

## Workflow-design residual

Prefer deterministic application logic for steps whose correct behavior can be expressed and validated directly. Use model-directed decisions where interpretation, ambiguity, flexible planning, classification, synthesis, or adaptation to newly observed results genuinely benefits from model behavior.

Do not use an agent label as justification for broad credentials, open-ended loops, or model-owned authorization. Explicit budgets, stopping conditions, permission boundaries, validation, and recovery remain system responsibilities even when the model chooses the next action.

These application and workflow-design practices remain migration source material until their exact learning, engineering, or decision-support owners are verified.
