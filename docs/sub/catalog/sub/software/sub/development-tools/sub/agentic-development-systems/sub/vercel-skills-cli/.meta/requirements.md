# Documentation Requirements

## Requirements

- Identify Vercel Skills CLI as the original independent MIT-licensed Node.js npm package `skills` with `skills` and `add-skill` command-line entrypoints; distinguish from the web skills.sh registry, Vercel Agent Skills collection, the Agent Skills format and individually installed packages.
- Source-bound release: original public v1.7.4 dated 2026-10-19; its tagged `package.json` records Node.js `>=22.20.0` and `skills@1.7.4`. Public `npx skills` is the documented invocation. Supported agents, paths, telemetry and command formats are mutable.
- Describe the stable `add`, `find`, `list`, `use`, `check`, `update`, `remove`, and `init` workflows, and qualify `experimental_sync` and `experimental_install` as previews rather than stable interface guarantees.
- Explain repository, URL and local source selection, global vs project-local installs, supported target agents and independent source revision pinning. Third-party skill content may have scripts and runtime instructions; its trusted execution is not guaranteed by the CLI or registry.
- Review third-party instructions, scripts and local file changes before installation or privileged agent use; grant minimal permissions and protect tokens, workspaces and network access. A skills.sh rank or scanner signal is not certification.
- Preserve original documentation of anonymous usage telemetry and audit requests; `DISABLE_TELEMETRY=1` and `DO_NOT_TRACK=1` are documented opt-outs for the inspected release, not claims about other clients or complete data protection.
- Distinguish the MIT software license from separate rights of third-party skills, code, scripts and data. Vercel original source is established, but complete beneficial ownership and indirect Russian stakes were not audited; avoid unsupported Tier 1 or Tier 2 classification.
- Maintain one canonical `produced-by` to `catalog/producers/v/vercel-inc` and reciprocal producer `produces`. Link the separate skills.sh registry and Vercel Agent Skills collection, and remove the original cross-identity `Vercel Skills CLI` registry alias.

## Validation

- Original tagged package metadata, repository release and docs establish independent software; parent index lists new node exactly once and registry retains its distinct identity.
- Entity, requirements, reader, inverse producer relation and all local links resolve; no CLI invocation, external security audit, whole-catalog CI or rendering is asserted.
