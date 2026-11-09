# Neon Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Updated upstream feature and access boundaries

An [independent comparison of the current upstream skill tree](https://github.com/neondatabase/agent-skills/tree/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills) with the previously pinned source found **8 changed files in 5 of 7 skill directories**, despite an unchanged upstream README. Treat these source changes as version-specific; the original migration and Postgres diagnostics guidance above remains valid within its cited scope.

- **AI Gateway credits:** the newer [AI Gateway skill](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon-ai-gateway/SKILL.md) permits prepaid credits on all Neon plans, including Free. A Free account needs a payment card and purchased credits before models can serve requests. The `paid_plan_required` error name does not necessarily mean the subscription must be upgraded. Treat purchases and branch credentials as separately authorized operations.
- **Functions secrets:** the [updated configuration](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon-functions/SKILL.md) uses `{ value, required }` for secrets, with required/optional/default-branch behavior that depends on CLI and config package versions. Empty or omitted values can modify or remove a live secret. Review the exact target and deployed configuration; do not copy older `process.env.X!` recipes as universally current.
- **Realtime authorization:** the [newer Realtime skill](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon-realtime/SKILL.md) states that live subscriptions reject RLS-protected tables. **Do not switch off production RLS merely to enable subscriptions** without an approved alternative user-isolation design, such as server-authorized sealed queries, and explicit testing.
- **Logs:** the [updated Loki reference](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon/references/logs-loki.md) adds version-sensitive CLI/SDK methods and cautions that limited log query results may be incomplete. Access and retention of production telemetry require separate permission review.

No billing action, user-key access, code installation or database execution was performed during this static source review. Full rights, all live service behavior, and repository-wide renderer/CI remain outside this bounded check.

## Relations

- Produced by: [Neon](../../../../../producers/sub/n/sub/neon/)

## Collection purpose

Neon Agent Skills is Neon's published collection of portable agent instructions, scripts, and supporting resources for Neon and Lakebase Postgres workflows. The upstream collection covers database use and branches, authentication, object storage, gateways, and related developer-agent work. [Upstream collection](https://github.com/neondatabase/agent-skills).

## Organization and access

The repository's `skills/` directories and their `SKILL.md` entry points hold the collection's skill content. The upstream README provides the current inventory and installation choices. Optional Agent Plugins v1 packaging and client-specific manifests for Claude, Cursor, Kimi, Pi, and other clients distribute or expose that same collection; they do not create separate skill-collection identities.

The Neon MCP server is an integration that can accompany the skills. A separately linked Neon-for-agent-platforms repository contains companion material with its own distribution boundary; a link from this collection does not establish common ownership of every companion workflow.

## Migration, connection and diagnostic safety

The collection-owned [`neon-postgres` skill](https://github.com/neondatabase/agent-skills/blob/65ee2bf7427b358e6fe1989d214065692bd01205/skills/neon-postgres/SKILL.md) makes an operational distinction important for database work:

- Use pooled Neon connections (a hostname containing `-pooler`) for ordinary application requests; use the **direct, non-pooled** connection for schema migrations, `pg_dump`/`pg_restore`, replication and operations requiring session state. Verify the intended project, branch and database, and do not replace the application's pooled connection string merely to run a migration.
- Test schema migrations on a separate branch with appropriately handled production-like data before production deployment. Record rollback/recovery options, confirm the production target and obtain explicit authorization before irreversible schema or resource changes.
- Prefer first-party read-only database diagnostics. An `unused-indexes` result is not permission to drop an index. `EXPLAIN ANALYZE` **executes the underlying SQL**, so avoid it for any mutating query without explicit approval. Compute restarts and scale-to-zero can reset statistics; use representative workloads before drawing conclusions.

Skill installation does not provide authentication, backup guarantees or permission to provision, mutate or delete a database.

## Runtime and permission boundaries

Installing instructions does not authenticate a database session or grant authority to change data, provision infrastructure, deploy code, or use credentials. Actual operations depend on the agent client, configured tools, account permissions, and runtime behavior. Review the underlying service's data and access conditions for the chosen workflow.

Skill names, client support, plugin declarations, Neon/Databricks product branding, and service features change. Follow the current upstream inventory and [Neon documentation](https://neon.com/docs/ai/agent-skills) for supported installation and usage; collection publication alone does not validate a specific client or deployment.

## Source interpretation

Neon's Apache-2.0 repository bundles instruction content and client integrations for Lakebase Postgres and backend workflows. Current guidance merges the former branching and egress skills into neon-postgres and links an independently maintained agent-platforms companion. Skills, MCP authentication and cloud resources remain distinct; verify the selected database and access scope.

[Reviewed original README](https://github.com/neondatabase/agent-skills/blob/65ee2bf7427b358e6fe1989d214065692bd01205/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Agent Skills repository and current inventory](https://github.com/neondatabase/agent-skills)
- [Neon Agent Skills documentation](https://neon.com/docs/ai/agent-skills)
