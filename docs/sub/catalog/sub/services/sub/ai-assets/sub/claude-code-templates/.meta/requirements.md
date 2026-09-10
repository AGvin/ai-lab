# Documentation Requirements

## Requirements

- Identify Claude Code Templates (`aitmpl.com`, also presented as AI Templates) as a hosted interactive catalog for discovering and installing ready-to-use Claude Code components, including skills, agents, commands, settings, hooks, MCP integrations, and plugins where currently supported.
- Keep the hosted catalog/discovery identity distinct from the project's installable CLI, analytics, conversation-monitoring, health-check, and other local tooling; those capabilities do not turn the service profile into a generic software profile.
- Explain that the Agent Skills relation represents Claude Code Templates as a material discovery resource for skills, not as the authority for the Agent Skills specification, an endorsement by AI Lab, or a claim of complete skill coverage.
- Preserve source/provenance boundaries for components aggregated from multiple upstream and community sources rather than implying that Daniel Avila authored every listed component.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include the current official catalog site, documentation, and project repository as authoritative project resources.
- Keep counts, integrations, sponsorships, supported component totals, and other rapidly changing service facts source-backed and time-scoped if expanded.

## Validation

- The canonical service identity remains the hosted `aitmpl.com` discovery/catalog surface rather than a duplicate standalone identity for every CLI feature or listed component.
- The `discovery-resource-for` relation points to the canonical Agent Skills domain and does not expand into per-skill edges solely because the catalog currently lists those skills.
- Producer provenance does not imply authorship of third-party or community-contributed components.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official catalog, documentation, and repository destinations remain current project-owned sources.
