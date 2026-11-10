# Documentation Requirements

## Requirements

- Present the MCP Skills Extension as the stable official Model Context Protocol extension identified by `io.modelcontextprotocol/skills` for discovery and delivery of Agent Skills through MCP.
- Keep the extension distinct from the Agent Skills format/specification itself: Agent Skills owns the portable skill package/instruction format, while this node owns the MCP transport/discovery binding.
- Preserve the stable extension boundary from SEP-2640 and the official stable specification, including its use of MCP resources and negotiated extension support, without importing superseded experimental working-group designs into current normative behavior.
- Treat exact methods, resource URI conventions, metadata fields, discovery/index behavior, limits, digests, tool associations, and compatibility requirements as version-sensitive normative state that must be re-checked against the current first-party stable specification.
- Keep concrete client/server support, OpenAI plugin behavior, FastMCP or SDK implementations, individual skill collections, registries, installation workflows, and implementation bugs with their applicable catalog/software/service/learning owners.
- Preserve the distinction between serving skills over MCP and executing arbitrary local helper code; do not infer executable-code semantics beyond the stable extension specification.

## Validation

- The node does not duplicate the canonical Agent Skills format node.
- Stable status is traceable to the official extension repository/specification and accepted SEP-2640.
- Historical experimental Skills-over-MCP proposals are not restated as current normative requirements.

## Scoped original-source qualification — 2026-11-07

- The MCP Skills Extension is the stable official optional MCP extension `io.modelcontextprotocol/skills`, based on accepted SEP-2640, targeting core MCP revision `2026-07-28` or later. It exposes portable Agent Skills as discoverable resource-backed entries through an MCP connection. The Agent Skills `SKILL.md` packaging contract and individual client execution policy remain separate.
- The stable extension specifies `SKILL.md` URIs, complete resource/digest listings or the `dynamic` marker, discovery metadata and client verification/consent. Serving or listing a skill does not authorize arbitrary code execution, external tool permissions, or acceptance of untrusted instructions; actual host support and safety controls must be separately verified.
- Verified first-party source 1: https://github.com/modelcontextprotocol/ext-skills/blob/main/specification/stable/skills.mdx
- Verified first-party source 2: https://github.com/modelcontextprotocol/ext-skills
- Verified first-party source 3: https://modelcontextprotocol.io/seps/2640-skills-extension
- Existing extension identity and bounded official stable specification accepted only; no MCP server/client session, skill loading/execution, independent security/legal review, repository-wide schema/cache/CI/render, clean pass or final gate. No reader page currently present (uncredited).
