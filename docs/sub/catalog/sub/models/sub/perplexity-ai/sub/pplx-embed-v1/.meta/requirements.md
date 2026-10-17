# Documentation Requirements

## Requirements

- Identify PPLX Embed V1 as Perplexity AI's current text-embedding model family exposed by the Perplexity Embeddings API.
- Preserve the family split between standard embeddings for independent texts/queries and contextualized embeddings for chunks that share document context.
- Keep concrete parameter class, dimensions, context length, quantization/output format, pooling behavior, model-card artifacts, and serving characteristics with the concrete member or current first-party service documentation.
- Keep Perplexity Embeddings API pricing, quotas, batching, endpoint behavior, and client SDKs outside intrinsic model-family identity.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The family remains distinct from the hosted Embeddings API service.
- Standard and contextualized variants are not silently conflated.
- Producer provenance resolves bidirectionally to Perplexity AI.
