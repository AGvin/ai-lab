# Rerank

Rerank is Cohere’s model family for scoring and reordering candidate documents against a query.

## Identity and provenance

The catalog currently materializes Rerank 4 Pro and Fast as distinct concrete models. Current documentation also describes Rerank 5; those new releases remain zero-credit follow-ups outside this existing-node package. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).

## Decision and operating boundaries

- Reranking consumes an already selected candidate set and query. It is separate from generating document embeddings, maintaining a vector index, fetching sources or generating a final answer. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Version 4 has a 32,768-token query-plus-document window. Context Focus, calibrated relevance labels and the approximate parameter sizes documented for version 5 must not be inherited by version 4. [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- Choose the exact model and service contract, then evaluate ranking quality on representative candidate sets. Model-family membership does not supply one universal score threshold, license or deployment capacity. [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).

## Catalog relations

- [Cohere](../../../../../producers/sub/c/sub/cohere/) — producer.
- [Rerank 4 Fast](sub/models/sub/rerank-v4-0-fast/) — member.
- [Rerank 4 Pro](sub/models/sub/rerank-v4-0-pro/) — member.

## Official resources

- [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank).
- [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).
- [Rerank 5 release discovery](https://docs.cohere.com/v2/changelog/rerank-v5).
- [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
