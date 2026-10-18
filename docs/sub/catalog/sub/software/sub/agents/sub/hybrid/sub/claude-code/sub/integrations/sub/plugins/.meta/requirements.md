# Documentation Requirements

## Requirements

- Document Claude Code-specific plugin support as mutable software/product facts from current official Anthropic documentation.
- Cover current package/manifest structure, installation and discovery, marketplaces, supported plugin components such as commands/hooks/agents/skills/MCP integrations when source-backed, permissions, lifecycle, and compatibility.
- Keep exact paths, manifest fields, commands, marketplace rules, load/update behavior, supported components, and compatibility current-source-backed because they may change.
- Distinguish Claude Code's product-specific plugin contract from the vendor-neutral Agent Plugins standard unless official documentation explicitly states conformance/interoperability.
- Keep generic plugin concept, trust, lifecycle, adoption, removal, and portability teaching with selected concept/learning owners.

- Preserve the distinction between the interactive `/plugin install` review panel and direct shell installation, and between a shared project enablement entry and downloading a plugin on each collaborator's machine.
- Explain that plugin code runs with user privileges, that install scope controls visibility, and that changes need the applicable reload/session lifecycle; local settings are not automatically inherited by cloud sessions.

## Validation

- Current Claude Code plugin behavior is supported by current official Anthropic documentation.
- Vendor-specific fields are not presented as universal Agent Plugins requirements.
- Generic plugin pedagogy is not duplicated.
