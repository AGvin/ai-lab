# OpenAI Codex Plugins

Codex plugins package capabilities such as skills, MCP connections, and optional hooks. Codex shares a plugin catalog with ChatGPT, while execution behavior belongs to the active Codex client.

## Client and execution boundaries

The Codex desktop app provides plugin browsing and management; the CLI exposes `/plugins`. The Codex IDE extension does not currently support plugins. Install the desired package through a supported client, then start a new chat or session for its capabilities to become available. Invoke the installed skills or connected tools in that session.

Codex sandbox and approval controls apply to its execution environment. External services retain separate authentication and permissions. Local hooks and executable capabilities require the appropriate host environment; their availability should not be inferred for ChatGPT's cloud-orchestrated work.

Review package provenance and granted access before use. Removing a plugin does not necessarily disconnect an MCP connection that was established separately. Skills, MCP connections, repository instructions, and plugins remain distinct mechanisms; shared catalog lifecycle and portable package semantics are documented by their owners below.

## Related

- [Shared ChatGPT plugin catalog](../../../../../../../../../../../services/sub/assistant-workspaces/sub/chatgpt/sub/integrations/sub/plugins/)
- [Agent Plugins specification](../../../../../../../../../../../specifications/sub/formats/sub/agent-plugins/)

## Official resources

- [Plugins in ChatGPT and Codex](https://learn.chatgpt.com/docs/plugins)
- [Build plugins](https://learn.chatgpt.com/docs/build-plugins)
