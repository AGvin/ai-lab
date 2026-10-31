# Documentation Requirements

## Identity and provenance

- Rerank is Cohere’s model family for scoring and reordering candidate documents against a query.
- The catalog materializes Rerank 4 Pro/Fast and the separately released Rerank 5 Pro/Fast as four distinct concrete model identities. Version 5 was announced on 2026-10-21; it is not a serving alias, context setting, or silent rename of version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).

## Operational decision boundaries

- Reranking consumes an already selected candidate set and query. It is separate from generating document embeddings, maintaining a vector index, fetching sources or generating a final answer. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Version 4 has a 32,768-token query-plus-document window. Context Focus, calibrated relevance labels and the approximate parameter sizes documented for version 5 must not be inherited by version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Choose the exact model and service contract, then evaluate ranking quality on representative candidate sets. Model-family membership does not supply one universal score threshold, license or deployment capacity. [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).

- Rerank 5 Pro (`rerank-v5.0-pro`, approximately 2B parameters) and Fast (`rerank-v5.0-fast`, approximately 500M) are proprietary text rerankers with a 32,768-token query-plus-document model context, 100+ supported languages and optional Context Focus. The quality-versus-latency positioning comes from Cohere, not independent AI Lab benchmarking. [Rerank 5 model details](https://docs.cohere.com/docs/rerank) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- The Rerank 5 endpoint accepts up to 10,000 candidates but truncates a long document according to `max_tokens_per_doc` (default 4,096), and supports at most 2,048 query tokens under current best practices. The model context ceiling must not be mistaken for an unconditionally processed 32k document. Context Focus is opt-in and its character spans must be applied to the original document. [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 5 model details](https://docs.cohere.com/docs/rerank).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
