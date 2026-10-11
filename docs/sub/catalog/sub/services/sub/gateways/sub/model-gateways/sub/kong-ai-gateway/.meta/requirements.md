# Documentation Requirements

## Requirements

- Identify Kong AI Gateway as Kong Inc.'s generally available AI-native gateway product beginning with the independently versioned 2.x line.
- Preserve the product boundary established by Kong: AI Gateway 2.x has its own runtime, control plane, Admin API, version number, release cadence, and Konnect experience rather than being only a plugin set inside Kong Gateway 3.x.
- Keep LLM/model routing, MCP and agent traffic, AI policies, provider coverage, analytics, and cost/security controls source-backed and version-scoped.
- Keep legacy AI Gateway plugins that remain supported inside Kong Gateway 3.x with the canonical Kong Gateway software identity; migration guidance does not erase that historical/software boundary.
- Treat provider/protocol support, policy inventory, Konnect features, migration tooling, pricing, and version support as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Kong AI Gateway 2.x is not collapsed back into the general Kong Gateway software identity.
- The entity remains an AI/model gateway service even when its traffic model includes MCP and agent workloads beyond model API calls.
- Producer provenance resolves to Kong Inc.
