# Agent Plugins

Agent Plugins is an open, vendor-neutral, versioned portable plugin package specification.

## Specification boundary

The portable contract is defined by the current Agent Plugins specification and includes a required plugin manifest plus the standard's package component and reference surfaces. Exact filenames, fields, schema constraints, validation behavior, versions, and extension rules are versioned specification facts.

Agent Skills and Model Context Protocol artifacts remain separate formal contracts. Client-specific packaging, marketplaces, commands, hooks, permissions, discovery, lifecycle behavior, or other extensions in Claude Code, Cursor, OpenCode, OpenAI products, and other hosts must not be generalized into portable Agent Plugins behavior.

## Official resources

- [Agent Plugins specification](https://agent-plugins.org/specification)
- [Agent Plugins specification repository](https://github.com/agentplugins/agent-plugins-spec)
