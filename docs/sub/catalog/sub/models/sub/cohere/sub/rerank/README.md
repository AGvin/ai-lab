# Rerank

Rerank is Cohere’s model family for scoring and reordering candidate documents against a query.

## Identity and provenance

The catalog materializes three separately named Rerank 3.x models (3.5, English 3.0, Multilingual 3.0), Rerank 4 Pro/Fast and separately released Rerank 5 Pro/Fast as seven concrete model identities. Version 5 was announced on 2026-10-21; it is not a serving alias, context setting, or silent rename of version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).

## Decision and operating boundaries

- Reranking consumes an already selected candidate set and query. It is separate from generating document embeddings, maintaining a vector index, fetching sources or generating a final answer. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Version 4 has a 32,768-token query-plus-document window. Context Focus, calibrated relevance labels and the approximate parameter sizes documented for version 5 must not be inherited by version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Choose the exact model and service contract, then evaluate ranking quality on representative candidate sets. Model-family membership does not supply one universal score threshold, license or deployment capacity. [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).

- Rerank 5 Pro (`rerank-v5.0-pro`, approximately 2B parameters) and Fast (`rerank-v5.0-fast`, approximately 500M) are proprietary multilingual text rerankers, released on 2026-10-21. Both offer a 32,768-token model context; Pro prioritizes complex-ranking quality and Fast prioritizes latency and throughput according to Cohere. [Rerank 5 model details](https://docs.cohere.com/docs/rerank) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- Rerank 5 Context Focus is opt-in; scores are calibrated, but application thresholds still require representative validation. The v2 API recommends no more than 1,000 candidates per request for performance, and `max_tokens_per_doc` defaults to 4,096. The current v2 reference does not establish a Rerank 5-specific query-token ceiling. Verify exact endpoint limits; the 32k context is not the default processed document length. [Rerank v2 API reference](https://docs.cohere.com/reference/rerank) [Rerank 5 model details](https://docs.cohere.com/docs/rerank).

- Cohere still lists three Rerank 3.x endpoints: `rerank-v3.5` (multilingual), `rerank-english-v3.0` and `rerank-multilingual-v3.0`, with **4,096-token query-plus-document windows**, unlike the 32k Rerank 4/5 models. Do not infer Rerank 5-specific Context Focus or calibrated-score semantics. [Cohere model inventory](https://docs.cohere.com/docs/models) [Rerank comparison](https://docs.cohere.com/docs/rerank).

## Catalog relations

- [Cohere](../../../../../producers/sub/c/sub/cohere/) — producer.
- [Rerank 3.5](sub/models/sub/rerank-v3-5/) — member.
- [Rerank English 3](sub/models/sub/rerank-english-v3-0/) — member.
- [Rerank Multilingual 3](sub/models/sub/rerank-multilingual-v3-0/) — member.
- [Rerank 4 Fast](sub/models/sub/rerank-v4-0-fast/) — member.
- [Rerank 4 Pro](sub/models/sub/rerank-v4-0-pro/) — member.
- [Rerank 5 Fast](sub/models/sub/rerank-v5-0-fast/) — member.
- [Rerank 5 Pro](sub/models/sub/rerank-v5-0-pro/) — member.

## Official resources

- [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank).
- [Cohere model inventory](https://docs.cohere.com/docs/models).
- [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).
- [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).
- [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
