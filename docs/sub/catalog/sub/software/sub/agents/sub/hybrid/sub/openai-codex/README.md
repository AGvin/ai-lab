# OpenAI Codex

OpenAI Codex is OpenAI's coding agent for writing, reviewing, testing, and shipping software across desktop/ChatGPT, editor, terminal, automation, and delegated cloud workflows. Local Codex surfaces such as the CLI, IDE integration, and desktop workflows can operate on user-controlled files and commands, while delegated cloud tasks run in OpenAI-managed environments.

## Execution and trust boundary

Codex can combine repository/worktree access, shell and external tools, reusable skills/plugins, MCP-connected tools, browser or Computer Use surfaces, connected services, and scheduled or background workflows. Treat repository instructions, generated diffs, credentials and secrets, tool permissions, MCP servers, browser/computer access, connected services, and external actions such as commit, push, deployment, or merge as explicit review boundaries.

Local command execution does not mean all inference or relevant task context remains local. Data-use behavior also depends on the account/workspace context and applicable OpenAI data controls, so plan-specific retention, training, residency, limits, model availability, and feature availability should be verified from current official documentation rather than treated as stable product identity.

## Related

- [OpenAI](../../../../../../../producers/sub/o/sub/openai/) — canonical producer organization.

## Official resources

- [OpenAI Codex](https://openai.com/codex/)
- [Codex developer documentation](https://developers.openai.com/codex)
- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540)
