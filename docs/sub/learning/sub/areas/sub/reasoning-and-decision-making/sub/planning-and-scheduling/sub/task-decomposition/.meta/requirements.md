# Documentation Requirements

## Requirements

- Teach task decomposition as breaking a goal/problem into meaningful subproblems or work units whose relationships make planning, assignment, search, execution, verification, or recombination more tractable.
- Decompose around responsibility, dependency, data, state, capability, or verification boundaries rather than arbitrary token/character/size targets unless size itself is the real processing constraint.
- A useful subtask should expose a bounded purpose, relevant input/context, expected output/effect, dependencies/preconditions, assumptions/unknowns, and completion/acceptance criterion where material.
- Teach hierarchical and recursive decomposition without requiring decomposition to happen once before execution. Decomposition can be refined after new information, constraints, failures, or intermediate results change the problem structure.
- Preserve global requirements and terminal acceptance while decomposing. Local subtasks must not optimize their own outputs in ways that silently violate cross-cutting constraints or leave no owner for integration.
- Distinguish decomposition from scheduling and orchestration. Decomposition identifies useful work units/relationships; scheduling allocates/orders them over resources/time; orchestration controls actual execution/state/participants.
- Identify dependencies before claiming parallelism. Units can execute concurrently only when required inputs/state are available and concurrent effects do not violate shared-state/resource/conflict constraints.
- Teach recombination as part of decomposition design when outputs must merge: define artifact/output identity, ownership, compatibility/schema, conflict handling, duplicate-work policy, evidence/provenance, and final validation before dispatch where practical.
- Explain context partitioning trade-offs. Giving each subtask only local context can reduce cost/noise and improve specialization while creating omission/global-consistency risks; pass the authoritative cross-cutting requirements and evidence each subproblem actually needs.
- Explain decomposition costs: coordination, dispatch, duplicated context/work, lost global information, inconsistent partial results, integration/merge effort, and additional validation can exceed the benefit of smaller units.
- Prefer a direct deterministic loop or single-owner procedure when decomposition does not materially improve tractability, parallelism, specialization, verification, or failure isolation.
- Evaluate requirement coverage, dependency correctness, subtask independence, context sufficiency, duplicated/omitted work, conflict/integration failures, recombination correctness, coordination cost, and terminal accepted-result quality compared with simpler baselines.
- Keep agent-specific worker/tool assignment, permissions, workflow state, dispatch, parallel execution, and operational recovery with Agents and Automation.

## Validation

- Decomposition boundaries are semantic/operational rather than arbitrary size cuts by default.
- Each subtask has enough context plus explicit inputs/outputs/dependencies/acceptance where material.
- Parallelism is justified by dependency/state analysis rather than by task count alone.
- Recombination/conflict ownership is defined before independent outputs are expected to merge.
- Decomposition is compared against simpler single-owner/direct alternatives.
