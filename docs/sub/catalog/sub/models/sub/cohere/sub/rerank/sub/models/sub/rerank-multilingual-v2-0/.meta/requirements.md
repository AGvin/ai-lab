# Documentation Requirements

## Identity and provenance

- Rerank Multilingual v2 is Cohere's independently named historical multilingual text document-reranking model, with exact API ID `rerank-multilingual-v2.0`. Keep it distinct from the other v2 language model, the separately named v3 models and newer Rerank 4/5; a language setting or endpoint alias is not a new learned identity. [Cohere lifecycle record](https://docs.cohere.com/docs/deprecations).
- Cohere announced v2 deprecation on **2024-12-02** and shut down this original hosted model on **2025-04-30**. Requests to shut-down models fail. Display an explicit unavailable/historical warning immediately below the title and do not recommend this API model for new integrations. [Cohere lifecycle record](https://docs.cohere.com/docs/deprecations).

## Operational decision boundaries

- Preserve the text query/candidate-document reranking boundary: this is a second-stage relevance model, not an embedding model, corpus index, search engine or answer generator. Existing search infrastructure supplies the candidates. [Original Rerank launch](https://cohere.com/blog/rerank) [Current Rerank explanation](https://docs.cohere.com/docs/rerank).
- The v2 retirement entry recommends Rerank 3.5 as the replacement at that announcement. That dated migration advice is not a current universal ranking; choose an available model and evaluate relevance, latency, API limits and score thresholds for the workload. Updating a reranker does not itself require regenerating embedding vectors, since reranking consumes candidate text rather than a model-specific stored embedding space. [Lifecycle record](https://docs.cohere.com/docs/deprecations) [Rerank explanation](https://docs.cohere.com/docs/rerank).
- The December 2024 entry originally excluded fine-tuned derivatives from that specific base-model deprecation. Do not present this as continuing availability: Cohere separately retired all fine-tuning access, including previously fine-tuned Rerank models, effective **2025-09-15**. Do not create speculative fine-tuned model identities. [Lifecycle record](https://docs.cohere.com/docs/deprecations).
- Do not inherit v3 4k or v4/v5 32k context, current endpoint document limits, v5 Context Focus/calibrated scores, approximate v5 parameters or downloadable/open-weight rights. Exact historical v2 context, parameters, training parent and current third-party deployments are not established by this review.
- Cohere is the existing family producer. Beneficial ownership and indirect current Russian share/control links remain unverified by this bounded review; names or publishing accounts do not prove control. No new producer, sanctions finding or ownership risk tier is asserted.

## Validation

- Retain one canonical model ID and one reciprocal family membership. Project the complete identity, retirement dates, warning and historical fine-tuning boundary into the reader.
- Resolve all local reader links. No endpoint call, independent ranking benchmark, downloaded-weight execution, global cache/schema/CI, full ownership audit, clean research cycle or publication-gate credit.
