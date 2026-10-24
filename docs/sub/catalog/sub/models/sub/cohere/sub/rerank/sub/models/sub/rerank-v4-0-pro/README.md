# Rerank 4 Pro

Rerank 4 Pro is Cohere’s document-reranking model positioned for quality-sensitive and complex ranking tasks.

## Identity and provenance

The release explicitly identifies rerank-v4.0-pro. Current documentation lists it alongside the newer Rerank 5 models; a newer release does not silently change this node’s identity. [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank).

## Decision and operating boundaries

- The version 4 window is 32,768 tokens for query and document together; the service reserves four tokens and chunks longer documents. Its documented document score uses the most relevant chunk, so chunk boundaries and candidate preparation affect interpretation. [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- The model supports multilingual text and semi-structured documents. The API guidance serializes structured input deliberately; version 4 scores are query-dependent relevance values rather than universal probabilities or calibrated relevance classes. Do not backport version 5 Context Focus or score labels. [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank) [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
- The Pro performance role is Cohere’s positioning, not a locally measured comparison. Current public sources establish no open-weight license or parameter total for version 4; the version 5 size estimates do not describe this model. [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0) [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank).
- Reranking does not retrieve an unseen corpus or produce a grounded answer by itself. The application supplies candidates, handles endpoint limits, selects cutoffs and validates search outcomes. [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).

## Catalog relations

- [Rerank](../../../../) — series or family.

## Official resources

- [Rerank model comparison](https://docs.cohere.com/v2/docs/rerank).
- [Rerank 4 release](https://docs.cohere.com/changelog/rerank-v4.0).
- [Rerank best practices and score boundaries](https://docs.cohere.com/docs/reranking-best-practices).
