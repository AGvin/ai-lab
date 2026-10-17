# Documentation Requirements

## Requirements

- Identify Redis Agent Memory as Redis's managed memory service for AI applications and agents, available as a managed service on Redis Cloud.
- Preserve its primary identity as persistent agent/application memory with session memory, long-term memory, automatic summarization/extraction, retrieval, and a service API rather than as a generic Redis database profile.
- Keep Redis Iris as the broader context-engine product boundary: Agent Memory is one component/capability within Iris, but current Redis documentation also exposes Agent Memory as an independently provisioned managed service with its own setup and API surface.
- Preserve the deployment distinction: Redis Cloud Agent Memory is a released managed service, while current self-managed Redis Software deployment is still private preview and does not independently justify a separate current software identity.
- Keep the deprecated open-source Agent Memory Server backend distinct from the maintained Redis Agent Memory Data Plane API and do not present the deprecated server as the current canonical product.
- Treat supported SDKs, REST endpoints, model configuration, retention, limits, pricing, availability, deployment options, and framework integrations as freshness-sensitive.
- Keep underlying Redis Search/vector/indexing mechanisms as implementation details when memory/context is the primary product identity.

## Validation

- Redis Agent Memory remains classified under managed memory/context services rather than generic vector search or databases.
- Producer provenance resolves bidirectionally to Redis.
- Private-preview self-managed deployment is not misreported as a generally available self-managed product.
- Deprecated Agent Memory Server documentation is not conflated with the current managed service.
