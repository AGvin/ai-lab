# Model Context Protocol

Model Context Protocol (MCP) is a versioned formal interoperability protocol defined by its first-party specification and schema.

## Current specification boundary

The current verified research baseline is revision `2026-07-28`. In that revision, the core uses JSON-RPC 2.0 with stateless, self-contained client requests carrying protocol version and client capabilities in `_meta`. The former required `initialize` / `notifications/initialized` handshake and protocol-level session model belong to earlier compatibility paths rather than the modern core.

Current version selection uses `server/discover` or direct requests with unsupported-version handling. Server needs for extra client input use the Multi Round-Trip Request pattern instead of server-initiated JSON-RPC requests. Core server feature vocabulary includes Resources, Prompts, and Tools. Roots, Sampling, and Logging are deprecated for new implementations under the current revision; legacy HTTP+SSE and Dynamic Client Registration also remain backward-compatibility paths rather than preferred new design.

The standard transport bindings are stdio and Streamable HTTP, while custom transports may preserve the protocol message contract. HTTP authorization is optional overall and, when supported, follows the MCP authorization specification; stdio uses environment-supplied credentials instead of the HTTP flow. Optional extensions remain distinct from the core protocol.

Exact methods, fields, headers, error codes, capability objects, transport details, authorization behavior, deprecations, and extensions remain revision-sensitive and should be read from the active first-party specification/schema.

## Official resources

- [MCP 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP 2026-07-28 schema](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2026-07-28/schema.json)
- [MCP repository](https://github.com/modelcontextprotocol/modelcontextprotocol)
