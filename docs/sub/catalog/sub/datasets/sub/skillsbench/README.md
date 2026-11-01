# SkillsBench

**SkillsBench** is a released benchmark dataset for evaluating whether reusable **Agent Skills** improve AI agents' ability to complete specialist tasks. The original [BenchFlow publishing project](https://github.com/benchflow-ai/skillsbench) distributes the benchmark independently from the BenchFlow evaluation runtime and from models or agents measured by it.

## Dataset and release boundaries

The public [SkillsBench v1.1 release](https://github.com/benchflow-ai/skillsbench/releases/tag/v1.1) pins **87 active tasks across eight categories** as native `task.md` packages. Each contains task instructions and may include a container environment, curated Skills, an oracle implementation and a verifier. The release's [registry](https://github.com/benchflow-ai/skillsbench/blob/main/registry.json) pins task source commits and content digests; v1.1 requires **BenchFlow >=0.6.3,<0.7** to reproduce its evaluation protocol. The `tasks-extra/` packages are excluded from this benchmark roster unless explicitly selected.

Do not combine results from the original February 2026 paper's **86-task** snapshot, later tagged **87-task v1.1** release, or ongoing main-branch development as if they share one immutable set. Current contributing documentation mentions 1.2 development, while the available tagged public release and official registry pin v1.1. Compare models only with exact task versions, harness, skill/no-skill conditions, trial aggregation, verifier and runtime revisions. The leaderboard is a separate result archive, not additional benchmark tasks.

## Rights and operational safeguards

The original repository's [Apache-2.0 license](https://github.com/benchflow-ai/skillsbench/blob/main/LICENSE) and the publisher's [Hugging Face dataset metadata](https://huggingface.co/datasets/benchflow/skillsbench) both declare Apache-2.0. That does **not** independently verify the redistribution rights for every third-party input bundled into tasks; review exact assets and notices before reuse.

Benchmark tasks may execute shell scripts, container builds, oracles and verifiers. Run unreviewed packages in isolated sandboxes with scoped network and filesystem access, protect model API keys and private trajectories, and account for hosted sandbox costs. No benchmark run, independent score replication, complete license/ownership audit or whole-catalog build has been performed.

## Original producer

- [BenchFlow publishing project](../../../producers/sub/b/sub/benchflow/).

## Official resources

- [Original SkillsBench project](https://github.com/benchflow-ai/skillsbench)
- [Tagged v1.1 benchmark release](https://github.com/benchflow-ai/skillsbench/releases/tag/v1.1)
- [Pinned version registry](https://github.com/benchflow-ai/skillsbench/blob/main/registry.json)
- [Project website and leaderboard](https://www.skillsbench.ai/)
- [Publisher's dataset mirror](https://huggingface.co/datasets/benchflow/skillsbench)
- [BenchFlow evaluation framework (separate software)](https://github.com/benchflow-ai/benchflow)
