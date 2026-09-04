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
