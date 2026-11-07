# Documentation Requirements

## Requirements

- Present τ-bench as Sierra's maintained released family of realistic tool-agent-user evaluation benchmarks, with user-simulated dialogue, domain policy compliance, structured tools, and state- or task-grounded grading rather than a generic agent framework or customer-service software product.
- Preserve versioned evaluation identities without duplicating the shared benchmark family: original τ-bench (2024), τ²-bench dual-control user and agent tool actions (2025), and τ³-bench knowledge retrieval and full-duplex voice variants (2026). Distinguish the text, knowledge and voice tracks and their evaluation setups.
- Note that the **2026-07-22 v1.0.1** grading update repairs `banking_knowledge` tasks and changes affected benchmark scores compared with pre-v1.0.1 definitions; require pinned task and grading revisions before comparing scores across releases or leaderboard snapshots.
- Keep domains such as airline, retail, telecom and banking knowledge, policies, synthetic users, tool permissions and retrieval/voice simulation constraints aligned with the first-party benchmark documentation. Do not conflate the benchmark repository's install/CLI/harness APIs with immutable dataset identity.
- Preserve Sierra as source steward/producer, distinguished from models submitted to the benchmark and from independent research collaborators.
- Treat benchmark task counts, failure modes, model rankings, voice provider support, licenses, leaderboards and package compatibility as mutable first-party release facts.

- Render the identity, provenance and operational context recorded in canonical `entity.identity_note`; keep version-sensitive claims and official resources aligned with the cited first-party sources.

- Render the standard `entity-relations` block from validated current-entity relations, ordered by explicit numeric order, target canonical name and target ID; resolve every visible target to its reader.

- Distinguish current 2.0 multilingual text/voice definitions from the 1.x leaderboard: English tasks, prompts and grading changed, and 2.0 scores are not comparable to 1.x. Use v1.0.1 for legacy comparisons and retain its banking-knowledge correction boundary.

## Validation

- Original, dual-control and τ³ tracks are differentiated before any numerical comparison.
- A 1.0.1 banking-knowledge result is not silently compared with an earlier unpatched result.
- The independently maintained benchmark family is not duplicated as evaluation infrastructure software.
- The Sierra producer has a reciprocal `produces` reference.

## Scoped original-source qualification — 2026-11-08

- **τ-bench** is **Sierra**'s benchmark family for language-model agents carrying out simulated customer-service dialogues with policy instructions, tools, user simulation and task-state evaluation. The original `sierra-research/tau-bench` repository warns that its **airline/retail tasks are outdated**; the maintained `sierra-research/tau2-bench` project contains τ², τ³ and current **τ-bench 2.0** family evolution, not independently countable duplicate canonical datasets.
- The maintainer's **2.0** release adds six-language text/voice evaluation and new/revised task definitions and grading, and explicitly separates these results from the **1.x** leaderboard; compare legacy setups against **v1.0.1** where the authors direct. Even within one release, user-simulator, policy state, agent tools, trial count, language and judge/scoring changes affect comparability; replaying no agent task here.
- Original publisher sources: https://github.com/sierra-research/tau-bench ; https://github.com/sierra-research/tau2-bench ; https://taubench.com/
- Bounded credit applies to canonical benchmark-family provenance, status and public release/protocol distinctions only. No actual model/tool/voice test, complete task licensing, current leaderboard audit, independent safety or legal review, repository-wide schema/cache/CI/render, clean or final gate.
