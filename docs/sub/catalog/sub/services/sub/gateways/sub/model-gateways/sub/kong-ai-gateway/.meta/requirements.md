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

## Scoped original-source qualification — 2026-11-06

- Kong AI Gateway 2.0 became generally available on 2026-09-01 as a separately versioned AI-native gateway runtime/control plane. Its first-party launch describes MCP server bundling with ACL-driven tool visibility, identity-aware traffic policies and multi-modal pricing. Legacy Kong Gateway 3.x AI plugins remain a distinct software/runtime lineage: 3.14 LTS still supports them, with 3.18 planned to make them opt-in.
- Document policies and migration per exact Kong AI Gateway or Kong Gateway 3.x release. MCP ACL, pricing enforcement, provider support, and production certification are not interchangeable between runtime lines; integration does not change upstream model or MCP tool ownership.
- Verified first-party source 1: https://konghq.com/blog/product-releases/kong-ai-gateway-2-0-ga
- Verified first-party source 2: https://developer.konghq.com/ai-gateway/
- This is a bounded identity/source qualification, not live service execution, credential review, security/privacy certification, complete license/ownership clearance, independent benchmarking, full schema/cache/CI/render, clean-group acceptance or final-delivery credit.
