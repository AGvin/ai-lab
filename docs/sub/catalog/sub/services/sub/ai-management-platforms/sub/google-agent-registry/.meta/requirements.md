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

## Scoped original-source qualification — 2026-11-06

- Google Cloud Agent Registry became generally available on 2026-06-18 with API v1/client libraries and Agent-to-Agent v1.0 binding support. It catalogs and governs registered agent, MCP server and related resource metadata but does not itself execute agents; the current Agent Registry product/API lifecycle remains separate from Gemini Enterprise Agent Platform and its managed Agent Runtime.
- Google's official release notes date standalone Skill governance to preview on 2026-07-23 and cross-project management boundaries to preview on 2026-10-30. The latter can centralize search/governance across managed projects but must not be presented as a fully GA cross-project runtime or universally enabled permission boundary.
- Search discoverability, lifecycle revisions, approvals, IAM and supported regions are configured under account/project policy. An agent appearing in a registry is not automatically trusted or authorized to access third-party tools or enterprise data.
- Verified first-party source 1: https://docs.cloud.google.com/agent-registry/release-notes
- Verified first-party source 2: https://docs.cloud.google.com/agent-registry/docs/overview
- Scope is source-backed existing governance/registry service identity and publisher-documented operational boundaries only. No new entity/metadata, independent compliance/security/runtime proof, comprehensive freshness audit, whole-repository schema/cache/CI/render, reader-repair, clean pass, final gate or merge credit.
