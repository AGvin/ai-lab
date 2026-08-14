# Cursor

Cursor is Anysphere, Inc.'s AI-first code editor and development environment. Its primary canonical identity is an editor, while agent workflows extend that editor across local and hosted execution surfaces.

## VS Code foundation and customization

Cursor is based on the VS Code codebase, so the [Visual Studio Code](../vs-code/) profile is useful upstream context for editor behavior and VS Code's Agent Customization model. Treat that customization guidance as background compatibility context rather than a 1:1 contract: Cursor has its own rules, skills, plugins, MCP, subagents, commands, and hooks surface, and individual formats or features can differ.

## Execution and data boundary

Cursor supports editor Agent workflows, CLI use, rules and Agent Skills, plugins, MCP integrations, and remote/background or cloud-agent execution. Those surfaces do not share one execution boundary: local editor operations, hosted agents, and remote model inference should be evaluated separately.

AI requests may pass through Cursor infrastructure and downstream model providers, and codebase indexing or agent workflows can expose repository context beyond the local process. Privacy Mode changes data-handling guarantees but should not be interpreted as a fully local request path. Review repository access, indexing, selected providers, hosted execution, shell/tool permissions, skills/plugins/MCP, secrets, and generated diffs before using sensitive code.

## Related

- [Visual Studio Code](../vs-code/) — upstream editor foundation and Agent Customization reference; use it as compatibility context rather than assuming identical agent-customization behavior.
- [Anysphere, Inc.](../../../../../../../producers/sub/a/sub/anysphere-inc/) — canonical producer organization.
- [Extensions](./sub/extensions/) — Cursor-owned extension navigation when materialized.

## Official resources

- [Cursor](https://cursor.com/)
- [Documentation](https://cursor.com/docs)
- [Privacy](https://cursor.com/privacy)
- [Security](https://cursor.com/security)
- [Terms of Service](https://cursor.com/terms-of-service)
