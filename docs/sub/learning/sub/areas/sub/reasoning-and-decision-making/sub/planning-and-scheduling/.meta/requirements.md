# Documentation Requirements

## Requirements

- Present Planning and Scheduling as the general learning group for constructing, representing, ordering, revising, and allocating actions over goals, dependencies, resources, time, and constraints independent from a particular agent implementation.
- Keep `planning/`, `task-decomposition/`, `scheduling/`, and `replanning/` as distinct selected learning topics because plan generation/representation, decomposition, resource/time allocation, and plan revision have different learning outcomes.
- Explain that the current materialized subset focuses on `planning/` because planner/executor legacy material contains source-backed plan-representation and executable-plan teaching ready for migration.
- Do not imply that unmaterialized `task-decomposition/`, `scheduling/`, or `replanning/` topics are absent from the selected logical architecture; standard navigation reflects only physical children.
- Teach plans as explicit artifacts with goals, assumptions, actions/tasks, dependencies, preconditions/ready conditions, expected effects/outputs, constraints, resources, acceptance/terminal criteria, and revision identity where those fields matter.
- Distinguish plan construction from execution. A plan describes intended coordinated work; executing actions changes authoritative state and can invalidate assumptions, requiring monitoring/replanning in the applicable agent/workflow/system owner.
- Distinguish planning from scheduling: planning determines actions/structure needed to reach a goal; scheduling assigns/order actions over time/resources/constraints when that dimension is material.
- Distinguish planning from task decomposition: decomposition produces useful subproblems/work units; planning additionally represents dependencies, action ordering/conditions, goals, assumptions, and terminal acceptance.
- Distinguish planning from replanning: replanning updates a plan after material state/assumption/requirement change rather than treating every plan edit as a new independent plan.
- Keep agent-specific planner/executor contracts, tool permissions, workflow state, execution monitoring, and operational recovery in Agents and Automation while linking the general planning concepts taught here.
- Keep concrete planning framework APIs, prompts, traces, provider behavior, and project-specific plans with their catalog/evidence/project owners.

## Validation

- Planning is taught as an implementation-independent reasoning/decision method rather than as a synonym for agent orchestration.
- Plan representation is explicit and inspectable; hidden model reasoning is not required as a plan artifact.
- Planning, decomposition, scheduling, execution, and replanning boundaries remain distinct.
- Current navigation exposes only materialized selected children.
