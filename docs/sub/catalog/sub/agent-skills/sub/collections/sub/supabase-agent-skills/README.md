# Supabase Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Supabase Agent Skills is Supabase’s official collection of instructions and supporting material for Supabase development and PostgreSQL operational guidance. General PostgreSQL advice and Supabase-specific workflows remain distinguishable within the collection; individual skill folders are not automatically separate products.

## Distribution and applicability

The repository provides skills CLI and Claude Code plugin installation routes. Those are distribution surfaces of the same collection. Check the current inventory, skill revision, supported client and included scripts before installation. Advice must be matched to the application’s schema, PostgreSQL version and Supabase features; publication is not a blanket applicability or safety guarantee.

## License and permissions

The repository is MIT-licensed. Skills are separate from the hosted Supabase platform, CLI, MCP server and database credentials. Installing them does not grant a project connection or authorize a migration. Use scoped database access, inspect generated SQL and review changes before applying them. Hosted service contracting and data-processing terms belong to the applicable Supabase order, independently of this instruction package.

## Source-backed Supabase security details

The pinned [Supabase skill](https://github.com/supabase/agent-skills/blob/c9be0e931b7930f7d02126d04774d904c381e7d7/skills/supabase/SKILL.md) says public Data API access and row-level security (RLS) are **separate controls**: a grant to `anon` or `authenticated` can expose a table unless matching RLS policies are in place. Enable RLS for exposed tables and inspect authorization policies rather than treating a schema change or a generated SQL snippet as safe by default. The same skill explicitly warns not to publish `service_role`/secret keys in browser bundles or use user-editable `user_metadata` for authorization; use scoped tokens when the CLI, Management API or MCP access is actually authorized.

The pinned [MCP manifest](https://github.com/supabase/agent-skills/blob/c9be0e931b7930f7d02126d04774d904c381e7d7/.mcp.json) configures a remotely hosted documentation endpoint `https://mcp.supabase.com/mcp?features=docs`. Installing a skill alone does not connect a database, and a documentation MCP query is still an external request; the docs-feature manifest does **not** itself prove permission to read or mutate any user's Supabase project. Confirm exact environment, RLS posture, privilege scope, migration review and backup/rollback strategy before any production query, grant or schema change. This was a bounded static source audit; no service or database was accessed.

## Relations

- Produced by: [Supabase, Inc.](../../../../../producers/sub/s/sub/supabase-inc/)

## Source interpretation

Supabase's MIT collection distinguishes general PostgreSQL best-practice guidance from Supabase-specific workflows, with CLI and plugin delivery paths. The upstream now links its getting-started/ai-skills documentation. Validate schema/version and RLS assumptions; installation supplies neither database credentials nor authority to apply migrations.

[Reviewed original README](https://github.com/supabase/agent-skills/blob/c9be0e931b7930f7d02126d04774d904c381e7d7/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Supabase Agent Skills repository](https://github.com/supabase/agent-skills)
- [Official documentation](https://supabase.com/docs/guides/getting-started/ai-skills)
- [Collection source license](https://github.com/supabase/agent-skills/blob/main/LICENSE)
