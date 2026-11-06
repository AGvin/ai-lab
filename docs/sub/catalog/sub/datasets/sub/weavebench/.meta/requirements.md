# Documentation Requirements

## Requirements

- Present WeaveBench as Microsoft Research's long-horizon real-world benchmark for computer-use agents that must orchestrate GUI observations/actions with CLI and code operations inside one trajectory.
- Preserve the released benchmark boundary: 114 tasks across eight work domains plus trajectory-aware judging of deliverables, screenshots, logs, files, and action traces.
- Keep evaluated agent runtimes, desktop-control plugins, frontier models, and trajectory-judge implementations separate from the benchmark identity unless independently materialized.
- Treat task inventory, judge implementation, runtime setup, leaderboards, and published results as freshness-sensitive.

## Validation

- WeaveBench remains a benchmark/dataset identity rather than a computer-use agent or runtime.
- Model/runtime scores remain run-scoped and are not intrinsic benchmark facts.
