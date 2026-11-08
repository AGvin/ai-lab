# Documentation Requirements

## Requirements

- Present ORAgentBench as an execution-grounded benchmark for autonomous LLM agents on end-to-end operations-research workflows.
- Preserve task count, difficulty distribution, public/hidden evaluator boundaries, scoring thresholds, bundled agent adapters, solver/runtime requirements, and released benchmark version only from current upstream artifacts.
- Distinguish benchmark tasks/datasets from the reusable optimization skills bundled for experiments.
- Treat leaderboard/model results and task inventory as freshness-sensitive.

## Validation

- ORAgentBench remains a benchmark/dataset identity rather than an agent framework or skills collection.
- Claims about pass rates and benchmark composition resolve to the released repository/paper artifacts.

## Scoped original-source qualification — 2026-11-08

- **ORAgentBench** is the original June–July 2026 execution-grounded operations-research agent benchmark with **107 human-reviewed executable tasks** across easy, medium and hard tiers. Tasks require reading heterogeneous operational files, formulating and executing optimization code, then submitting feasible decision artifacts judged by hidden task-specific validators.
- The original evaluation separates required artifact/schema validity, **hard feasibility** and normalized objective quality, using a task-pass threshold for the released benchmark. Its 14 evaluated model-agent configurations and scores are publisher results tied to particular solvers, isolation, task versions and runtime budgets, not independently reproduced agent/model ratings.
- Bundled optimization skills, Harbor environment images, task graders and the ORAgentBench corpus remain distinct resources; running untrusted task/solver scripts requires isolated environments and bounded credentials. Original task/data asset reuse rights and evaluator access require independent review.
- First-party sources: https://github.com/ORAgentBench/ORAgentBench ; https://oragentbench.github.io/ ; https://arxiv.org/abs/2606.19787 .
- Source credit is limited to one pre-existing original benchmark identity and public task/evaluation method. No solver execution, private validator access, model-score replication, rights/security/legal clearance, full schema/cache/CI/render, clean or final acceptance.
