# Documentation Requirements

## Requirements

- Identify Redis Agent Memory as Redis's managed memory service for AI applications and agents, available as a managed service on Redis Cloud.
- Preserve its primary identity as persistent agent/application memory with session memory, long-term memory, automatic summarization/extraction, retrieval, and a service API rather than as a generic Redis database profile.
- Keep Redis Iris as the broader context-engine product boundary: Agent Memory is one component/capability within Iris, but current Redis documentation also exposes Agent Memory as an independently provisioned managed service with its own setup and API surface.
- Preserve the deployment distinction: Redis Cloud Agent Memory is a released managed service, while current self-managed Redis Software deployment is still private preview and does not independently justify a separate current software identity.
- Keep the original Agent Memory Server V0 research artifact distinct from the maintained Redis Agent Memory service API; the current upstream README says V0 is not the supported production distribution.
- Treat supported SDKs, REST endpoints, model configuration, retention, limits, pricing, availability, deployment options, and framework integrations as freshness-sensitive.
- Keep underlying Redis Search/vector/indexing mechanisms as implementation details when memory/context is the primary product identity.

## Validation

- Redis Agent Memory remains classified under managed memory/context services rather than generic vector search or databases.
- Producer provenance resolves bidirectionally to Redis.
- Private-preview self-managed deployment is not misreported as a generally available self-managed product.
- The Agent Memory Server V0 research artifact is not conflated with the current managed production service.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Redis Agent Memory is Redis's managed memory service for AI applications and agents. It provides session state and longer-term memory, with extraction, summarization and retrieval features exposed through a service API. Current Redis documentation places it within the Iris context engine while giving Agent Memory its own service setup and SDK/API surface. [Agent Memory overview](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/) · [Cloud service guide](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory/).

The Redis Cloud deployment is managed; the Redis Software deployment is documented as private preview. Choose the available deployment and model configuration before planning production use, and define which events or memories may persist, who may retrieve them and when they should expire or be deleted. Memory extraction is an application data-processing step, so its configured model and access boundaries matter. [Deployment and model guidance](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/) · [Service administration](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory/).

The original Agent Memory Server now lives under the upstream repository's V0 research material and is not the supported production distribution. Its Apache-2.0 repository license does not establish the managed service's contract. Redis also distinguishes its published research evaluation configurations from the shipping service; benchmark results require the exact provider version, models and protocol. [Repository and V0 boundary](https://github.com/redis/agent-memory-server).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
