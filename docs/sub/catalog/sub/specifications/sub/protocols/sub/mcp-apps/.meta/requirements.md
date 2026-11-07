# Documentation Requirements

## Requirements

- Present MCP Apps as the stable official Model Context Protocol extension for interactive user interfaces delivered by MCP servers/tools to supporting hosts.
- Keep MCP Apps explicitly distinct from MCP core. The verified stable extension revision is `2026-01-26`; re-check the official extension specification before changing exact metadata fields, URI rules, message shapes, capability negotiation, or security requirements.
- Preserve the extension identity `io.modelcontextprotocol/ui` and its core interoperability boundary: UI resources are declared with the `ui://` URI scheme, associated with tools through extension metadata, and communicate bidirectionally with the host using the MCP JSON-RPC base protocol.
- Preserve the security boundary from the active specification, including host-controlled isolated rendering/sandboxing and auditable communication, without turning implementation-specific browser behavior into timeless protocol truth.
- Treat MCP Apps as an optional backwards-compatible MCP extension; do not promote its methods/metadata into the canonical MCP core node.
- Keep concrete host/client support, SDK implementation behavior, example apps, framework integrations, rendering bugs, and deployment guidance with their applicable software/service/learning owners.
- Keep related but distinct UI protocols/specifications such as AG-UI or A2UI separate when they independently pass lifecycle and intake gates.

## Validation

- MCP Apps is not described as MCP core.
- Exact normative details are traceable to the current first-party extension specification with a visible revision boundary.
- The node does not become a host support matrix, SDK tutorial, or generic generative-UI concept page.

## Scoped original-source qualification — 2026-11-07

- MCP Apps is the official optional **stable 2026-01-26** Model Context Protocol UI extension `io.modelcontextprotocol/ui`, distinct from MCP core and from specific implementations such as the OpenAI Apps SDK or the MCP-UI project.
- First-party specification documents `ui://` resources, tool-to-UI metadata, optional capability negotiation, bidirectional iframe/host JSON-RPC communication and host-controlled isolation. Its sandbox, CSP and allowed tool-call boundary do not make arbitrary third-party HTML, data processors, credentials or host implementations automatically trusted or conformant.
- Verified first-party source 1: https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx
- Verified first-party source 2: https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/
- Verified first-party source 3: https://github.com/modelcontextprotocol/ext-apps
- Existing extension identity/source qualified only. No MCP server, browser iframe, host UI, tool execution or security penetration test was run; reader is currently absent without repair credit. No full legal/privacy/security/rights review, root-wide schema/cache/CI/render, clean pass or final gate.
