# Rerank

Rerank is Cohere’s model family for scoring and reordering candidate documents against a query.

## Identity and provenance

The catalog materializes Rerank 4 Pro/Fast and the separately released Rerank 5 Pro/Fast as four distinct concrete model identities. Version 5 was announced on 2026-10-21; it is not a serving alias, context setting, or silent rename of version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).

## Decision and operating boundaries

- Reranking consumes an already selected candidate set and query. It is separate from generating document embeddings, maintaining a vector index, fetching sources or generating a final answer. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Version 4 has a 32,768-token query-plus-document window. Context Focus, calibrated relevance labels and the approximate parameter sizes documented for version 5 must not be inherited by version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Choose the exact model and service contract, then evaluate ranking quality on representative candidate sets. Model-family membership does not supply one universal score threshold, license or deployment capacity. [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).

- Rerank 5 Pro (`rerank-v5.0-pro`, approximately 2B parameters) and Fast (`rerank-v5.0-fast`, approximately 500M) are proprietary multilingual text rerankers, released on 2026-10-21. Both offer a 32,768-token model context; Pro prioritizes complex-ranking quality and Fast prioritizes latency and throughput according to Cohere. [Rerank 5 model details](https://docs.cohere.com/docs/rerank) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- Rerank 5 Context Focus is opt-in; scores are calibrated, but application thresholds still require representative validation. The endpoint limits candidates to 10,000 per call, defaults to 4,096 tokens per document and allows up to 2,048 query tokens. Do not equate the maximum context window with the default processed document length. [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 5 model details](https://docs.cohere.com/docs/rerank).

## Catalog relations

- [Cohere](../../../../../producers/sub/c/sub/cohere/) — producer.
- [Rerank 4 Fast](sub/models/sub/rerank-v4-0-fast/) — member.
- [Rerank 4 Pro](sub/models/sub/rerank-v4-0-pro/) — member.
- [Rerank 5 Fast](sub/models/sub/rerank-v5-0-fast/) — member.
- [Rerank 5 Pro](sub/models/sub/rerank-v5-0-pro/) — member.

## Official resources

- [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank).
- [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).
- [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).
- [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
