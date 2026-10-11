# Documentation Requirements

## Requirements

- Identify Neon Agent Skills as a released first-party portable Agent Skills collection for Neon/Lakebase Postgres, database branches, authentication, object storage, API gateways and developer-agent workflows.
- Preserve the single canonical collection identity despite the optional Agent Plugins v1 packaging and separate Claude, Cursor, Kimi, Pi and other client-specific manifests. The Neon MCP server is an integration, not another collection or a product-identical skill.
- Keep the independently linked Neon-for-agent-platforms repository and its packages separate unless evidence establishes they belong to the same maintained distribution. Do not reassign independently authored companion workflows automatically.
- Treat skill count, names, Postgres and Auth capabilities, documentation URLs, underlying Databricks product branding, supported clients, plugin declarations and installation guidance as freshness-sensitive.
- Installing a skill does not establish an authenticated database connection or authorize credentials/deployment operations; preserve tool permission and runtime validation boundaries.
- Preserve source-backed first-party producer provenance with a reciprocal `produces` relation.

## Validation

- The collection is independently maintained as a public upstream skill distribution.
- Client-specific plugin/MCP packaging and the collection's individual SKILL.md files are not duplicated as separate canonical products.
- Current compatibility, version and feature statements derive from first-party release documentation.
- The producer's inverse relation matches the collection identity.
