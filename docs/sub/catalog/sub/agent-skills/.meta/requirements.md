# Documentation Requirements

## Requirements

- Present Agent Skills as the catalog entry point for published skill collections and for standalone skills only when independent publication or another independent canonical identity is verified.
- Explain the Agent Skills concept concisely using the official Agent Skills site and specification as authoritative references.
- Treat collection membership or a source path inside one collection repository as insufficient by itself to justify a duplicated standalone catalog node.
- Keep the currently materialized direct-child navigation limited to `collections/`; do not retain an empty or collection-duplicating `skills/` branch.
- Keep collection composition, concrete skill purpose, dependencies, runtime/tool requirements, bundled resources, and source links with the owning collection unless a future independently published skill becomes canonical.
- Do not present internal RC, migration, ownership, or placeholder language as reader-facing catalog content.

## Validation

- Direct-child navigation matches the materialized tree exactly.
- No standalone skill page is linked unless its independent canonical identity has been verified.
- The page contains no `Temporary catalog summary`, RC-only taxonomy, or obsolete `meta.yml` processing terminology.
- Official standard and specification links resolve to the current Agent Skills sources.
