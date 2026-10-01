# Documentation Requirements

## Requirements

- Identify Microsoft Skills as Microsoft's official `microsoft/skills` repository-backed collection of agent skills, plugins, custom-agent assets, templates, and MCP configurations for Azure SDK and Microsoft Foundry development workflows.
- Preserve the collection boundary rather than materializing each language/service skill as an independent catalog entity unless a later task selects a durable standalone skill identity.
- Keep the duplicated `.github/skills/` installation surface and canonical plugin-contained skill sources as implementation details of the same collection, following current repository guidance.
- Keep MicrosoftDocs Azure Agent Skills as a separate canonical collection because it is generated/curated from Microsoft Learn documentation and has a different repository, ownership workflow, catalog, and release/update pipeline.
- Treat skill counts, language breakdown, installer commands, plugin manifests, supported agents, repository structure, and WIP/testing status as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The collection is not conflated with Microsoft Agent Framework, Copilot Studio, Foundry, VS Code, or the MicrosoftDocs Azure Agent Skills collection.
- Producer provenance resolves to Microsoft.
