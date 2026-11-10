# Documentation Requirements

## Requirements

- Present WeaveBench as Microsoft Research's long-horizon real-world benchmark for computer-use agents that must orchestrate GUI observations/actions with CLI and code operations inside one trajectory.
- Preserve the released benchmark boundary: 114 tasks across eight work domains plus trajectory-aware judging of deliverables, screenshots, logs, files, and action traces.
- Keep evaluated agent runtimes, desktop-control plugins, frontier models, and trajectory-judge implementations separate from the benchmark identity unless independently materialized.
- Treat task inventory, judge implementation, runtime setup, leaderboards, and published results as freshness-sensitive.

## Validation

- WeaveBench remains a benchmark/dataset identity rather than a computer-use agent or runtime.
- Model/runtime scores remain run-scoped and are not intrinsic benchmark facts.

## Scoped original-source qualification — 2026-11-08

- **WeaveBench** is Microsoft Research's original June 2026 long-horizon computer-use benchmark comprising **114 tasks in eight work domains**. It assesses an agent that must combine **GUI observations/actions, CLI operations and code execution** within a single work trajectory rather than conflating separate browser, code and shell-only tests.
- The publisher's trajectory-aware judging inspects deliverables, logs, screenshots, files and action traces, not merely a final answer; a successful-looking output does not necessarily meet the recorded workflow and artifact criteria. Reported model/runtime scores and judge findings are specific to the configured desktop environments, model versions, agent tools and evaluation methodology.
- Original publisher source: https://www.microsoft.com/en-us/research/publication/weavebench-a-long-horizon-real-world-benchmark-for-computer-use-agents-with-hybrid-interfaces/ .
- Scoped source acceptance confirms one already materialized benchmark identity, task/work-domain boundary and publisher method, not dataset-wide redistribution rights, privileged computer control, executed runs, reproduced model results, independent safety/security/legal audit, whole-repo schema/cache/CI/render, clean or final delivery.
