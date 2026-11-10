# Documentation Requirements

## Requirements

- Present the Berkeley Function Calling Leaderboard (BFCL) as a released benchmark/dataset family for evaluating function/tool calling and current agentic tool-use behavior.
- Preserve the current V4 agentic scope only with version context, including web-search, memory-management, and format-sensitivity evaluation surfaces when supported by the official benchmark.
- Keep live-data slices, benchmark versions, test-case inventories, model handlers, cost/latency measurements, and leaderboard results freshness-sensitive.
- Distinguish the BFCL benchmark/dataset from Gorilla models, the Gorilla software repository as a whole, and unrelated function-calling APIs.

## Validation

- BFCL remains a benchmark/dataset identity rather than a model, framework, or hosted model API.
- Comparative model claims remain tied to the exact benchmark version and evaluation configuration.

## Scoped original-source qualification — 2026-11-08

- **Berkeley Function Calling Leaderboard (BFCL)** is the UC Berkeley/Gorilla team's original versioned **function- and tool-calling evaluation dataset and protocol**, not merely a mutable rank table. Its **BFCL V4** release expands prior AST-based single-call/multi-call and multiturn tests with agentic **web-search and memory** tasks plus format sensitivity. Published V1–V4 results, task splits, live function environments and their graders must stay pinned to specific benchmark code and corpus revisions.
- The publisher's currently presented V4 leaderboard states **last updated 2026-04-12** and identifies the evaluation implementation by original source-code commit and package release. Live API tools, function registries and model endpoints can change. Aggregate accuracy mixes scenario categories under explicitly selected weighting, so a model's leaderboard position is not universal tool-execution reliability, safe-action authorization, or an independently verified modern deployment score.
- Original publisher sources: https://gorilla.cs.berkeley.edu/leaderboard ; https://github.com/ShishirPatil/gorilla .
- The original-source gate qualifies the existing benchmark family, V4 task/protocol boundaries, version and original publisher only. No tool execution, function-call replay, benchmark model evaluation, independent dataset asset-rights or security/legal audit, missing reader repair, full schema/cache/CI/render, clean or final gate.
