# Cline

Cline is an open-source coding agent whose current product surface spans IDE/editor integration, a CLI, SDK-based use, and automation-oriented workflows. It can inspect project context, edit files, run terminal commands, use browser or network-capable tools, and connect external capabilities through MCP and related extensions.

## Execution boundary

Cline runs in user-controlled development environments rather than as a primarily hosted agent service. The same agent runtime can be exposed through interactive editor/terminal use or headless and scheduled automation, so unattended execution increases the importance of explicit repository, shell, filesystem, network, credential, and tool boundaries.

Treat repository instructions and rules, generated diffs, provider credentials, MCP servers, browser/network access, filesystem permissions, shell commands, and unattended automation as review and trust boundaries. Approval controls reduce accidental actions but are not a universal security guarantee.

## Official resources

- [Cline](https://cline.bot/)
- [Cline documentation](https://docs.cline.bot/cline-overview)
- [Cline repository](https://github.com/cline/cline)
- [Cline Bot Inc.](../../../../../../../producers/sub/c/sub/cline-bot-inc/)
