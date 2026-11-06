# Documentation Requirements

## Requirements

- Identify Cloudflare Workers AI as Cloudflare's producer-operated serverless model-execution API/platform running supported models on Cloudflare's GPU-backed global network.
- Preserve its primary model-API identity: it exposes a managed catalog of models through Workers bindings and HTTP APIs without requiring users to operate inference servers.
- Keep Cloudflare AI Gateway, Vectorize, Agents, AI Search, Workers runtime, and individual model identities separate even when they integrate directly.
- Treat available models, pricing, limits, bindings/API surfaces, custom-model options, regional behavior, and plan availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Workers AI is not represented as the producer/owner of third-party model families it hosts.
- Producer provenance resolves to Cloudflare.

## Scoped original-source qualification — 2026-11-06

- Workers AI is Cloudflare-hosted serverless inference accessed through a Worker binding, REST API, or the dashboard. Its runtime and model catalog are distinct from Cloudflare AI Gateway, which routes third-party providers as well. The provider's 2026-11-05 changelog announces specific model removals for November 15: this is a mutable service/catalog lifecycle, not a timeless model capability.
- Do not infer third-party model authorship, permanent free-tier quotas, model availability after scheduled deprecations or AI Gateway billing from the Workers AI service identity.
- Verified first-party source 1: https://developers.cloudflare.com/workers-ai/get-started/
- Verified first-party source 2: https://developers.cloudflare.com/changelog/product/workers-ai/
- This accepts only the existing service identity and bounded source facts, not a full freshness/license/ownership audit, independent benchmarks, permission to process sensitive data, runtime tests, complete schema/cache/CI/render or final delivery.
