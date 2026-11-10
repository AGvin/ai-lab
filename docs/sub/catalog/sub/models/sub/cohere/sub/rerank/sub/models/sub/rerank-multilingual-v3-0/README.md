# Rerank Multilingual 3

Rerank Multilingual 3 is Cohere's separately listed **multilingual, including non-English documents** document-reranking model, identified by `rerank-multilingual-v3.0`. It is a separately identified Multilingual 3.0 model, not an English 3.0 option or a Rerank 3.5 alias. [Cohere model inventory](https://docs.cohere.com/docs/models) [Rerank comparison](https://docs.cohere.com/docs/rerank).

## Identity and provenance

The v3.x model has a **4,096-token context shared between each query and candidate document**. This is not the Rerank 4/5 32k window and does not imply chat generation or embeddings. Cohere identifies this API model separately in its current Rerank table. [Rerank comparison](https://docs.cohere.com/docs/rerank) [Cohere model inventory](https://docs.cohere.com/docs/models).

## Decision and operating boundaries

- Supply search candidates from an existing index or search engine, then let the Rerank endpoint reorder them. It does not perform retrieval, vectorization or answer generation. [Rerank overview](https://docs.cohere.com/docs/rerank-overview).
- Documents exceeding the combined query/document context can be chunked under the provider's service contract. Verify preprocessing, model-specific limits and output relevance empirically. [Rerank comparison](https://docs.cohere.com/docs/rerank) [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices).
- Do not assume v4/v5 32k context, Rerank 5 Context Focus or calibrated-score capabilities, v5 parameter sizes, freely downloadable weights, common training parents or interoperable scores for this earlier-generation model. [Cohere model inventory](https://docs.cohere.com/docs/models) [Rerank comparison](https://docs.cohere.com/docs/rerank).
- Check active account/platform access, prices and rate limits before selecting a previous-generation reranker for new work. No independent inference, ranking benchmark or ownership audit was performed.

## Catalog relations

- [Rerank](../../../../) — model family.

## Official resources

- [Cohere model inventory](https://docs.cohere.com/docs/models).
- [Cohere Rerank comparison](https://docs.cohere.com/docs/rerank).
- [Rerank overview](https://docs.cohere.com/docs/rerank-overview).
- [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices).
