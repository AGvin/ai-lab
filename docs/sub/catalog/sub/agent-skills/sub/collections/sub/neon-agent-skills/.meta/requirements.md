# Documentation Requirements

## Requirements

- Identify Neon Agent Skills as a released first-party portable Agent Skills collection for Neon/Lakebase Postgres, database branches, authentication, object storage, API gateways and developer-agent workflows.
- Preserve the single canonical collection identity despite the optional Agent Plugins v1 packaging and separate Claude, Cursor, Kimi, Pi and other client-specific manifests. The Neon MCP server is an integration, not another collection or a product-identical skill.
- Keep the independently linked Neon-for-agent-platforms repository and its packages separate unless evidence establishes they belong to the same maintained distribution. Do not reassign independently authored companion workflows automatically.
- Treat skill count, names, Postgres and Auth capabilities, documentation URLs, underlying Databricks product branding, supported clients, plugin declarations and installation guidance as freshness-sensitive.
- Installing a skill does not establish an authenticated database connection or authorize credentials/deployment operations; preserve tool permission and runtime validation boundaries.
- For `neon-postgres` workflows, preserve the first-party distinction between pooled application traffic (Neon endpoint host with `-pooler`) and a direct, non-pooled connection for migrations, `pg_dump`/`pg_restore`, logical replication and session-level SQL. Do not recommend silently switching the application's pooled `DATABASE_URL`; use an independently selected direct/unpooled migration connection instead.
- Before applying schema changes to production, require a reviewed migration plan and first run it on an isolated Neon branch with production-like structure and appropriate authorized data handling; confirm selected project, branch, database and backup/restore assumptions.
- For diagnostics, default to Neon read-only checks and treat `unused-indexes` as candidates rather than unconditional drop instructions. `EXPLAIN (ANALYZE)` executes its SQL; do not run it for mutating statements without explicit authorization. Check when compute restart/scale-to-zero resets relevant statistics, and do not infer safe mutation from an MCP read-only label.
- Preserve source-backed first-party producer provenance with a reciprocal `produces` relation.

## Reader projection

- Render the standard `entity-relations` block from all validated current-entity relations eligible for reader presentation.
- Render the `official-resources` block from canonical references supporting the identity, versioned facts, access context, and stated boundaries of this page.

## Selected migration and diagnostic safety review — 2026-11-09

- Inspected the [pinned first-party `neon-postgres` instructions](https://github.com/neondatabase/agent-skills/blob/65ee2bf7427b358e6fe1989d214065692bd01205/skills/neon-postgres/SKILL.md) and current collection README (unchanged at the compared revision). Its migration section requires direct/non-pooled connection, branch testing before production and clear project/branch/database selection. Database diagnostics warn that `EXPLAIN ANALYZE` executes queries, idle compute restarts may reset measurements, and suggested unused indexes are not deletion permissions.
- This records one bounded operational-risk correction, not a live Neon database test, OAuth flow, complete reference audit, data restoration rehearsal, or permissions/security certification.

## Validation

- The collection is independently maintained as a public upstream skill distribution.
- Client-specific plugin/MCP packaging and the collection's individual SKILL.md files are not duplicated as separate canonical products.
- Current compatibility, version and feature statements derive from first-party release documentation.
- The producer's inverse relation matches the collection identity.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.

## Neon current selected-skill drift reconciliation — 2026-11-09

- Independently compared the full `skills/` file inventories at historical pin `65ee2bf7427b358e6fe1989d214065692bd01205` and current first-party commit `2b0e2b6f56d2b41c5363049e30e6ab72aa260cce`: seven direct skill directories and 35 selected files at both revisions, but eight file contents differ in **five** directories (`neon-ai-gateway`, `neon-functions`, `neon-postgres`, `neon-realtime`, `neon`). The top-level README and root Apache-2.0 LICENSE remain byte-identical, so README-only freshness was insufficient.
- The full first-party repository tree comparison covers **282 tracked file blobs at each revision, 25 changed files**: eight changed original `skills/` files, eight bit-for-bit corresponding mirrors under `plugins/neon-postgres/skills/`, and nine manifest/package metadata files that only bump `3.0.1` to `3.0.5` (including `package-lock.json`; no dependency-entry drift). No additions or deletions appeared in the compared trees. This bounds the selected collection source change and client distribution surfaces, but not service runtime behavior.
- **AI Gateway entitlement changed:** the [current gateway skill](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon-ai-gateway/SKILL.md) and [November 6 release notes](https://neon.com/blog/category/changelog) document prepaid AI Gateway credits on every plan including Free, after adding a card and buying credits; this supersedes the historical paid-plan-only claim. `unavailable_reason: paid_plan_required` for an account with no credits is not automatically a requirement to upgrade its plan. Credentials may be minted even when model calls are denied until credits/entitlements are valid; never trigger purchase without approval.
- **Function env compatibility changed:** [current function instructions](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon-functions/SKILL.md) and [parent](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon/SKILL.md) replace old unguarded `process.env.X!` with explicit `{ value: process.env.X, required: true | false | "default-branch" }`; requirements depend on current `@neon/config`/`neon`/`@neon/env` versions. Missing required values fail before deploy. An empty secret can overwrite/delete a value, and optional/branch-specific omissions require review. Do not copy new syntax into older clients without version checks.
- **Realtime RLS limitation:** [current Realtime skill](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon-realtime/SKILL.md) says live-query subscriptions reject tables protected by row-level security. Do **not** blindly disable RLS on production tables: choose an approved access-control design, use server-authorized sealed queries where applicable, and test user isolation before moving sensitive data.
- **Logs and SDK interfaces drift:** [current Logs/Loki reference](https://github.com/neondatabase/agent-skills/blob/2b0e2b6f56d2b41c5363049e30e6ab72aa260cce/skills/neon/references/logs-loki.md) adds `neon logs loki` (CLI 9.1+), `@neon/sdk` 7.11+ Loki API, and named-parameter object syntax; truncated result limits must not be treated as exhaustive. Log queries can contain private data and production telemetry; review credentials/project/branch and authorized scope.
- This is a bounded complete selected-`skills/` hash/changed-hunk comparison, with eight changed files and 23 change hunks inspected; no Neon API call, database mutation, credential read, billing change, CI, renderer or independent product integration performed. Historical pin remains a historical source; no universal current-freshness marker is advanced for related product claims.

