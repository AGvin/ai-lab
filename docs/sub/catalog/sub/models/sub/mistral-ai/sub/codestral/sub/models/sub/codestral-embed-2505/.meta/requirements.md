# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Codestral Embed 2505 as Mistral's GA code-embedding checkpoint for semantic representation of code.
- Preserve embedding context, output dimension/type controls, batching, and evaluation guidance only at exact first-party model scope.
- Treat pricing, API aliases, lifecycle, and downstream retrieval integrations as freshness-sensitive.

## Validation

- Membership resolves to Codestral.

## Source-backed profile

- Required reader orientation: Codestral Embed 2505 is Mistral AI’s code-embedding model, released on May 28, 2025.
- Preserve this model-scoped fact: The GA Premier release `codestral-embed-2505` accepts an 8K-token context and produces vectors through the embeddings API. [Codestral Embed 2505 model card](https://docs.mistral.ai/models/codestral-embed-25-05)
- Preserve this model-scoped fact: The `codestral-embed` interface supports vectors up to 3,072 dimensions and provides `output_dimension` and `output_dtype` controls. [Code embedding dimensions and types](https://docs.mistral.ai/studio/knowledge-rag/embeddings/code_embeddings)

## Operational and interpretation boundaries

- Explain this boundary: Indexing and query vectors must use the same model, dimension and encoding. Dimension changes require a compatible index; code embeddings are not generated source code or a proof of semantic equivalence. [Code embedding dimensions and types](https://docs.mistral.ai/studio/knowledge-rag/embeddings/code_embeddings)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
