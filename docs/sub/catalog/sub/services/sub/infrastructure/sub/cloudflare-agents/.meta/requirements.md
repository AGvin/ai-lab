# Documentation Requirements

## Requirements

- Identify Cloudflare Agents as Cloudflare's hosted durable-agent runtime/platform built around the Agents SDK, Durable Objects, state/session storage, real-time connections, scheduling, recovery, and globally managed execution.
- Preserve its managed infrastructure identity despite the presence of an SDK: the durable hosted runtime is a core product boundary, while agent harness logic can be supplied by the user or Cloudflare components.
- Keep Workers AI, AI Gateway, Vectorize, AI Search, Browser, Sandbox, MCP/payment tools, communication channels, and individual agents as separate products/integrations where independently durable.
- Treat runtime limits, channels, tool integrations, SDK APIs, storage semantics, pricing, deployment constraints, and feature lifecycle as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity is not reduced to an installable framework-only identity or conflated with generic Cloudflare Workers.
- Producer provenance resolves to Cloudflare.
