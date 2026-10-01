# Documentation Requirements

## Requirements

- Identify Pinecone as the producer identity for the Pinecone managed vector/search service.
- Keep producer identity distinct from the service entity and from third-party model/integration providers used through Pinecone.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- `produces` is the inverse of Pinecone service `produced-by`.
- Producer references are current first-party sources.
