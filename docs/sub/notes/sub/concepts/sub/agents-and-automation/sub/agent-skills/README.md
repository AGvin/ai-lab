# Agent Skills

Legacy residual for Agent Skills material whose remaining ownership is formal specification or still-active mixed-source routing.

> **Migration note:** This page is intentionally fragmentary during the active consolidation. Durable Agent Skills purpose, discovery/activation/execution semantics, host-versus-skill authority, related-concept boundaries, portability principles, and security/trust implications are already preserved in the canonical `concepts/ai-engineering/extensibility-and-packaging/agent-skills/` owner, with portability teaching additionally materialized under `learning/.../agent-skills/platform-support-and-portability/`. Former host-specific platform-support material has been reconciled into each product's canonical `sub/integrations/sub/agent-skills/` owner, so that child residual is no longer retained. The remaining package-layout and `SKILL.md` details stay here until the exact formal specification-artifact owner is selected; the sources/collections child remains linked while its installer/catalog fragment is still unresolved.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Residual sources

- [Sources and collections](./sub/sources/) — remaining installer/catalog material pending an approved canonical destination.

## Formal package residual

The open Agent Skills format requires a directory with a `SKILL.md` entrypoint:

```text
skill-name/
├── SKILL.md          # Required metadata and instructions
├── scripts/          # Optional executable helpers
├── references/       # Optional documentation loaded on demand
├── assets/           # Optional templates and output resources
└── ...               # Optional client-specific files
```

`SKILL.md` starts with YAML frontmatter and continues with Markdown instructions:

```markdown
---
name: release-notes
description: Draft release notes from merged changes. Use when preparing a software release or changelog.
---

# Release notes workflow

1. Identify the release range.
2. Group changes by user impact.
3. Separate breaking changes and migrations.
4. Verify every claim against the source changes.
```

The standard requires `name` and `description`. It also defines optional fields such as `license`, `compatibility`, `metadata`, and experimental `allowed-tools`. Individual clients may add their own metadata or invocation controls.

These normative/package-shape details are preserved here only as migration source. They must move to the selected formal Agent Skills specification artifact rather than becoming independent concept or learning truth.

## References

- Agent Skills overview: https://agentskills.io/home
- Agent Skills specification: https://agentskills.io/specification
