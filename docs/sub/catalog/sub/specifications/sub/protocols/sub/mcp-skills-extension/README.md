# MCP Skills Extension

**MCP Skills Extension** is the official stable optional Model Context Protocol extension, `io.modelcontextprotocol/skills`, for discovering and delivering portable Agent Skills through an MCP connection. It is defined in the accepted SEP-2640 and the official extension specification for MCP **2026-07-28** and later. [Stable Skills extension specification](https://github.com/modelcontextprotocol/ext-skills/blob/main/specification/stable/skills.mdx).

## Extension versus portable skill format

This extension defines MCP resource-based discovery and delivery of skill packages. The canonical [Agent Skills format](../../../formats/sub/agent-skills/) owns the `SKILL.md` package content and metadata contract; the MCP Skills Extension owns how supporting clients and servers find, advertise and retrieve those packages.

Stable specification details cover resource URLs including `SKILL.md`, resource/digest inventories or a `dynamic` indicator, discovery metadata and negotiated support. Exact URI patterns, metadata keys, digest behavior, version and compatibility are specification-scoped. Deprecated experiments are not automatically part of this released extension.

## Security and execution boundary

Listing or retrieving a skill does not authorize code execution, local helper installation, credential access or privileged external actions. An MCP client must enforce its own consent, integrity verification, untrusted-instruction handling and tool-permission policies. Vendor-specific skill registries, OpenAI plugin behavior and SDK integration details remain separate product concerns.

## Official resources

- [Stable MCP Skills specification](https://github.com/modelcontextprotocol/ext-skills/blob/main/specification/stable/skills.mdx)
- [Official extension repository](https://github.com/modelcontextprotocol/ext-skills)
- [Accepted SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension)
