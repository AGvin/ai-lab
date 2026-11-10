# Documentation Requirements

## Requirements

- Present Agent Skills here as the open package format/specification, not as the broader skill concept or as one client's implementation behavior.
- Treat the current `agentskills.io` specification and upstream repository as authoritative sources for the package contract. Re-check them before changing required files, metadata fields, validation constraints, or experimental features.
- Preserve the core package boundary from the upstream specification: a skill directory with a required `SKILL.md` entrypoint containing YAML frontmatter followed by Markdown instructions.
- Record currently required frontmatter fields such as `name` and `description`, and optional/experimental fields such as `license`, `compatibility`, `metadata`, or `allowed-tools`, only with their current upstream status and constraints.
- Describe optional supporting directories/files only according to the specification; do not turn common client conventions into universal mandatory layout.
- Keep reusable purpose, discovery/activation/execution semantics, trust boundaries, and relationships to other extension mechanisms with the selected Agent Skills concept owner.
- Keep creation, usage, portability, and maintenance teaching under the selected Agent Skills learning owners.
- Keep client-specific discovery paths, precedence, invocation, permissions, enable/disable controls, extensions, and compatibility under each concrete product integration owner.

## Validation

- Required/optional/experimental package claims are traceable to the current upstream Agent Skills specification.
- Client-specific metadata or invocation controls are not redefined as universal Agent Skills requirements.
- Generic concept and authoring pedagogy are not duplicated into the formal specification artifact.

## Scoped original-source qualification — 2026-11-07

- Agent Skills is an open skill-directory packaging specification, not a guarantee that any assistant will automatically discover, invoke or safely execute a skill. The published contract requires a directory-local `SKILL.md` with YAML frontmatter and a Markdown instruction body; `name` and `description` are required, and optional support material includes `scripts/`, `references/`, and `assets/`.
- The official spec constrains name/description and names optional `license`, `compatibility` and `metadata` fields; `allowed-tools` is expressly experimental. Implementation-specific activation, trust, sandboxing and permissions are outside the package schema. A package may contain executable code and references; do not treat its mere format as safe to execute.
- Verified primary source 1: https://agentskills.io/specification
- Verified primary source 2: https://github.com/agentskills/agentskills
- Existing format identity/source gate only; no packaged skill executed, client interoperability/permissions certified, full upstream security/license review, repository-wide schema/cache/CI/render, clean pass or final gate.
