# TheAgentCompany

**TheAgentCompany** (The Agent Company) is an original benchmark dataset of **175 workplace tasks** for AI agents operating inside a simulated small software company. The [research paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d744742f6fac4d1134c019b7cef3c8a-Abstract-Datasets_and_Benchmarks_Track.html) appeared at NeurIPS 2025, Datasets and Benchmarks. This catalog entry covers its concrete task dataset, **not** the execution harness, evaluated AI models, grading service, live business integrations or separately incorporated company.

## Dataset, tasks and evaluation

The [original 1.0.0 release](https://github.com/TheAgentCompany/TheAgentCompany/releases/tag/1.0.0) was published on 2024-12-20. Its source snapshot `de36f6e74da992b18b877c437d936b7cb64a8105` contains **175 distinct workspaces/tasks/*/task.md instructions** for six general workplace roles: software engineer, product manager, data scientist, human resources, finance and administration. The tasks combine coding, communications, documents, spreadsheets, reasoning and coordination with simulated colleagues.

Agents work against self-hosted, pre-populated instances of **GitLab, Plane, ownCloud and RocketChat**. The benchmark uses result-based checkpoints and subcheckpoints with deterministic and, where configured, LLM-based evaluation. The Python/OpenHands runner, encrypted evaluator code, server fixtures, external backups, optional simulated coworkers and published leaderboard results are **not additional task-dataset entities**. A score depends on task/version, evaluation implementation, tool access, simulation state, selected model, judge and run configuration; do not mix unmatched historical evaluation protocols.

**Snapshot comparison:** the original main revision `98b68ef82a47690c316f42fddb05baafaab56851` (2025-11-17) still has 175 task.md files with the same corresponding Git blob hashes as the 1.0.0 release, but multiple harness/deployment scripts differ. This does **not** independently establish reproducible, equivalent execution or scoring across versions. Pin the original release and all runtime dependencies for comparison.

## License, trust and operational safeguards

The original [root LICENSE](https://github.com/TheAgentCompany/TheAgentCompany/blob/main/LICENSE) grants **MIT** for the project source, but the rights to separately downloaded backups, service/container images, third-party data and dependencies are not independently cleared by that one grant. Original setup instructions download scripts and external server fixtures; some examples loosen Docker socket permissions or require privileged execution. **Do not run them unreviewed on a production host**: use a disposable isolated VM, inspect and pin scripts/images first, protect the Docker socket, limit mounts/network/credentials and secure agent traces, screenshots and evaluator API keys. No source or benchmark was executed in this review.

The paper credits a research team with affiliations spanning Carnegie Mellon University, independent researchers and Duke University. The GitHub organization name does not prove a separately incorporated publishing business; that **producer identity remains deferred**. Ultimate beneficial ownership and indirect funding/control were not completely audited, and no unsupported geopolitical risk label is assigned.

## Original resources

- [TheAgentCompany source repository](https://github.com/TheAgentCompany/TheAgentCompany)
- [Public benchmark 1.0.0 release](https://github.com/TheAgentCompany/TheAgentCompany/releases/tag/1.0.0)
- [Project site and leaderboard](https://the-agent-company.com/)
- [Original NeurIPS 2025 paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d744742f6fac4d1134c019b7cef3c8a-Abstract-Datasets_and_Benchmarks_Track.html)
- [Project license](https://github.com/TheAgentCompany/TheAgentCompany/blob/main/LICENSE)
- [Upstream evaluation/setup instructions](https://github.com/TheAgentCompany/TheAgentCompany/blob/main/evaluation/README.md)
