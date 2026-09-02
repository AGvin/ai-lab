# Reranking

Legacy residual retained for candidate-budget tuning, staged retrieval evaluation, diversity handling, and downstream-context selection guidance that are intentionally outside the canonical Reranking concept owner.

> **Migration note:** Reranking identity, first-stage retrieval versus reranking boundaries, cross-encoder and alternative reranker families, hybrid-fusion distinction, score non-guarantees, and candidate-recall versus latency/precision trade-offs are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/reranking/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Candidate-budget residual

Tune the initial candidate count and the final retained count separately. A reranker cannot repair first-stage omissions, so candidate generation needs enough recall to contain the required evidence while the reranking stage remains small enough to satisfy latency and cost constraints.

Do not choose one top-k value as a universal default. The useful candidate budget depends on corpus size, retriever quality, reranker cost, query difficulty, and downstream context limits.

## Staged-evaluation residual

Evaluate retrieval stages independently enough to diagnose where failures enter the pipeline:

- measure first-stage recall before reranking;
- measure ordering/precision or another appropriate relevance objective after reranking;
- inspect whether reranking improves the evidence actually passed downstream;
- measure final task quality separately when a generation or decision stage follows retrieval.

Optimizing a reranker metric alone can hide missing first-stage evidence or downstream failures.

## Diversity and context-selection residual

When a task requires evidence from multiple documents, perspectives, sections, or time periods, avoid pruning every supporting passage merely because several candidates discuss the same topic. Distinguish true near-duplicates from complementary evidence before final context selection.

Do not pass every reranked candidate downstream automatically. Apply the concrete application's relevance, diversity, evidence, context-budget, and access constraints after reranking.

These candidate-budget, staged-evaluation, diversity, and context-selection practices remain migration source material until their exact learning, retrieval-engineering, evaluation, or decision-support owners are verified.
