# MCP Inspector

MCP Inspector is the official development and debugging tool for Model Context Protocol servers, distributed through `@modelcontextprotocol/inspector`.

## Product scope

The v2 package includes Web UI, CLI and TUI, plus experimental `mcpdo` persistent-connection tooling. It inspects server capabilities, tools, resources, prompts and authentication; it does not certify protocol conformance or replace an independent security review.

## Operational boundaries

The canonical release record is v2.11.0 (2026-10-14). Confirm v1 versus v2 tooling and protocol support. On machines lacking an OS keychain, the project warns that `~/.mcp-inspector/secrets.json` may be stored without encryption unless a key is configured. Protect OAuth credentials, avoid public UI binding and review commands executed through stdio servers. The source-license transition includes MIT, Apache-2.0 and separately licensed documentation portions.

## Relations

- Maintained by: [Agentic AI Foundation](../../../../../../../producers/sub/a/sub/agentic-ai-foundation/)

## Official resources

- [First-party reference](https://github.com/modelcontextprotocol/inspector)
