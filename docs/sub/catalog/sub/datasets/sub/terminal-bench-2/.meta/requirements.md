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

## Scoped original-source qualification — 2026-11-08

- **Terminal-Bench 2.0** is the independently versioned task benchmark for agents performing verifiable end-to-end work in **containerized terminal environments**. The original publisher's `terminal-bench-2` repository identifies its released dataset as **`terminal-bench@2.0`**; this is not the earlier Terminal-Bench 1.x corpus, a CLI agent product, or the separate **Harbor** evaluation/rollout framework.
- The official publisher documents Harbor as the current evaluation runner and explains task-bound oracle solutions and validators. Dataset identity, reference revision, container image, selected agent/harness, tool access, scoring hooks and execution budgets must be pinned before numerical comparisons; publisher statements about task quality are not independently validated by this catalog source review.
- First-party sources: https://github.com/harbor-framework/terminal-bench-2 ; https://github.com/laude-institute/terminal-bench-2 ; https://harborframework.com/docs/running-tbench
- Acceptance covers the existing `2.0` source dataset identity, official published task and harness separation, and documented version boundary. No container command execution, oracle/agent run, task rights/security/operational audit, root-wide schema/cache/CI/render, clean or final credit.
