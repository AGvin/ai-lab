# Documentation Requirements

## Identity and provenance

- Rerank Multilingual 3 is Cohere's separately documented multilingual, including non-English documents document-reranking model with exact API identifier `rerank-multilingual-v3.0`; it is a separately identified Multilingual 3.0 model, not an English 3.0 option or a Rerank 3.5 alias. Cohere lists it separately alongside other v3.x models and later Rerank 4/5. [Model inventory](https://docs.cohere.com/docs/models) [Rerank comparison](https://docs.cohere.com/docs/rerank).
- This specific v3.x model has **4,096 tokens of context for each combined query and document**, not a generative answer window or the 32k Rerank 4/5 context. It accepts text candidates and may handle semi-structured documents serialized as strings. [Rerank comparison](https://docs.cohere.com/docs/rerank) [Rerank overview](https://docs.cohere.com/docs/rerank-overview).

## Operational decision boundaries

- Rerank reorders a supplied query's candidate documents; it does not index, search an unprovided corpus, embed content, or generate factual answers. Preserve a separate retrieval step and interpret scores within the chosen model. [Overview](https://docs.cohere.com/docs/rerank-overview) [Best practices](https://docs.cohere.com/docs/reranking-best-practices).
- Long candidates are chunked when the query/document budget is exceeded. Check exact endpoint, chunking, query length and candidate-count constraints rather than transferring Rerank 4/5 32k windows. Do not backport version 5 Context Focus, calibrated scoring semantics or Pro/Fast parameter sizes. [Rerank comparison](https://docs.cohere.com/docs/rerank) [Best practices](https://docs.cohere.com/docs/reranking-best-practices).
- The legacy API ID's presence in current documentation is not proof of account/region availability, open downloadable weights, benchmark quality, pricing, rate-limit eligibility, or a separate corporate producer. Investigate before new integrations. [Model inventory](https://docs.cohere.com/docs/models) [Rerank comparison](https://docs.cohere.com/docs/rerank).
- No definitive model-training ancestry, ownership percentages or Russian control links were established by this scoped source review. Do not claim derived-from relationships or assign risk tiers without current company evidence.

## Validation

- Keep one canonical model ID and exactly one inverse family membership; reject alias, API mode, train-parent, and producer duplicates.
- The complete reader must preserve language scope, exact API identifier, combined 4k context, operational limits and relation/link integrity.
- No actual endpoint inference, global freshness audit, full schema/cache/CI, clean research pass or publication gate credit from this bounded intake.
