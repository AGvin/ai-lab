# Documentation Requirements

## Identity and provenance

- Rerank 5 Fast is Cohere's separately named proprietary text-reranking model, announced on 2026-10-21. Its exact Cohere API identifier is `rerank-v5.0-fast`, distinct from the other Rerank 5 tier and Rerank 4. [Rerank 5 release](https://docs.cohere.com/v2/changelog) [Rerank model details](https://docs.cohere.com/docs/rerank).
- Cohere estimates about 500 million parameters for this tier and does not publish a general open-weight license in the reviewed primary materials. An API identifier or private deployment offering is not evidence of downloadable unrestricted weights, a training parent or license portability. [Rerank model details](https://docs.cohere.com/docs/rerank).

## Operational decision boundaries

- Rerank 5 ranks an application-supplied candidate list by relevance to the query; it does not retrieve an unseen corpus, embed documents for indexing, or synthesize a grounded response. The modality is text; the shared model context is 32,768 tokens combining query and document, with 100+ languages. JSON, records and tables are passed as formatted text/YAML strings, not native multimodal input. [Rerank model details](https://docs.cohere.com/docs/rerank).
- The current v2 Rerank API recommends no more than 1,000 candidates per request for performance. `max_tokens_per_doc` defaults to 4,096 and truncates longer input; the v2 reference does not specify a Rerank 5-specific query-token ceiling. Confirm the target deployment's limits instead of inheriting older-model caps. The 32k model context is not the default processed document size. [Rerank v2 API reference](https://docs.cohere.com/reference/rerank) [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices).
- Optional Context Focus returns scored relevant passages as character offsets into original input when `relevant_spans` is enabled; it is off by default and described for Cohere API access. Calibrated relevance scores are 0–1 ranking outputs, not independent guarantees that a passage is factually true; thresholds require local evaluation and do not license instruction-style relevance overrides. [Rerank model details](https://docs.cohere.com/docs/rerank) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- Cohere positions Fast for lower-latency, higher-throughput and more cost-sensitive retrieval; no independent AI Lab measurement establishes a deployment-wide speed or quality ratio. Availability differs across Cohere API, Model Vault, Microsoft Foundry, SageMaker, North and negotiated private deployments. Check endpoint/account eligibility, limits, data residency and current contract separately; do not infer Amazon Bedrock availability or universally supported Context Focus from platform names. [Rerank model details](https://docs.cohere.com/docs/rerank) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- Existing 4.0 rankings are not schema-equivalent in scoring calibration or Context Focus. Re-ranking uses original candidate text at query time, so a version change need not rebuild a vector index, but relevance thresholds and downstream LLM quality still require evaluation on the target dataset. [Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices) [Rerank 5 release](https://docs.cohere.com/v2/changelog).
- Publisher benchmark/throughput claims are not independent evaluation, no runtime workload was executed, and ultimate beneficial ownership was not independently audited here; do not invent Russian-origin/control classification from names or rumors.

## Validation

- Preserve this unique canonical entity ID and exact source-backed Cohere API model identifier; keep one reciprocal Rerank has-member/member-of pair, with no invented derived-from edge.
- Render a complete English reader conveying limits, optionality, provenance, license and decision impact; resolve every local reader link.
- This scoped source review provides no download, inference, benchmark, global cache/schema, full research-clean-cycle, final-rendering or final-gate credit.
