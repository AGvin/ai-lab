# Documentation Requirements

## Requirements

- Identify Azure Agent Skills as the MicrosoftDocs-maintained collection of production-oriented Agent Skills for Azure cloud development, built from/linked to current Microsoft Learn documentation and distributed through skill/plugin installation surfaces.
- Preserve its distinct identity from `microsoft/skills`: Azure Agent Skills has a docs-to-skills generation/catalog pipeline, Azure-service knowledge focus, its own repository, and multi-assistant plugin packaging.
- Preserve the collection boundary rather than creating a catalog entity for every generated Azure service skill.
- Treat skill inventory/counts, generated timestamps, bundles, plugin manifests, installation commands, supported assistants, network/documentation dependencies, and experimental host-feature requirements as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Generated documentation and Azure operation boundaries

- State that MicrosoftDocs Azure skills can combine generated local summaries with Microsoft Learn content retrieved through `mcp_microsoftdocs:microsoft_docs_fetch` or `fetch_webpage`; selected skills declare network access, so documentation queries are not necessarily offline.
- Preserve generated-at metadata as a freshness hint and use live first-party documentation for changing Azure APIs, support matrices, limits, pricing, licensing and permissions; copying a skill directory does not validate currency or grant MCP availability.
- For cost-management and backup workflows, distinguish reading documentation from accessing tenant billing/recovery data. Require explicit tenant/subscription/resource targets, RBAC, data sensitivity, spend/change authorization and suitable recovery safeguards before Azure mutation.
- Ground these boundaries in pinned [Cost Management](https://github.com/MicrosoftDocs/Agent-Skills/blob/6ecdaf59cde880d0ef3d1715357b6c0b0c6696d8/skills/azure-cost-management/SKILL.md) and [Backup](https://github.com/MicrosoftDocs/Agent-Skills/blob/6ecdaf59cde880d0ef3d1715357b6c0b0c6696d8/skills/azure-backup/SKILL.md); no connected tenant, runtime, retention or billable operation was tested.

## Validation

- The collection is not conflated with Microsoft Skills, Copilot product features, or general Microsoft Learn documentation.
- Producer provenance resolves to Microsoft.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
