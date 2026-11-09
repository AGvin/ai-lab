# Documentation Requirements

## Requirements

- Identify Prisma Skills as Prisma's released first-party portable Agent Skills collection for ORM setup, CLI/Client APIs, schema migrations, database provisioning, version upgrades and Prisma deployment workflows.
- Preserve the distinction between this collection and the version-specific `prisma/orm/skills` subdirectory; referenced Prisma 8 skills are not automatically separate canonical collections without a durable independent upstream lifecycle.
- Keep version-specific v6/v7/v8 guidance separate, including the MongoDB connector boundary, client API changes, adapters and breaking upgrades. A skill's documented version scope is not a global current Prisma API guarantee.
- Do not duplicate individual `prisma-*` directories as canonical collection peers. Distinguish software tooling (Prisma ORM/Client/Studio), deployment services and MCP connectors from instruction packages.
- Keep exact skills, dependencies, package-version requirements, API availability, migration support and distribution methods freshness-sensitive.
- Preserve source-backed first-party producer provenance with a reciprocal `produces` relation.

## Database lifecycle and deployment approval boundaries

- State that the `prisma-postgres-setup` no-account `create-db` database defaults to deletion after 24 hours unless claimed, and the claim URL/connection string must be kept private. Reuse existing databases and verify the exact workspace/project/region before creating a new one.
- Distinguish Prisma 7 ORM CLI `migrate reset`/schema changes from Prisma 8 Platform/Compute operations; require explicit target, backup/rollback consideration and user authorization before destructive migration or reset.
- From pinned `prisma-compute`, warn that Platform operations may select production without an explicit branch even when the current Git branch is not production; verify project, stage/branch and CLI version before deploy, promote, rollback or delete. Deploy-on-push and CI service tokens need separately reviewed permissions.
- Ground these boundaries in the pinned [Postgres setup](https://github.com/prisma/skills/blob/8ea289b730c2e89f7ff1f518af128b113d842a92/prisma-postgres-setup/SKILL.md), [Prisma 7 CLI](https://github.com/prisma/skills/blob/8ea289b730c2e89f7ff1f518af128b113d842a92/prisma-cli/SKILL.md) and [Compute](https://github.com/prisma/skills/blob/8ea289b730c2e89f7ff1f518af128b113d842a92/prisma-compute/SKILL.md). Source guidance is not proof of a live deployment or data-recovery test.

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

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
