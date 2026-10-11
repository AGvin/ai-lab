# Documentation Requirements

## Requirements

- Identify MongoDB Agent Skills as MongoDB's first-party portable instruction collection for query design, schema design, indexing, query optimization, MongoDB Atlas Search and Vector Search.
- Preserve the official collection as one maintained identity even when distributed through the `mongodb-atlas` cloud plugin, the `mongodb` self-managed plugin, or standalone `npx skills add mongodb/agent-skills` installation.
- Distinguish MCP server connection/authentication setup from the instruction files; standalone skills installation alone does not configure the MCP server or grant database credentials.
- Track MongoDB Community/Enterprise Advanced and Atlas deployment differences, data-access permissions, client compatibility, skill inventory and security guidance as mutable.
- Do not materialize each skill folder, plugin manifest or bundled database feature as a new canonical product.
- Attribute primary collection maintenance to MongoDB and preserve reciprocal producer links.

## Validation

- The collection remains distinct from MongoDB's database/server software, managed Atlas service and MCP integration.
- Model and agent advice about database access does not imply verified credentials or permissions.
- Official upstream documentation matches the current collection identity.
- The `produced-by` and `produces` relations are reciprocal.
