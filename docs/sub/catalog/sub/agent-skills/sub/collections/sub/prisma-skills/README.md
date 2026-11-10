# Prisma Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Prisma Skills is Prisma's first-party collection of portable Agent Skills instructions for ORM and database workflows. It covers setup, CLI and Client use, schema changes, upgrades, provisioning and deployment. The official repository declares MIT licensing and provides the collection installation path `npx skills add prisma/skills`. The instructions are distinct from Prisma ORM, a running database, hosted deployment services and an MCP connection. [Collection repository](https://github.com/prisma/skills).

## Scope and operating boundaries

Match the instructions to the installed Prisma version. Current upstream guidance separates existing Prisma 6/7 projects from Prisma 8 setups and points detailed Prisma 8 API work to package-owned references synchronized through Prisma tooling. Legacy recipes should not be assumed to apply unchanged to a newer major release or to every database connector. [Version guidance](https://github.com/prisma/skills) · [Prisma documentation](https://www.prisma.io/docs).

Installing instructions does not grant credentials or authorize destructive schema changes. Review the selected revision, migration plan, target database and the coding client's available tools before running it. Individual skill directories and generated client packaging are parts of the collection rather than independent service identities. [Collection and installation guidance](https://github.com/prisma/skills).

## Provisioning, migration and production-target safeguards

The pinned [Prisma Postgres setup](https://github.com/prisma/skills/blob/8ea289b730c2e89f7ff1f518af128b113d842a92/prisma-postgres-setup/SKILL.md) first reuses an existing database. Its no-account `create-db` option is **temporary**: the default database is deleted after **24 hours** unless claimed through a private URL before expiry. Never present an unclaimed temporary database as permanent storage or reveal its connection string or claim URL in logs or source control. Check the selected workspace, project, region and environment before provisioning, and never create a duplicate database merely because the shell cannot read the app's existing secret configuration.

Database operations can be destructive. The original [Prisma 7 CLI skill](https://github.com/prisma/skills/blob/8ea289b730c2e89f7ff1f518af128b113d842a92/prisma-cli/SKILL.md) includes migrations and `migrate reset`, while the separately versioned [Prisma Compute skill](https://github.com/prisma/skills/blob/8ea289b730c2e89f7ff1f518af128b113d842a92/prisma-compute/SKILL.md) uses Prisma 8 deployment commands. Compute's operational CLI can target the **production branch by default**, irrespective of the current Git branch, unless the proper explicit branch/project target is supplied. Require a database backup and rollback plan where relevant, review exact target and schema diff, and obtain approval for migration resets, remote deployments, promotions or deletions. No database, CLI or deployment was operated during this catalog review.

## Produced by

- [Prisma](../../../../../producers/sub/p/sub/prisma/)

## Source interpretation

Prisma's MIT collection distinguishes new Prisma ORM 8 setup from legacy Prisma 6/7 workflows. Detailed package-owned Prisma 8 guidance is synchronized separately; older CLI recipes are not interchangeable with new setup. Confirm the application's installed version and review schema changes, migrations and deployment targets before execution.

[Reviewed original README](https://github.com/prisma/skills/blob/8ea289b730c2e89f7ff1f518af128b113d842a92/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Collection repository](https://github.com/prisma/skills)
- [Prisma documentation](https://www.prisma.io/docs)
