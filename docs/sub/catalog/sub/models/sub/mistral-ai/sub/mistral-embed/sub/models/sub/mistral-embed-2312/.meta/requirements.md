# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Mistral Embed 2312 as the current GA general embedding checkpoint exposed by Mistral's embeddings API.
- Preserve context, batching, embedding behavior, and use-case guidance only at exact first-party model scope.
- Treat pricing, lifecycle, and API alias behavior as freshness-sensitive.

## Validation

- Membership resolves to Mistral Embed.

## Source-backed profile

- Required reader orientation: Mistral Embed 2312 is Mistral AI’s general text-embedding model, released in December 2023.
- Preserve this model-scoped fact: The model card lists the GA Premier identifier `mistral-embed-2312` and an 8K-token context. [Mistral Embed model card](https://docs.mistral.ai/models/mistral-embed-23-12)
- Preserve this model-scoped fact: The `mistral-embed` interface produces a 1,024-dimensional vector for each text input. [Text embedding contract](https://docs.mistral.ai/studio/knowledge-rag/embeddings/text_embeddings)

## Operational and interpretation boundaries

- Explain this boundary: Keep document and query embeddings in the same model space and dimension. Similarity is a retrieval signal, not an accuracy or access-control decision. [Text embedding contract](https://docs.mistral.ai/studio/knowledge-rag/embeddings/text_embeddings)
- Explain this boundary: Codestral Embed’s code specialization and configurable output dimensions do not transfer to this checkpoint.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
