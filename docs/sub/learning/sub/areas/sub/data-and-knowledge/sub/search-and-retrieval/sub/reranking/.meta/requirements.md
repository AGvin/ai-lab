# Documentation Requirements

## Requirements

- Teach Reranking as a second-stage relevance step whose value depends on sufficient first-stage recall and an explicit latency/cost/context budget.
- Tune initial candidate count and final retained count separately; a reranker cannot recover evidence omitted by candidate generation.
- Avoid one universal top-k default. Candidate budgets depend on corpus size, retriever quality, reranker cost, query difficulty, and downstream context limits.
- Evaluate stages separately: first-stage recall, post-reranking ordering/precision, evidence actually passed downstream, and final task quality when a later generation/decision stage exists.
- Distinguish near-duplicates from complementary evidence when a task needs multiple documents, sections, perspectives, or time periods.
- Do not automatically pass every reranked candidate downstream; apply the application's relevance, diversity, evidence, context-budget, and required scope constraints.

## Validation

- Reranker quality does not hide missing first-stage evidence.
- Candidate and retained counts are tuned independently.
- Final context selection can preserve complementary evidence rather than only topical redundancy.
