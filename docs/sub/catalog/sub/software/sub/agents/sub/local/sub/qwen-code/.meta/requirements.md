# Documentation Requirements

## Requirements

- Present Qwen Code as Qwen Team's released open-source agentic coding tool for terminal-based software-development workflows.
- Preserve local-agent placement: its CLI runs on the user's machine, reads/edits repositories and executes tools locally or through configured sandbox/container modes, while model inference can use Alibaba Cloud Model Studio or other configured remote providers.
- Keep Qwen coding models, Qwen Studio, Alibaba Cloud Model Studio, SDK packages, desktop/mobile shells, chat-channel adapters, MCP servers, plugins/extensions and sandbox images as separate model/product/components rather than peer Qwen Code identities.
- Preserve trust boundaries around shell/file access, sandbox configuration, provider credentials, MCP/tools/extensions, external context integrations and autonomous code changes.
- Treat release versions, supported Node/runtime/OS versions, providers, IDE/desktop/channel surfaces, sandbox behavior, SDK packages and subscription/token-plan requirements as freshness-sensitive.
- Preserve current open-source/license and stable-release state only while first-party repository evidence supports it.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Qwen Code remains installable coding-agent software rather than a trained Qwen model.
- Local tool execution is not conflated with local model inference.
- Producer provenance resolves bidirectionally to Qwen Team.
