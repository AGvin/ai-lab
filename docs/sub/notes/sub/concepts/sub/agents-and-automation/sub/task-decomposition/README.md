# Task Decomposition

Legacy residual retained for practical decomposition, parallelization, context-partitioning, and recombination guidance that is intentionally outside the canonical Planning and Scheduling concept owner.

> **Migration note:** Task-decomposition identity, hierarchical/recursive decomposition, relationship to planning/execution, and non-universal decomposition order are already preserved in `docs/sub/concepts/sub/reasoning-and-decision-making/sub/planning-and-scheduling/`. The remaining material below stays here until its exact learning, agent-workflow, orchestration, or engineering owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Practical decomposition can separate work such as:

- research into source discovery, evidence extraction, comparison, and synthesis;
- code changes by component or responsibility;
- document processing by independent files or sections; and
- specialized subtasks assigned to different tools, agents, or deterministic workers.

These are workflow examples rather than part of the generic planning definition.

## Decomposition-design residual

Decompose around meaningful responsibility, dependency, data, or verification boundaries rather than arbitrary token/size targets. A useful subtask should have enough relevant context to make correct decisions plus a clear input, expected output, dependencies, and completion/acceptance criterion.

Parallelize only units that can proceed safely without hidden dependency or uncontrolled shared mutable state. Define artifact ownership, conflict detection, duplicate-work handling, and recombination/validation before dispatch when outputs must later be merged.

Excessive decomposition can increase coordination cost, lose global context, duplicate work, and produce incompatible partial results. Prefer a simpler deterministic loop or single-owner workflow when it already satisfies the workload.

These decomposition and recombination practices remain migration source material until their exact learning, orchestration, engineering, or project owners are verified.
