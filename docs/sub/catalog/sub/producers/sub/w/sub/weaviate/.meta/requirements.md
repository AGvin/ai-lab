# Documentation Requirements

## Requirements

- Identify Weaviate as the producer identity for Weaviate products represented in the catalog.
- Keep Weaviate Cloud distinct from self-managed/open-source Weaviate Database when both are materialized.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- `produces` relations for Weaviate Cloud and Weaviate Database both invert their respective `produced-by` relations.
