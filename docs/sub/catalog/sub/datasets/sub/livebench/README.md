# LiveBench

LiveBench is a recurring-release benchmark/dataset family designed around objective ground-truth scoring and reduced test-set contamination risk.

## Dataset boundary

LiveBench changes over time through new question releases, so one public release or leaderboard snapshot is not the timeless benchmark identity. Dataset question sets remain distinct from the runner, API adapters, Docker-based execution, leaderboard service, and generic benchmark methodology. Recurring new questions mitigate contamination risk without guaranteeing independence from all model training data.

Public-question availability, release identifiers, task sets, execution requirements, retry behavior, and leaderboard results are mutable or version-sensitive; results must be scoped to the applicable release, tasks, and evaluation conditions.

## Official resources

- [LiveBench](https://livebench.ai/)
- [LiveBench repository](https://github.com/LiveBench/LiveBench)
- [LiveBench paper](https://arxiv.org/abs/2406.19314)
