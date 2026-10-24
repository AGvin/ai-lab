# Documentation Requirements

## Requirements

- Identify Bloom as the open-source framework originally released by Anthropic for automatically generating behavioral evaluation suites and now maintained by Meridian Labs through Petri Bloom.
- Preserve the seed-driven behavior definition, understanding/ideation/rollout/judgment pipeline, scenario variations, target-model execution, and scoring boundary only while current upstream documentation supports it.
- Keep Bloom distinct from Petri's broad auditing workflow, fixed benchmark datasets, leaderboard results, and generic evaluation concepts.
- Preserve the current repository/lifecycle boundary: the original standalone `safety-research/bloom` repository is frozen while new development occurs in Meridian Labs' Petri Bloom implementation.
- Treat configuration schema, provider/model integrations, pipeline stages, generated evaluation inventory, seed files, scoring, viewer/tooling, and release APIs as freshness-sensitive.
- Do not compare model scores across differently seeded/generated Bloom suites as though they were one immutable benchmark; reproducibility requires full seed/configuration context.
- Preserve Anthropic original production provenance and Meridian Labs current maintenance.

## Validation

- Bloom remains an evaluation-generation framework rather than one fixed benchmark dataset.
- Frozen original repository and current maintained implementation are not treated as duplicate products.
- Evaluation comparisons remain seed/configuration scoped.
