# Planning

Legacy residual retained for agent-specific planning workflow and replanning guidance that is intentionally outside the canonical Planning and Scheduling concept owner.

> **Migration note:** Generic planning/scheduling identity, plan representations, task decomposition, planning-versus-execution, feasibility/authorization boundaries, method diversity, and replanning semantics are already preserved in `docs/sub/concepts/sub/reasoning-and-decision-making/sub/planning-and-scheduling/`. The remaining material below stays here until its exact agent-learning, workflow-design, engineering, or project owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Agent-planning application residual

Agent workflows can use planning to:

- break a repository change into inspection, implementation, testing, and publication stages;
- identify information that must be retrieved before a later decision;
- order tool operations whose inputs depend on earlier results; and
- place human approval before consequential actions.

These are agent/workflow examples rather than part of the generic planning definition.

## Planning-workflow residual

Prefer short, inspectable steps with clear prerequisites, expected outputs, and acceptance/verification points over vague action lists. Keep the currently actionable plan in explicit workflow state when continuation/recovery depends on it, rather than relying on conversational memory alone.

Separate reversible exploration from consequential execution and do not treat a plausible generated plan as evidence that required tools, permissions, data, or resources actually exist. Replan when observations, failures, resource state, or evidence invalidate a material assumption instead of forcing an obsolete sequence.

Detailed planning has a cost: long plans can consume context, create unnecessary coordination, and become stale rapidly in dynamic environments. Use a deterministic operation or simpler workflow when it already satisfies the task.

These agent-specific planning practices remain migration source material until their exact learning, workflow-design, engineering, or project owners are verified.
