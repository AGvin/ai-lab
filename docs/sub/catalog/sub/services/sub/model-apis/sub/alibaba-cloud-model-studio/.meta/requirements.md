# Documentation Requirements

## Requirements

- Identify Alibaba Cloud Model Studio as Alibaba Cloud's managed model-service platform providing Qwen and supported third-party models through managed APIs, including OpenAI-compatible access, without requiring users to operate inference infrastructure.
- Preserve its primary model-API/platform identity while noting workspace, regional endpoint, model management, provisioned-throughput, token-plan, and related platform surfaces.
- Keep Qwen and third-party model identities, Alibaba Cloud Skills, concrete endpoint aliases, and region-specific model snapshots separate from the service identity.
- Treat supported models, endpoints, regions, data-location/deployment scopes, quotas, pricing, retirement schedules, API compatibility, and plan features as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The service does not become the producer identity of third-party models it hosts.
- Producer provenance resolves to Alibaba Cloud.
