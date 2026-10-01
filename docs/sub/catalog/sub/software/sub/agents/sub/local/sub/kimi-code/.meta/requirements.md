# Documentation Requirements

## Requirements

- Present Kimi Code as Moonshot AI's released installable coding-agent suite for terminal and IDE workflows, including Kimi Code CLI and supported IDE integrations.
- Preserve local-agent placement: repository/file inspection, shell/tool execution, code edits and local session state operate in user-controlled development environments even when model inference uses Kimi-hosted or configured remote providers.
- Keep Kimi coding models, Kimi hosted assistant, Kimi Work, Kimi Claw, third-party provider models, MCP servers, plugins, Agent Skills, hooks and IDEs as separate model/product/integration owners.
- Preserve trust boundaries around repository/file access, shell commands, hooks/plugins/skills, MCP servers, credentials, remote control, subagents, generated diffs and external side effects.
- Treat model routing, membership/usage limits, release versions, supported IDEs, remote-control behavior, plugin/skill inventory, model context and third-party client/provider compatibility as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Kimi Code remains coding-agent software rather than a Kimi trained model.
- Local tool execution is not described as proof that inference or all task data stays local.
- Producer provenance resolves bidirectionally to Moonshot AI.
