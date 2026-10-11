# Documentation Requirements

## Requirements

- Identify Weaviate Database as released open-source/self-managed vector search infrastructure for similarity search, hybrid retrieval, and vector-powered AI applications.
- Preserve canonical ownership under `software/data-infrastructure/vector-search`. Distinguish the database from the provider-operated `services/data-infrastructure/vector-search/weaviate-cloud` identity.
- Describe Docker, Kubernetes, and cloud-provider self-managed installation choices as deployments of the same database rather than different products.
- Do not promote experimental embedded clients, SDK language packages, agent features, or integrations into peer database identities without independent material lifecycle evidence.
- Use current official Weaviate documentation and code repository as the evidence for released indexing, hybrid search, model integrations, schema, backup, clustering, security, and compatibility claims.
- Keep release-specific APIs, telemetry/security defaults, resource needs, performance, and deployment support freshness-sensitive.
- Preserve the producer relation to Weaviate, with a matching inverse relation.

## Validation

- Weaviate Database is distinct from managed Weaviate Cloud.
- The `produced-by` relation resolves to `catalog/producers/w/weaviate` and has a reciprocal `produces`.
- Local/self-hosted deployment options are accurately classified as software deployment modes.
- Product claims and official references remain source-backed.
