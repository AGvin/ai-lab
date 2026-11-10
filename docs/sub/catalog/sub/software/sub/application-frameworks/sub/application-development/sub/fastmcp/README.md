# FastMCP

FastMCP is an Apache-2.0-licensed Python framework for constructing MCP servers, clients, typed tools, resources and prompts.

## Scope and capabilities

The separately published Prefect-maintained FastMCP library is distinct from the similarly named convenience layer in the official MCP Python SDK. Server/client and MCP Apps integrations remain features of the framework.

## Deployment and safety boundaries

Running FastMCP locally is not equivalent to hosted Prefect Horizon infrastructure. Review Python, transport and MCP protocol compatibility for the selected major release; some 2026 examples differ across major versions. Verify OAuth and tool permissions and treat remote tool output as untrusted.

## Relations

- Produced by: [Prefect Technologies, Inc.](../../../../../../../producers/sub/p/sub/prefect-technologies-inc/)

## Official resources

- [Source repository](https://github.com/PrefectHQ/fastmcp)
- [Documentation](https://gofastmcp.com/)
