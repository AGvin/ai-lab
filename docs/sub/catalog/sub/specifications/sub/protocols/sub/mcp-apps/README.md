# MCP Apps

**MCP Apps** is the official optional Model Context Protocol extension for serving interactive user-interface resources from MCP tools to supporting host applications. The stable published extension revision is **2026-01-26**, with extension identifier `io.modelcontextprotocol/ui`. It is an extension of MCP, not a mandatory core capability. [MCP Apps stable specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx).

## Protocol boundary

MCP servers expose `ui://` resources associated with tools through extension metadata. A compatible host discovers and renders the resource in an isolated view and exchanges messages with it through the specified JSON-RPC-based app/host communication protocol. Clients and servers negotiate optional support, so an MCP connection without Apps capability must not be assumed to render embedded interfaces.

The actual tool-to-resource metadata, URI rules, message types, capability markers and security controls are versioned by the extension specification. MCP Apps is distinct from general application UI, SDK-specific MCP-UI implementations, the OpenAI Apps SDK and independent agent UI protocols.

## Trust and compatibility

A host controls isolation, content-security policy, tool visibility and the authority delegated to embedded UI code. Rendering an MCP App does not make its third-party HTML, network access, tool calls, cookies or data handling automatically safe. Individual products may support only part of the extension or apply additional authorization; check their current releases before assuming portability.

## Official resources

- [MCP Apps stable specification (2026-01-26)](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx)
- [Official extension repository](https://github.com/modelcontextprotocol/ext-apps)
- [Stable extension release announcement](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)
