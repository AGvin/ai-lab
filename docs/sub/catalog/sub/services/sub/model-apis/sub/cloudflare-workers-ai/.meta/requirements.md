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
