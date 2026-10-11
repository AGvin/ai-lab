# Documentation Requirements

## Requirements

- Identify Prisma Skills as Prisma's released first-party portable Agent Skills collection for ORM setup, CLI/Client APIs, schema migrations, database provisioning, version upgrades and Prisma deployment workflows.
- Preserve the distinction between this collection and the version-specific `prisma/orm/skills` subdirectory; referenced Prisma 8 skills are not automatically separate canonical collections without a durable independent upstream lifecycle.
- Keep version-specific v6/v7/v8 guidance separate, including the MongoDB connector boundary, client API changes, adapters and breaking upgrades. A skill's documented version scope is not a global current Prisma API guarantee.
- Do not duplicate individual `prisma-*` directories as canonical collection peers. Distinguish software tooling (Prisma ORM/Client/Studio), deployment services and MCP connectors from instruction packages.
- Keep exact skills, dependencies, package-version requirements, API availability, migration support and distribution methods freshness-sensitive.
- Preserve source-backed first-party producer provenance with a reciprocal `produces` relation.

## Validation

- The collection is independently maintained as a public upstream skill distribution.
- Client-specific plugin/MCP packaging and the collection's individual SKILL.md files are not duplicated as separate canonical products.
- Current compatibility, version and feature statements derive from first-party release documentation.
- The producer's inverse relation matches the collection identity.
