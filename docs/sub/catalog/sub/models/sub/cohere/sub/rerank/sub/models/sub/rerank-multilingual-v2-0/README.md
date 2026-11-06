# Rerank Multilingual v2

> **Historical — hosted API unavailable.** Cohere shut down `rerank-multilingual-v2.0` on **30 April 2025**. Do not select this API model for new integrations. [Lifecycle record](https://docs.cohere.com/docs/deprecations).

Rerank Multilingual v2 is Cohere's separately identified historical **multilingual text reranker**. It scores and reorders supplied candidate documents for a query. It is distinct from the other v2 language model and later Rerank generations. [Cohere lifecycle record](https://docs.cohere.com/docs/deprecations).

## Lifecycle and migration

- **2 December 2024:** Cohere announced Rerank v2 deprecation and recommended Rerank 3.5 at that time.
- **30 April 2025:** the original hosted v2 model shut down; requests to shut-down models fail.
- **15 September 2025:** Cohere separately retired fine-tuning access, including previously fine-tuned Rerank models. The older v2 announcement's fine-tune exception is not proof of continuing availability. [Lifecycle record](https://docs.cohere.com/docs/deprecations).

These dates describe Cohere's hosted API. This review establishes no currently available third-party deployment or downloadable-weight license.

## Decision and operating boundaries

Supply candidates from an existing search system. Reranking compares the query with candidate text; it does not create embeddings, index a corpus or generate an answer. Replacing the reranker does not itself require re-embedding the existing index. Evaluate the selected replacement's relevance, latency, input handling and score thresholds on representative data. [Original Rerank launch](https://cohere.com/blog/rerank) [Rerank explanation](https://docs.cohere.com/docs/rerank).

The dated 3.5 replacement advice is not a current universal winner. Do not copy later generations' 4k/32k context, Context Focus, calibrated scores, parameter sizes or current API document limits onto v2. Exact historical context and parameters remain unspecified here rather than guessed.

Cohere remains the existing family producer. This scoped review establishes neither a concrete training parent nor complete beneficial ownership, indirect Russian stakes/control, independent benchmarks or operational inference.

## Catalog relations

- [Rerank](../../../../) — model family.

## Official resources

- [Cohere lifecycle and shutdown record](https://docs.cohere.com/docs/deprecations).
- [Original Rerank launch](https://cohere.com/blog/rerank).
- [Rerank explanation and current comparison](https://docs.cohere.com/docs/rerank).
