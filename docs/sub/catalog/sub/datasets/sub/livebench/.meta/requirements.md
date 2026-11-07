# Documentation Requirements

## Requirements

- Identify LiveBench as a recurring-release benchmark/dataset family designed around objective ground-truth scoring and reduced test-set contamination risk.
- Preserve task/category and release boundaries when describing the benchmark; do not turn one leaderboard snapshot or one public release into a timeless identity fact.
- Keep the dataset/question sets distinct from the LiveBench runner, API adapters, Docker-based task execution, leaderboard service, and generic benchmark methodology.
- Preserve the project's recurring-new-question strategy as a contamination-mitigation mechanism without claiming it guarantees independence from model training data.
- Treat public-question availability, release identifiers, task sets, execution requirements, retry behavior, and leaderboard results as mutable/version-sensitive facts.

## Validation

- LiveBench is represented as a benchmark family with changing releases rather than one static score table.
- Objective ground truth is not generalized to unrelated benchmarks or every possible future LiveBench task without upstream support.
- Results are scoped to the applicable release, tasks, and evaluation conditions.

## Scoped original-source qualification — 2026-11-08

- **LiveBench** is a published recurring-release benchmark family designed for **objective ground-truth grading and reduced public-test-set contamination**, with recurring fresh question sets and version-specific task categories rather than one immutable question inventory.
- The original upstream README distinguishes its historically named **2025-04-25** release from the then-latest fully public **2024-11-25** question set; these are time-scoped documentation statements, **not a claim about the latest release in November 2026**. Public, private, or delayed-release questions and the runnable scoring harness, adapters and leaderboard are separate revision/access surfaces.
- First-party sources: https://github.com/LiveBench/LiveBench ; https://livebench.ai/ ; https://huggingface.co/livebench ; https://arxiv.org/abs/2406.19314
- Original-source qualification covers the benchmark family and upstream release, access and grading boundaries only. No live model evaluation, current leaderboard verification, proof of uncontaminated training or complete rights/security/legal audit, root-wide validation, clean or final credit.
