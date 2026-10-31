# Documentation Requirements

## Requirements

- Identify Terminal-Bench 2.0 as a released independently versioned benchmark of AI agents doing end-to-end tasks in containerized terminal environments, distinct from its original Terminal-Bench 1.x task corpus and subsequent Harbor evaluation harness.
- Preserve the benchmark's own versioned task inventory, self-contained containers, oracle solutions, validators, reproducible task environments and terminal-agent evaluation protocol. Do not conflate the number of tasks from different benchmark revisions.
- Keep Harbor as an evaluator/rollout execution framework, not the same entity as the benchmark dataset; use the released Terminal-Bench 2.0 repository as version-specific evidence and record the selected dataset revision; a generic current run page or a query parameter does not establish a pinned 2.0 selection.
- Distinguish task-solving scores from model quality independent of agent harness, tool access, container environment, execution budgets, scoring hooks and reference revisions.
- Preserve the Laude Institute/Harbor upstream maintenance boundary; auxiliary leaderboard dashboards and model submissions are not new benchmark entities.
- Preserve the canonical first-party producer relation and matching inverse.
- Recognize the Stanford/Laude collaboration identified by the release announcement without converting stewardship into exclusive task authorship.
- Keep benchmark material out of training corpora used by evaluated models and distinguish benchmark evaluation from training use to avoid contamination.

## Validation

- The released dataset/benchmark identity remains distinct from evaluation software/harnesses, leaderboards and model submissions.
- Revision, scoring and methodology boundaries are explicit when numerical claims are made.
- Source links and reciprocal producer provenance resolve correctly.
