# Documentation Requirements

## Requirements

- Present τ-bench as Sierra's maintained released family of realistic tool-agent-user evaluation benchmarks, with user-simulated dialogue, domain policy compliance, structured tools, and state- or task-grounded grading rather than a generic agent framework or customer-service software product.
- Preserve versioned evaluation identities without duplicating the shared benchmark family: original τ-bench (2024), τ²-bench dual-control user and agent tool actions (2025), and τ³-bench knowledge retrieval and full-duplex voice variants (2026). Distinguish the text, knowledge and voice tracks and their evaluation setups.
- Note that the **2026-07-22 v1.0.1** grading update repairs `banking_knowledge` tasks and changes affected benchmark scores compared with pre-v1.0.1 definitions; require pinned task and grading revisions before comparing scores across releases or leaderboard snapshots.
- Keep domains such as airline, retail, telecom and banking knowledge, policies, synthetic users, tool permissions and retrieval/voice simulation constraints aligned with the first-party benchmark documentation. Do not conflate the benchmark repository's install/CLI/harness APIs with immutable dataset identity.
- Preserve Sierra as source steward/producer, distinguished from models submitted to the benchmark and from independent research collaborators.
- Treat benchmark task counts, failure modes, model rankings, voice provider support, licenses, leaderboards and package compatibility as mutable first-party release facts.

## Validation

- Original, dual-control and τ³ tracks are differentiated before any numerical comparison.
- A 1.0.1 banking-knowledge result is not silently compared with an earlier unpatched result.
- The independently maintained benchmark family is not duplicated as evaluation infrastructure software.
- The Sierra producer has a reciprocal `produces` reference.
