# Documentation Requirements

## Requirements

- Identify Terminal-Bench 2.0 as a released independently versioned benchmark of AI agents doing end-to-end tasks in containerized terminal environments, distinct from its original Terminal-Bench 1.x task corpus and subsequent Harbor evaluation harness.
- Preserve the benchmark's own versioned task inventory, self-contained containers, oracle solutions, validators, reproducible task environments and terminal-agent evaluation protocol. Do not conflate the number of tasks from different benchmark revisions.
- Keep Harbor as an evaluator/rollout execution framework, not the same entity as the benchmark dataset; benchmark version `terminal-bench@2.0` is a dataset selection, not a separate software release by itself.
- Distinguish task-solving scores from model quality independent of agent harness, tool access, container environment, execution budgets, scoring hooks and reference revisions.
- Preserve the Laude Institute/Harbor upstream maintenance boundary; auxiliary leaderboard dashboards and model submissions are not new benchmark entities.
- Preserve the canonical first-party producer relation and matching inverse.

## Validation

- The released dataset/benchmark identity remains distinct from evaluation software/harnesses, leaderboards and model submissions.
- Revision, scoring and methodology boundaries are explicit when numerical claims are made.
- Source links and reciprocal producer provenance resolve correctly.
