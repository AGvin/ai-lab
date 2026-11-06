# Rerank 5 Fast

Rerank 5 Fast is Cohere's proprietary multilingual text reranking model, released on 2026-10-21. The Cohere API model ID is `rerank-v5.0-fast`; this is a distinct Rerank 5 tier, not a Rerank 4 alias.

## Identity and provenance

Cohere's public documentation estimates ~500M parameters and a 32,768-token combined query/document model context. Reviewed sources do not establish downloadable unrestricted weights or a public open-weight license, and do not prove any trained-from relationship with another Rerank model. [Rerank 5 release](https://docs.cohere.com/v2/changelog) [Rerank model details](https://docs.cohere.com/docs/rerank).

## Decision and operating boundaries

- This model reorders a supplied candidate set; it does not index, fetch unseen documents, embed a corpus or independently verify an answer. Cohere reports 100+ supported languages and text-only inputs, including JSON/tables serialized into YAML-style strings. [Rerank model details](https://docs.cohere.com/docs/rerank).
- The v2 API recommends no more than 1,000 candidate documents per request for performance; `max_tokens_per_doc` defaults to 4,096 and truncates long input. The current Rerank 5-specific query-token limit is not stated in the v2 reference; verify target deployment constraints rather than assuming the older-model 2,048 limit. The 32k context is not the default processed document length. [Rerank v2 API reference](https://docs.cohere.com/reference/rerank) [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices).
- Context Focus is optional (disabled by default) via `relevant_spans` and returns passage character offsets plus scores for original input. Calibrated scores range from 0 to 1, but user-defined cutoffs require validation and are not proof of factual correctness. The documented spans feature is available via Cohere API; verify other deployment surfaces separately. [Rerank model details](https://docs.cohere.com/docs/rerank) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- Cohere positions this tier for latency-sensitive search, high-throughput workflows and repeated agent searches. This is provider positioning, not an AI Lab benchmark.
- Providers include Cohere API, Model Vault, Microsoft Foundry and SageMaker, with private options subject to agreement; verify current region/account, endpoint rights, latency and price. Do not assume Amazon Bedrock parity or a universal score threshold. [Rerank 5 release](https://docs.cohere.com/v2/changelog) [Rerank model details](https://docs.cohere.com/docs/rerank).
- Migrating from Rerank 4 does not by itself require re-embedding an existing indexed corpus, but candidate preprocessing, scoring thresholds, downstream answer quality and user-data obligations require testing. Public comparative results are publisher claims, not independent reproduction. Current beneficial ownership and any partial Russian control were not independently determined in this review. [Rerank 5 release](https://docs.cohere.com/v2/changelog).

## Catalog relations

- [Rerank](../../../../) — family.

## Official resources

- [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- [Rerank model details](https://docs.cohere.com/docs/rerank).
- [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices).
