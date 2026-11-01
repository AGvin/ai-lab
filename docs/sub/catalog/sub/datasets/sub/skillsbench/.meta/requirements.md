# Documentation Requirements

## Requirements

- Identify SkillsBench as BenchFlow's released Agent Skills benchmark dataset, not a hosted model, agent, software runner or evaluated model. Skills are reusable folders with instructions, scripts and resources; the evaluation asks whether they improve task resolution and agent behavior.
- Scope numerical claims to exact releases. The 2026-02 paper/launch described 86 tasks; the reproducible public `v1.1` GitHub release and `registry.json` independently pin **87 tasks** with native BenchFlow `task.md`, `environment/`, `oracle/` and `verifier/` packages. The release organizes tasks into eight categories; do not blend historic task sets or scores.
- Record that `v1.1` requires BenchFlow **>=0.6.3,<0.7**, pins every task to a single release commit and per-task content digest, and excludes the `tasks-extra/` credential-dependent/integration-incompatible packages from the active benchmark roster. The published GitHub release is the reproducible version authority; mainline contributing documentation mentioning upcoming/current 1.2 work does not independently establish a tagged 1.2 benchmark snapshot.
- Separate task data, the BenchFlow SDK/CLI, reference oracle implementations, verifier scripts, LLM agent/harness configuration, leaderboard result archives and third-party source assets. A reported skill lift is conditional on exact paired runs and evaluation choices, not a universal model capability.
- The original project root declares Apache-2.0 and the original Hugging Face distribution metadata currently also declares Apache-2.0. These labels do not establish independent clearance for every embedded third-party artifact or unrestricted reuse of external inputs; assess specific assets and attribution before republishing.
- Running task packages executes untrusted code in Docker or remote sandboxes. Isolate verifier/oracle scripts, remove unnecessary credentials and mounts, limit network and privilege, budget cloud costs, and avoid exposing private trajectories or agent API keys.
- Attribute the original dataset to the BenchFlow publishing project (GitHub `benchflow-ai`, Hugging Face `benchflow`), not to a separately validated incorporated company or a specific model provider. No benchmark execution, comprehensive third-party rights audit, full beneficial-ownership review or global schema/cache/render/CI verification is claimed.
- Preserve reciprocal producer↔dataset relations, current first-party references, and bounded scope of this catalog addition.

## Validation

- One original `catalog/datasets/skillsbench` identity; no separate software, model, service or leaderboard-result entry is credited in this package.
- Reciprocal `catalog/producers/b/benchflow` relations and reader navigation resolve.
- Tagged 87-task `v1.1` release is not confused with the 86-task paper launch, untagged mainline work, optional `tasks-extra`, or evaluator framework.
- Licensing, execution, provenance and score-comparison limitations remain visible; full benchmark/runtime/global checks are not inferred.
