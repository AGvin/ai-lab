# Documentation Requirements

## Requirements

- Identify Google Agent Registry as Google Cloud's generally available governed registry/discovery service for agents and related reusable agent resources.
- Preserve its primary AI-management/governance identity: the service provides registration, versioning, lifecycle state, discovery/search, interfaces/bindings, and organizational reuse rather than executing agents itself.
- Preserve the independent GA boundary: Agent Registry has a dedicated product documentation tree, release notes, API v1/client libraries, console experience, resource types, and lifecycle separate from Gemini Enterprise Agent Platform even though the two integrate closely.
- Keep Gemini Enterprise Agent Platform as the managed agent build/runtime/orchestration platform; keep Agent Gateway, sandboxes, individual agents, standalone skills, A2A endpoints, and external resources as separate products/components/resources unless independently materialized.
- Treat supported resource types, regions, lifecycle/versioning behavior, semantic search, interfaces/protocols, quotas, IAM, APIs, and integrations as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains a registry/governance service rather than an agent runtime or static skill collection.
- Feature-level additions such as standalone Skill resources do not create duplicate product identities.
- Producer provenance resolves to Google.
