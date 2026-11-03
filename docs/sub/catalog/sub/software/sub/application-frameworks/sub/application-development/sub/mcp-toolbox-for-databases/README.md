# MCP Toolbox for Databases

MCP Toolbox for Databases is a Google Cloud–origin, open-source server and framework for exposing database-backed tools to AI applications and Model Context Protocol (MCP) clients. It supports prebuilt database toolsets as well as custom tool definitions backed by configured data sources. The original `genai-toolbox` repository was renamed to `mcp-toolbox`; those names refer to one project, not two products.

## Integration workflow

For development-oriented database exploration, a compatible MCP client can launch a local Toolbox server with a prebuilt toolset, for example using the server package `@toolbox-sdk/server` with `--prebuilt=postgres` and `--stdio`. For application-specific tools, operators define database `sources` and accessible `tools` in `tools.yaml`, then start the server with `npx @toolbox-sdk/server --config tools.yaml`. Tool definitions and source adapters are part of the server's configurable surface; separately released language SDKs and managed Google Cloud MCP servers have their own release boundaries.

Toolbox supports both Google Cloud databases and independently hosted or third-party database systems. A Google Cloud account is not inherently required for self-hosted connections that do not depend on Google Cloud resources. Choose a pinned release and compatible adapter/toolset for the actual database and MCP client. The documented behavior was reviewed at source commit `b9b96ba4c31012db51024dd7ddabf1bd83aa18d7` (2026-11-03); no database connection, SQL query or runtime compatibility test was executed for this catalog entry.

## Access, safety, and operations

**An MCP database connection gives AI-driven tools real data access.** Generic `execute_sql` tools can expose confidential records or change production state if database permissions allow it. Use the minimum required database privileges, preferably read-only for exploration; restrict the exposed tools and SQL operations; separate development and production environments; enforce connection/network restrictions, authentication and timeouts; and monitor tool activity.

Do not put database passwords in a shared `tools.yaml` or repository example. Configure credentials through an approved secret-management mechanism. Features such as connection pooling, OAuth/OIDC integrations and telemetry require deliberate deployment configuration; an MCP interface does not supply a universal security boundary. Source repositories and their Apache-2.0 software license do not grant rights over user data or third-party database contents.

## Relations

- Produced by: [Google Cloud](../../../../../../../producers/sub/g/sub/google-cloud/) — origin and project stewardship.
- Related: [Application Development Frameworks](../../) — category, distinct from database storage engines.

## Official resources

- [MCP Toolbox source](https://github.com/googleapis/mcp-toolbox)
- [Documentation](https://mcp-toolbox.dev/)
- [Google Cloud launch and provenance](https://cloud.google.com/blog/products/ai-machine-learning/mcp-toolbox-for-databases-now-supports-model-context-protocol)
- [Pinned Apache-2.0 license](https://github.com/googleapis/mcp-toolbox/blob/b9b96ba4c31012db51024dd7ddabf1bd83aa18d7/LICENSE)
