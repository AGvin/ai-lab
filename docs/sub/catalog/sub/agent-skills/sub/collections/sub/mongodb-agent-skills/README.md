# MongoDB Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Relations

- Produced by: [MongoDB](../../../../../producers/sub/m/sub/mongodb/)

MongoDB Agent Skills is MongoDB's official portable instruction collection for agent-assisted database work, including query and schema design, indexing, optimization, Atlas Search and Vector Search.

## Scope and boundaries

The same collection is distributed through the `mongodb-atlas` plugin, the self-managed `mongodb` plugin and standalone skills installation. The Atlas route connects to MongoDB-hosted MCP using OAuth; the self-managed route runs an MCP server locally for the user's deployment. Instruction files alone do not configure a live connection or grant credentials.

The repository uses Apache 2.0. That license concerns the collection, not every connected database, hosted service or coding agent. Inspect the current skills and client compatibility and configure database access for the intended deployment. A skill's advice does not verify permissions, and each skill directory or plugin manifest does not become a separate product identity.

## Source interpretation

MongoDB's Apache-2.0 collection has an Atlas plugin connecting to MongoDB-hosted MCP through OAuth and a separate self-managed plugin running MCP locally. Standalone skills do not establish either connection. Query/schema advice remains separate from database authorization, deployment compatibility and review of generated write operations.

[Reviewed original README](https://github.com/mongodb/agent-skills/blob/155bb9c4b42a9a3e019f47be0669de0e4547d1ea/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [MongoDB Agent Skills repository](https://github.com/mongodb/agent-skills)
- [MongoDB Agent Skills documentation](https://www.mongodb.com/docs/agent-skills/)
