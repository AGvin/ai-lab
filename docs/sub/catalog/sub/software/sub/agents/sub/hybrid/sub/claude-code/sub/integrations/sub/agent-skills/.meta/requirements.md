# Documentation Requirements

## Requirements

- Document Claude Code-specific Agent Skills support as mutable software/product facts.
- Cover current personal, project, managed, and plugin-provided skill locations or scopes; discovery; automatic and explicit invocation; namespacing; permissions or tool restrictions; and installation/removal behavior when source-backed.
- Distinguish Claude Code Agent Skills from plugins, slash commands, subagents, hooks, MCP, and CLAUDE.md instructions while explaining supported composition points where relevant.
- Keep exact paths, commands, frontmatter fields, precedence rules, plugin behavior, and availability current-source-backed because they may change.
- Link the canonical Agent Skills concept and portability learning owner for reusable semantics and cross-host practices.

- Preserve the documented distinction between `allowed-tools` turn-scoped pre-approval and an actual tool restriction; normal permissions still govern unlisted tools, and managed policy can suppress skill grants.
- Explain removal at the source scope and distinguish local personal skills from skills available in cloud sessions; removing discovery does not erase instructions already loaded into the conversation.

## Validation

- Current Claude Code-specific behavior is supported by current official Anthropic documentation.
- Generic Agent Skills authoring or portability teaching is not duplicated.
