# Documentation Requirements

## Requirements

- Identify Microsoft Skills as Microsoft's official `microsoft/skills` repository-backed collection of agent skills, plugins, custom-agent assets, templates, and MCP configurations for Azure SDK and Microsoft Foundry development workflows.
- Preserve the collection boundary rather than materializing each language/service skill as an independent catalog entity unless a later task selects a durable standalone skill identity.
- Keep the duplicated `.github/skills/` installation surface and canonical plugin-contained skill sources as implementation details of the same collection, following current repository guidance.
- Keep MicrosoftDocs Azure Agent Skills as a separate canonical collection because it is generated/curated from Microsoft Learn documentation and has a different repository, ownership workflow, catalog, and release/update pipeline.
- Treat skill counts, language breakdown, installer commands, plugin manifests, supported agents, repository structure, and WIP/testing status as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Source-specific permission and sensitive-data boundaries

- Distinguish Microsoft Skills instruction packages from deployed Azure resources, Azure MCP permissions, a local shell, `kubectl` access and AKS packet capture; availability of one does not imply the others.
- For `aks-network-capture`, require explicitly bound AKS target/context, nodes or pods, capture filter/duration, artifact destination and approval of temporary ConfigMaps, Jobs, retrieval pods, generated traffic and exact-run cleanup. Packet payloads can contain credentials or customer information; debug-container fallback requires separate authorization.
- Preserve the selected skill's action scope. The first-party `cost-optimization` skill makes recommendations only and must not automatically delete, resize, purchase or deploy resources; other skills may require their own access and external-transmission review.
- Cite the pinned [AKS capture skill](https://github.com/microsoft/skills/blob/4f831bbbf54e004507758d8ef2ab420c77bb81b6/.github/plugins/aks-skills/skills/aks-network-capture/SKILL.md), [capture authorization contract](https://github.com/microsoft/skills/blob/4f831bbbf54e004507758d8ef2ab420c77bb81b6/.github/plugins/aks-skills/skills/aks-network-capture/references/capture-authorization.md) and [cost optimization skill](https://github.com/microsoft/skills/blob/4f831bbbf54e004507758d8ef2ab420c77bb81b6/.github/plugins/azure-cost/skills/cost-optimization/SKILL.md). The documentation review does not establish actual tenant, credential, packet-capture or live MCP behavior.

## Validation

- The collection is not conflated with Microsoft Agent Framework, Copilot Studio, Foundry, VS Code, or the MicrosoftDocs Azure Agent Skills collection.
- Producer provenance resolves to Microsoft.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
