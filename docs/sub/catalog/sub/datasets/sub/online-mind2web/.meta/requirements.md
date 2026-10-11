# Documentation Requirements

## Requirements

- Identify Online-Mind2Web as the independently published COLM 2025 benchmark of 300 tasks on 136 live real-world websites; this end-to-end live-browser evaluation is distinct from original Mind2Web's static offline action-prediction dataset.
- Preserve the upstream task replacement policy: outdated, invalid or CAPTCHA-blocked tasks are revised, including 36 replacements announced on 2025-11-03 and additional 2026 task changes; do not treat the task collection as immutable.
- Preserve the 2026-05-23 v2 submission schema announcement and distinguish human review and automatic or model-based evaluation protocols. Pin submission schema, task IDs, task snapshot date, website availability and evaluation method for any comparison of longitudinal scores.
- Distinguish the live task-success objective from original Mind2Web offline action accuracy, Mind2Web 2 search-answer citation/evidence quality and resettable self-hosted WebArena task outcomes.
- Explicitly account for evolving third-party websites, access restrictions, anti-bot controls and variable site state; do not claim live sites or historical leaderboard scores are reproducible without a dated task/environment snapshot.
- Attribute the maintained benchmark publication to Ohio State NLP Group while acknowledging UC Berkeley coauthors and shared research authorship separately from the steward.

## Validation

- The official first-party repository substantiates task/site counts, replacement history, 2026 submission-schema revision and named research affiliations.
- The Ohio State NLP Group producer has the exact inverse `produces` relation to `catalog/datasets/online-mind2web`.
