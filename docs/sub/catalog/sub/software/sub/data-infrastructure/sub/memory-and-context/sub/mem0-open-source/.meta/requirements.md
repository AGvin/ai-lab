# Documentation Requirements

## Requirements

- Present Mem0 Open Source as the self-managed/open-source Mem0 memory engine, distinct from the producer-operated Mem0 Platform service.
- Keep library and self-hosted-server delivery as deployment forms of the same software identity.
- Keep memory storage/server ownership distinct from configured LLM and embedding providers: current library and self-hosted-server defaults use OpenAI for these operations, so self-managed storage does not imply an entirely local processing path.
- Treat vector stores, graph services, embeddings, rerankers, model/provider support, package versions, and deployment requirements as freshness-sensitive implementation details.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Mem0 Open Source remains under self-managed memory/context software rather than the managed service owner.
- Producer provenance resolves to Mem0.
