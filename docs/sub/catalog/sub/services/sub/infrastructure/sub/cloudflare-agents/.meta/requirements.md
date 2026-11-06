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

## Scoped original-source qualification — 2026-11-06

- Cloudflare's current Agents runtime uses Durable Objects and the Agents SDK Lifecycle, attaching explicit WebSocket, SQLite-backed State, Scheduler and harness capabilities. Durable stored state and scheduled jobs can survive object eviction, while in-memory execution/closures are not permanent. This is the hosted durable runtime identity, not an SDK-only installation.
- Workers AI, AI Gateway, Browser Run, Vectorize and externally hosted model providers remain separate services or integrations. SDK architecture, Cloudflare Workers/Durable Objects costs and limits, object naming, authorization, storage, routing and runtime lifecycles must be checked against the deployed version.
- Verified first-party source 1: https://developers.cloudflare.com/agents/runtime/
- Verified first-party source 2: https://developers.cloudflare.com/agents/runtime/capabilities/state/
- Verified first-party source 3: https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/
- Scope: originally documented hosted service identity and lifecycle/usage limits only; not a complete freshness/legal/security review, independent runtime execution, full schema/cache/CI/render, clean pass or final delivery gate.
