# Documentation Requirements

## Requirements

- Present Agent Skills as the catalog entry point for published skill collections and for standalone skills only when independent publication or another independent canonical identity is verified.
- Explain the Agent Skills concept concisely using the official Agent Skills site and specification as authoritative references.
- Treat collection membership or a source path inside one collection repository as insufficient by itself to justify a duplicated standalone catalog node.
- Render the standard child-navigation block from the validated direct-child projection; do not expose an empty or collection-duplicating standalone-skill branch as materialized navigation.
- Render the dedicated `discovery-resources` block from the validated visible `has-discovery-resource` projection so specialized catalogs such as Claude Code Templates are discoverable from the domain root without creating per-skill listing relations.
- Keep discovery-resource descriptions with the canonical target context; the Agent Skills relation record and requirements must not duplicate target summaries merely for rendering.
- Keep collection composition, concrete skill purpose, dependencies, runtime/tool requirements, bundled resources, and source links with the owning collection unless a future independently published skill becomes canonical.
- Do not present internal RC, migration, ownership, or placeholder language as reader-facing catalog content.

## Validation

- The child-navigation block matches the validated materialized direct-child projection exactly.
- The `discovery-resources` block matches the visible `has-discovery-resource` projection exactly and does not expand one catalog-level relation into volatile per-skill edges.
- No standalone skill page is linked unless its independent canonical identity has been verified.
- The page contains no `Temporary catalog summary`, RC-only taxonomy, or obsolete `meta.yml` processing terminology.
- Official standard and specification links resolve to the current Agent Skills sources.
