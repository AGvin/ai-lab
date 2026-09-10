# Documentation Requirements

## Requirements

- Use the reader-facing title `Planning and Scheduling`.
- Define planning as constructing or selecting actions, subgoals, policies, or other decision structures intended to move from an initial/current situation toward stated goals while respecting applicable action models, dependencies, constraints, and uncertainty assumptions.
- Define scheduling as assigning, ordering, or timing activities and resources subject to temporal, capacity, dependency, availability, or other execution constraints; planning and scheduling interact but are not synonyms.
- Explain that plans can be linear sequences, partial orders, dependency graphs, hierarchical decompositions, conditional branches/policies, or other formal structures; a natural-language checklist is only one possible representation.
- Preserve task decomposition as a planning technique: a complex goal can be decomposed into subgoals/subtasks whose relationships make search, execution, assignment, or verification more tractable. Do not create a separate `task-decomposition` child from the legacy merge source.
- Explain that decomposition can be hierarchical, recursive, interleaved with planning/execution, or derived through domain structure; one fixed decomposition-first procedure is not part of the generic definition.
- Distinguish planning from execution. A syntactically plausible plan is not evidence that actions are feasible, authorized, available, correctly modeled, or successfully executed in the current environment.
- Explain that planning can use symbolic search, constraint solving, optimization, probabilistic/sequential decision methods, learned policies/models, language models, external planners, or hybrid approaches; no one technique is universal.
- Explain that plans may require revision or replanning when observations, resources, goals, constraints, failures, or environment models change; replanning is a response to changed planning state rather than proof that every plan must be generated continuously.
- Distinguish generic planning/decomposition semantics from agent-specific workflow advice. Explicit state management, tool invocation, approval gates, retry/recovery, and agent orchestration retain their selected owners even when a plan references them.
- Keep agent-specific decomposition recipes, project plans, domain action schemas, PDDL/solver tutorials, concrete schedules, model planning benchmarks, and orchestration recommendations with their applicable learning, engineering, evaluation, or project owners.
- Use the canonical entity references as research inputs for automated-planning foundations and the relationship between modern LLM planning and task decomposition when reader-facing rendering is activated.

## Validation

- Planning is not reduced to an LLM-generated list of steps or to agent orchestration.
- Planning and scheduling are distinguished while their interaction is preserved.
- Task decomposition is merged into the planning owner and is not materialized as an unselected child.
- A plan is not presented as evidence of action feasibility, authorization, or successful execution.
- No linear, hierarchical, symbolic, learned, or LLM-based planning method is treated as universally required.
- Agent-specific procedural guidance from the split legacy sources is preserved for later learning/other owners rather than copied into the generic concept.
