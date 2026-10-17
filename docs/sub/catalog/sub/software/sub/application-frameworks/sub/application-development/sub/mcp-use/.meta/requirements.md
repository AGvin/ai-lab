# Documentation Requirements

## Requirements

- Identify mcp-use as the open-source MCP framework with TypeScript and Python SDKs for servers, clients, agents and applications. Preserve its independent framework identity and distinguish it from the MCP protocol standard.
- Preserve the TypeScript v2 migration from earlier v1 APIs without applying that version label to the Python SDK. Language-specific APIs, interactive-view support and release histories must remain explicit; npm scaffolding, SDK tooling and Inspector integration do not by themselves establish new product identities.
- Distinguish mcp-use's MCP Apps/UI surface from the official MCP Inspector release, FastMCP Python servers and Arcade MCP Python authorized tool library. A supported client label does not imply endorsement or equal UI extension support across every host.
- Pin framework version, compatible SDK/client capabilities, auth, transports, tool schemas, sandbox/embedding behavior and UI rendering restrictions; avoid placing raw secrets in view props or model-readable tool definitions.
- Identify Manufact, Inc. as the current company/team behind mcp-use using first-party company and product sources. Preserve the mcp-use software name and stable producer ID; Manufact Cloud is a separate operated service, and third-party MCP servers and model providers retain their own identities.

## Validation

- The first-party maintained source or documentation demonstrates released installable functionality and exact source/build identity.
- Version-sensitive protocol, license and hosted deployment distinctions remain explicit.
- Exact reciprocal `produced-by` / `produces` source-of-truth relation resolves to an existing or concurrently created producer.
