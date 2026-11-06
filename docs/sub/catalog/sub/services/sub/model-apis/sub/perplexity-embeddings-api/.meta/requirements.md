# Documentation Requirements

## Requirements

- Present Perplexity Embeddings API as Perplexity AI's released hosted API for its standard and contextualized text-embedding models used in semantic search, retrieval, RAG, and related applications.
- Keep concrete PPLX embedding trained-model identities in the model catalog; this service owns hosted endpoint/access behavior rather than intrinsic model architecture.
- Keep Perplexity Search API, Agent API, other orchestration APIs, SDKs, model cards, playground, and client libraries as separate services/access surfaces.
- Treat available model IDs, prices, batching, output encodings/quantization options, dimensions, context limits, endpoint schemas, quotas, and recommended similarity handling as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Embeddings API remains a hosted model-access service rather than a model family.
- Concrete embedding-model facts are not duplicated into mutable service state.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: Perplexity Embeddings API provides hosted access to standard text embeddings and document-context embeddings. The service owns authentication, quotas and request/response behavior; the trained models retain their own catalog identities.
- Decision and deployment boundary: Keep independent inputs separate from grouped document chunks. Match vector dimensions, encoding and similarity function: current guidance uses cosine similarity for unnormalized int8 output and Hamming distance for binary output. Data retention depends on the configured account and applicable API terms.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://docs.perplexity.ai/docs/embeddings/quickstart>, <https://docs.perplexity.ai/docs/resources/privacy-security>.

## Scoped original-source qualification — 2026-11-06

- Perplexity Embeddings API provides hosted text embeddings and grouped-document contextualized embedding generation. This service is distinct from Perplexity Search API and Agent API and from the underlying PPLX embedding model identities. Dimensionality, quantization/encoding, API request groupings and similarity procedures are version-specific.
- Do not mix standard independent texts and document-group embeddings as identical vectors without model-specific guidance, or presume unverified data retention, global rate limits and pricing.
- Verified first-party source 1: https://docs.perplexity.ai/docs/embeddings/quickstart
- Verified first-party source 2: https://docs.perplexity.ai/docs/resources/privacy-security
- This bounded source qualification does not establish a full freshness audit, independently validated runtime, legal/model-license clearance, current pricing or entitlements, global schema/cache/CI/render or final publication.
