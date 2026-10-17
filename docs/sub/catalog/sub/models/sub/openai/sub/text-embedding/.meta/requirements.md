# Documentation Requirements

## Requirements

- Identify this family as OpenAI's current text-embedding model line used to map text into vector representations for search, clustering, recommendations, classification, anomaly detection, and related retrieval workflows.
- Materialize the current third-generation `text-embedding-3-large` and `text-embedding-3-small` members because they are the current recommended embedding models.
- Keep `text-embedding-ada-002` as a documented older/current API model but do not materialize it solely for historical completeness while first-party guidance identifies the v3 models as the newest and most performant route.
- Keep embedding endpoint behavior, pricing, batching, regional processing, vector-database integration, and mutable rate limits outside intrinsic family identity.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The family is not conflated with a vector database or the Embeddings API endpoint.
- Current recommended members are represented without materializing every legacy embedding model.
- Producer provenance resolves bidirectionally to OpenAI.
