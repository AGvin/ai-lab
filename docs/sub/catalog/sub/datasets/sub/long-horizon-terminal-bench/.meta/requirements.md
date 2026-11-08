# Documentation Requirements

## Requirements

- Present Long-Horizon Terminal-Bench as a released long-horizon agent benchmark for sustained work in containerized terminal environments with dense intermediate reward grading.
- Preserve the original 46-task July 2026 release and the current 77-task LHTB 2.0 October 2026 expansion as versions of one benchmark family, with long stateful execution horizons, fine-grained graded subtasks, and partial-credit evaluation rather than only short-horizon binary task completion.
- Keep the benchmark/dataset identity distinct from Terminal-Bench itself, Harbor/evaluation harness software, individual model leaderboard results, and generic long-horizon-agent concepts.
- Treat task inventory, leaderboard results, evaluator implementation, runtime budgets, released versions, and dataset packaging as freshness-sensitive.

## Validation

- LHTB remains a benchmark/dataset identity rather than a terminal agent, sandbox, or evaluation framework.
- Claims about scores or model rankings are version- and run-scoped rather than intrinsic benchmark facts.

## Scoped original-source qualification — 2026-11-08

- **Long-Horizon Terminal-Bench (LHTB)** is the original July 2026 long-horizon stateful terminal benchmark with intermediate task-grading signals. The original **46-task** release is historic; the upstream **October 2026 LHTB 2.0** expands the same versioned benchmark to **77 tasks** (31 additional cases in `tasks-2.0/`), not a separate canonical dataset entity. The existing 46-only reader is therefore an incomplete latest-release description and requires reader reconciliation without duplicate source-gate credit.
- Original 46-task and newer 77-task result tables are **not directly comparable**: the publisher documents a 90-minute earlier versus **three-hour** v2.0 task time budget and a **modified Harbor runner** with `continue_until_timeout` for long-running tasks and binary verifier feedback. Do not treat a stock Harbor reproduction or a hidden task-grader as demonstrated behavior without exact task/harness revisions.
- The upstream Apache-2.0 repository license does not independently grant usage or redistribution rights to all bundled images, third-party toolchains, test assets, or model trajectories. Container tasks and evaluator scripts are untrusted execution inputs requiring isolated credentials, hosts and resource budgets.
- First-party sources: https://github.com/zli12321/LHTB ; https://hub.harborframework.com/datasets/silrlab/long-horizon-terminal-bench-2.0/latest .
- Scoped gate covers one existing benchmark family and independently documented version-specific task/evaluation boundaries only. No agent runtime, third-party asset rights/legal/security audit, reader/page repair, whole repository schema/cache/CI/render, clean or final delivery.
