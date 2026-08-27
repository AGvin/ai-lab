# Documentation Requirements

## Requirements

- Use the reader-facing title `Model Context Protocol` and treat this node as the canonical learning entrypoint for understanding, using, building, testing, and operating MCP integrations.
- Begin with a plain-language explanation of what problem MCP solves and how hosts, clients, and servers relate, then link the reusable abstract MCP concept and formal MCP specification as separate owners.
- Distinguish MCP from ordinary application APIs, direct function/tool definitions, Agent Skills, and host-specific Plugins; explain how they can complement one another.
- Make the materialized `using-mcp/` and `building-mcp-servers/` children discoverable and explain what each reader will learn.
- Keep exact protocol-version rules, message/schema requirements, normative authorization behavior, and other conformance language sourced from the formal specification rather than frozen as independent learning truth.
- Keep concrete server/client/SDK/product identities and mutable compatibility/support facts with applicable catalog/platform/evidence owners.
- Preserve a clear continuation path for later selected MCP learning children such as architecture/lifecycle, primitives, clients, authorization/security, testing/debugging, and deployment/operations without materializing empty nodes now.

## Validation

- The entrypoint is useful to a first-time MCP learner while accurately routing advanced builders/operators.
- It does not duplicate the formal protocol specification or concrete implementation catalog.
- Standard direct-child navigation includes only currently materialized learning children.
