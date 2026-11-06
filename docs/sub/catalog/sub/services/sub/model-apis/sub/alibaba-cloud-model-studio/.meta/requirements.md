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

## Scoped original-source qualification — 2026-11-06

- Alibaba Cloud Model Studio is a managed model-API platform exposing Qwen and selected third-party models, including OpenAI-/Anthropic-compatible endpoints. The provider specifies region, service deployment scope and access domain as distinct configuration dimensions affecting inference execution and data location.
- Model Studio API keys and Base URLs are scoped by region and billing plan; legacy DashScope shared domains, workspace-specific production endpoints and limited trial routes are not interchangeable. Supported models, regions, endpoint compatibility, pricing and deployment terms remain account- and time-dependent.
- Verified first-party source 1: https://www.alibabacloud.com/help/en/model-studio/regions
- Verified first-party source 2: https://www.alibabacloud.com/help/en/model-studio/base-url
- This accepts only service-scoped source identity and documented capability boundaries; it is not an exhaustive freshness audit, authenticated endpoint test, independent compliance/ownership review, global schema/cache/CI/render verification, clean pass or final-delivery gate.
