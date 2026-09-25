# Documentation Requirements

## Requirements

- Present Perplexity Embeddings API as Perplexity AI's released hosted API for its standard and contextualized text-embedding models used in semantic search, retrieval, RAG, and related applications.
- Keep concrete PPLX embedding trained-model identities in the model catalog; this service owns hosted endpoint/access behavior rather than intrinsic model architecture.
- Keep Perplexity Search API, Agent API, Router API, SDKs, model cards, playground, and client libraries as separate services/access surfaces.
- Treat available model IDs, prices, batching, output encodings/quantization options, dimensions, context limits, endpoint schemas, quotas, and recommended similarity handling as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Embeddings API remains a hosted model-access service rather than a model family.
- Concrete embedding-model facts are not duplicated into mutable service state.
- Producer provenance resolves bidirectionally to Perplexity AI.
