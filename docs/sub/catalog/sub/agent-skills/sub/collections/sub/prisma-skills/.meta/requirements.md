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

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Prisma Skills is Prisma's first-party collection of portable Agent Skills instructions for ORM and database workflows. It covers setup, CLI and Client use, schema changes, upgrades, provisioning and deployment. The official repository declares MIT licensing and provides the collection installation path `npx skills add prisma/skills`. The instructions are distinct from Prisma ORM, a running database, hosted deployment services and an MCP connection. [Collection repository](https://github.com/prisma/skills).

Match the instructions to the installed Prisma version. Current upstream guidance separates existing Prisma 6/7 projects from Prisma 8 setups and points detailed Prisma 8 API work to package-owned references synchronized through Prisma tooling. Legacy recipes should not be assumed to apply unchanged to a newer major release or to every database connector. [Version guidance](https://github.com/prisma/skills) · [Prisma documentation](https://www.prisma.io/docs).

Installing instructions does not grant credentials or authorize destructive schema changes. Review the selected revision, migration plan, target database and the coding client's available tools before running it. Individual skill directories and generated client packaging are parts of the collection rather than independent service identities. [Collection and installation guidance](https://github.com/prisma/skills).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
