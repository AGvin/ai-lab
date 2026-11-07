# Documentation Requirements

## Requirements

- Present OSWorld as the released benchmark family for evaluating multimodal computer-use agents on open-ended tasks in real computer environments.
- Preserve the current OSWorld 2.x benchmark/version boundary, task assets, environment images, website snapshots, and verified-result protocol as version-sensitive state.
- Keep environment/runtime implementation details separate from the benchmark task/dataset identity unless independently materialized.
- Treat task counts, active recommended release, model/agent results, and infrastructure setup as freshness-sensitive.

## Validation

- OSWorld remains a benchmark/dataset identity rather than a computer-use agent or desktop automation framework.
- Results are not compared across materially different OSWorld releases without explicit version context.

## Scoped original-source qualification — 2026-11-08

- **OSWorld** is the computer-use-agent benchmark family for tasks executed in real graphical operating-system environments. The original research/environment, **OSWorld-V2** code and separately versioned benchmark task bundles are not one immutable dataset or an agent product. The current first-party OSWorld-V2 README labels **`osworld-v2.1`**, released **2026-09-16**, as the recommended pinned version, distinct from historical `2026.06.24` and `2026.08.08` releases.
- Reproducibility requires matching a single benchmark-release manifest to Python task files, gated task assets, VM/provider images, website snapshots and evaluation harness; the publisher explicitly discourages using mutable `main` or mixing version components. UI task results also depend on resets, credentials and environment snapshots; historical leaderboard performance is not an independently verified result.
- Verified first-party sources: https://github.com/xlang-ai/OSWorld-V2 ; https://github.com/xlang-ai/OSWorld-V2/tree/main/benchmark_releases ; https://osworld-v2.xlang.ai/
- Acceptance covers existing benchmark family, publisher-maintained version boundary and public evaluation methodology only. No VM/browser action execution, restricted task-asset retrieval, performance/security/legal/rights audit, full repository schema/cache/CI/render, clean or final credit.
