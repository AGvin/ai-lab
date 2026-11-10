# MongoDB Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Relations

- Produced by: [MongoDB](../../../../../producers/sub/m/sub/mongodb/)

MongoDB Agent Skills is MongoDB's official portable instruction collection for agent-assisted database work, including query and schema design, indexing, optimization, Atlas Search and Vector Search.

## Scope and boundaries

The same collection is distributed through the `mongodb-atlas` plugin, the self-managed `mongodb` plugin and standalone skills installation. The Atlas route connects to MongoDB-hosted MCP using OAuth; the self-managed route runs an MCP server locally for the user's deployment. Instruction files alone do not configure a live connection or grant credentials.

The repository uses Apache 2.0. That license concerns the collection, not every connected database, hosted service or coding agent. Inspect the current skills and client compatibility and configure database access for the intended deployment. A skill's advice does not verify permissions, and each skill directory or plugin manifest does not become a separate product identity.

## MCP access, write permissions and data exposure

The Atlas plugin's [pinned MCP configuration](https://github.com/mongodb/agent-skills/blob/155bb9c4b42a9a3e019f47be0669de0e4547d1ea/plugins/mongodb-atlas/.claude-plugin/plugin.json) uses MongoDB's hosted `https://mcp.mongodb.com/` endpoint over OAuth, not a local-only connection. Agent tool calls can query data or manage Atlas resources within the permissions allowed by the signed-in user and organization AI-client policy. Check the connected project, role, data sensitivity and agent/provider data flow before granting access. See [MongoDB's managed MCP access policy](https://www.mongodb.com/docs/mcp-server/remote-mcp/manage-ai-client-access/).

For the **local/self-managed MCP server**, MongoDB documents that write-capable operations are permitted by default. For production or sensitive database inspection, configure `--readOnly` or `MDB_MCP_READ_ONLY=true` **and** a dedicated database user with a read-only role. Review and authorize changes to data, indexes, database users, network settings or clusters separately; an agent-generated suggestion is not that authorization. Store connection strings and service-account credentials outside prompts, logs and version control, and restrict file permissions and access lists. Review local MCP telemetry separately; an installed skill is not proof of offline processing. See [MongoDB MCP security guidance](https://www.mongodb.com/docs/mcp-server/local-mcp/security-best-practices/) and [configuration options](https://www.mongodb.com/docs/mcp-server/local-mcp/configuration/options/).

## Source interpretation

MongoDB's Apache-2.0 collection has an Atlas plugin connecting to MongoDB-hosted MCP through OAuth and a separate self-managed plugin running MCP locally. Standalone skills do not establish either connection. Query/schema advice remains separate from database authorization, deployment compatibility and review of generated write operations.

[Reviewed original README](https://github.com/mongodb/agent-skills/blob/155bb9c4b42a9a3e019f47be0669de0e4547d1ea/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [MongoDB Agent Skills repository](https://github.com/mongodb/agent-skills)
- [MongoDB Agent Skills documentation](https://www.mongodb.com/docs/agent-skills/)
