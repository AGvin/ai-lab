# Documentation Requirements

## Requirements

- Teach planning as construction and maintenance of an explicit, inspectable representation of intended actions/work needed to achieve a goal under assumptions, dependencies, constraints, resources, and acceptance/terminal conditions.
- Treat a plan as a versioned artifact when work is non-trivial. A plan is not private hidden chain-of-thought and should not require exposing model reasoning; it should contain the externally useful structure needed to coordinate, validate, execute, revise, or audit work.
- Where material, teach plan fields such as plan identity/version, goal, authoritative requirements, assumptions and unknowns, stable action/task identities, dependencies and ready/preconditions, expected inputs/outputs/effects, artifact references, acceptance criteria, capability/resource needs, constraints, and terminal conditions.
- Distinguish required work from optional optimization and distinguish verified facts from assumptions, estimates, hypotheses, or unresolved unknowns so later execution does not treat uncertain planning state as authoritative fact.
- Teach useful decomposition granularity: actions/subproblems should be small enough to have inspectable prerequisites, outputs, and acceptance while remaining large enough that coordination overhead does not dominate the work.
- Preserve dependency structure explicitly enough to identify sequential, parallel, conditional, mutually exclusive, or independently ready work. Do not infer safe parallelism merely because tasks appear textually separate.
- Validate a plan before relying on it: check requirement/goal coverage, dependency consistency, input/prerequisite availability, feasibility under declared constraints/resources, observable acceptance criteria, unresolved unknowns, and whether a simpler direct action or fixed procedure would suffice.
- Make plan revision explicit. Preserve stable task/issue identity where useful, record why the plan changed, compare material changes with the prior version, retain still-valid work, identify invalidated downstream actions, and bound repeated revisions when the plan oscillates or remains infeasible.
- Treat material state or assumption changes as replanning triggers rather than silently editing plan history. Examples include disproved assumptions, unavailable prerequisites, newly discovered dependencies/conflicts, changed authoritative requirements, resource/constraint violations, or evidence that the current plan cannot satisfy acceptance.
- Distinguish planning quality from execution success. A plan can be coherent but infeasible in the actual environment, while an executor can fail despite a valid plan; evaluation should attribute failures to representation, coverage, assumptions, dependencies, feasibility, or execution separately.
- Evaluate requirement/goal coverage, dependency/readiness correctness, feasibility, revision frequency/reasons, valid work preserved across revisions, unnecessary/duplicate planned work, acceptance completeness, planning latency/cost, and human correction needed compared with simpler baselines.
- Keep agent-specific planner/executor interfaces, tool/permission boundaries, authoritative runtime state, task execution monitoring, stale-executor fencing, and operational recovery with Agents and Automation.
- Keep concrete planning framework APIs, prompts, traces, exact project plans, and mutable product behavior with their catalog/evidence/project owners.

## Validation

- Plans are explicit inspectable artifacts and are never equated with private hidden chain-of-thought.
- Facts, assumptions, unknowns, dependencies, acceptance criteria, and version/revision state remain distinguishable where material.
- Planning is separated from execution and from agent-specific runtime control.
- Revisions preserve valid prior work and identify downstream invalidation rather than recreating every plan from scratch without traceability.
- Planning is compared against simpler direct/fixed approaches and is used only when the explicit artifact adds coordination or decision value.
