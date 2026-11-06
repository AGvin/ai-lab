# Documentation Requirements

## Identity and provenance

- Rerank is Cohere’s model family for scoring and reordering candidate documents against a query.
- The catalog materializes three separately named Rerank 3.x models (3.5, English 3.0, Multilingual 3.0), Rerank 4 Pro/Fast and separately released Rerank 5 Pro/Fast as seven concrete current-generation/previous-generation model identities, plus two separately identified retired v2 models (English and Multilingual), for nine materialized concrete models. Version 5 was announced on 2026-10-21; it is not a serving alias, context setting, or silent rename of version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).

## Operational decision boundaries

- Historical `rerank-english-v2.0` and `rerank-multilingual-v2.0` were deprecated on 2024-12-02 and shut down on 2025-04-30. Retain them for migration/history only, with explicit unavailability warnings; no new-integration recommendation or transfer of newer generation capabilities. The old fine-tune exception does not survive the separately announced 2025-09-15 retirement of all fine-tuning access. [Cohere lifecycle record](https://docs.cohere.com/docs/deprecations).

- Reranking consumes an already selected candidate set and query. It is separate from generating document embeddings, maintaining a vector index, fetching sources or generating a final answer. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Version 4 has a 32,768-token query-plus-document window. Context Focus, calibrated relevance labels and the approximate parameter sizes documented for version 5 must not be inherited by version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Choose the exact model and service contract, then evaluate ranking quality on representative candidate sets. Model-family membership does not supply one universal score threshold, license or deployment capacity. [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).

- Rerank 5 Pro (`rerank-v5.0-pro`, approximately 2B parameters) and Fast (`rerank-v5.0-fast`, approximately 500M) are proprietary text rerankers with a 32,768-token query-plus-document model context, 100+ supported languages and optional Context Focus. The quality-versus-latency positioning comes from Cohere, not independent AI Lab benchmarking. [Rerank 5 model details](https://docs.cohere.com/docs/rerank) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- The v2 Rerank API recommends not sending more than 1,000 candidates per request for performance and defaults `max_tokens_per_doc` to 4,096, truncating long documents. The general best-practices table lists a 10,000-document ceiling, but the current v2 reference does not specify a Rerank 5-specific query-token ceiling; verify account and deployment limits rather than inheriting older-model limits. Context Focus is opt-in and character spans apply to original input. [Rerank v2 API reference](https://docs.cohere.com/reference/rerank) [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 5 model details](https://docs.cohere.com/docs/rerank).

- Earlier Rerank 3.x identities `rerank-v3.5`, `rerank-english-v3.0` and `rerank-multilingual-v3.0` each use **4,096 query-plus-document tokens**. Version 3.5 is multilingual, while version 3.0 has distinct English and multilingual models. This is not a 32k Rerank 4/5 setting, new producer, or Rerank 5 Context Focus/calibrated-score feature. [Cohere model inventory](https://docs.cohere.com/docs/models) [Rerank comparison](https://docs.cohere.com/docs/rerank) [Rerank overview](https://docs.cohere.com/docs/rerank-overview).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
