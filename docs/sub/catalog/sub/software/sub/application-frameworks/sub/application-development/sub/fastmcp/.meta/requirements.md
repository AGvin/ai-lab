# Documentation Requirements

## Requirements

- Identify the actively maintained standalone FastMCP Python framework under `PrefectHQ/fastmcp` (Apache-2.0) for declaring typed MCP tools, resources, prompts, MCP servers, clients and MCP-app integration. Distinguish it from the similarly named high-level `mcp.server.fastmcp` convenience layer historically adopted into the official MCP Python SDK.
- Preserve separate installable library identity and Prefect producer from managed Prefect Horizon hosted MCP deployment. Running Python HTTP/stdio servers is self-managed FastMCP; using Horizon adds distinct provider-operated infrastructure without transferring ownership of locally deployed servers.
- Pin actual FastMCP major/minor release, MCP protocol version, Python compatibility, transport (stdio, Streamable HTTP or legacy SSE), OAuth/authentication and tool-schema serialization. The v3/v4 release documentation has changed in 2026; do not rely on outdated legacy examples as the current interface.
- Do not treat framework tool decorator metadata as automatic permission to access private services. Enforce per-user authority and safe handling of tool results; verify registry/tool provenance before agent invocation.
- Keep Apache 2.0 source license and Prefect project's official attribution distinct from separately licensed hosted platforms and integrated community MCP server authors.

## Validation

- The first-party maintained source or documentation demonstrates released installable functionality and exact source/build identity.
- Version-sensitive protocol, license and hosted deployment distinctions remain explicit.
- Exact reciprocal `produced-by` / `produces` source-of-truth relation resolves to an existing or concurrently created producer.
