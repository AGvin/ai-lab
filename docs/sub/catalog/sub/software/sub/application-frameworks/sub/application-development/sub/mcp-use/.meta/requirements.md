# Documentation Requirements

## Requirements

- Identify mcp-use as the actively developed standalone TypeScript MCP application and server framework providing typed tool definitions, MCP Apps/interactive views, testing/Inspector integration and SDK patterns for ChatGPT/Claude-compatible clients, not as the MCP protocol standard itself.
- Preserve v2 TypeScript framework identity and official migration from earlier v1 APIs; the npm create-app/SDK tooling and developer Inspector are project features, not independently maintained services without a separate lifecycle and owner.
- Distinguish mcp-use's MCP Apps/UI surface from the official MCP Inspector release, FastMCP Python servers and Arcade MCP Python authorized tool library. A supported client label does not imply endorsement or equal UI extension support across every host.
- Pin framework version, compatible SDK/client capabilities, auth, transports, tool schemas, sandbox/embedding behavior and UI rendering restrictions; avoid placing raw secrets in view props or model-readable tool definitions.
- Treat one mcp-use publisher/team as owner of its toolkit; any hosted deployment integrations or third-party MCP servers remain separately owned.

## Validation

- The first-party maintained source or documentation demonstrates released installable functionality and exact source/build identity.
- Version-sensitive protocol, license and hosted deployment distinctions remain explicit.
- Exact reciprocal `produced-by` / `produces` source-of-truth relation resolves to an existing or concurrently created producer.
