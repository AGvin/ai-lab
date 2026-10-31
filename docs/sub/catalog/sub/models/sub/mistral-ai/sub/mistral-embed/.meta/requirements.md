# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Mistral Embed as Mistral AI's general embedding model line and materialize the currently available Mistral Embed 2312 checkpoint.
- Keep code-specific Codestral Embed under Codestral rather than treating it as the same embedding model identity.
- Treat context, embedding dimensions, batching, pricing, lifecycle, and API alias behavior as freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.

## Source-backed profile

- Required reader orientation: Mistral Embed is Mistral AI’s general text-embedding model line.
- Preserve this model-scoped fact: The represented 2312 checkpoint returns numerical text representations for retrieval and similarity. Code-specific Codestral Embed remains a distinct identity. [Text embedding contract](https://docs.mistral.ai/studio/knowledge-rag/embeddings/text_embeddings) [Code embedding dimensions and types](https://docs.mistral.ai/studio/knowledge-rag/embeddings/code_embeddings)

## Operational and interpretation boundaries

- Explain this boundary: An embedding is a representation, not a generated answer, correctness assessment or access-control rule. Model and vector configuration must match across indexing and queries.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
