# OpenAI Codex

OpenAI Codex is OpenAI's coding agent for writing, reviewing, testing, and shipping software across desktop/ChatGPT, editor, terminal, automation, and delegated cloud workflows. Local Codex surfaces such as the CLI, IDE integration, and desktop workflows can operate on user-controlled files and commands, while delegated cloud tasks run in OpenAI-managed environments.

## Execution and trust boundary

Codex can combine repository/worktree access, shell and external tools, reusable skills/plugins, MCP-connected tools, browser or Computer Use surfaces, connected services, and scheduled or background workflows. Treat repository instructions, generated diffs, credentials and secrets, tool permissions, MCP servers, browser/computer access, connected services, and external actions such as commit, push, deployment, or merge as explicit review boundaries.

Local command execution does not mean inference or relevant task context remains local. In **Codex Cloud**, a published project environment prepares repositories and dependencies for tasks on OpenAI-managed computers; each new task receives its own isolated workspace and does not recover another task's uncommitted changes. Saved VM recovery windows are separate from conversation retention. Some Code Review, Security Review, GitHub and Linear integration workflows continue on **Codex Cloud (Legacy)** during migration, rather than sharing the current cloud-task environment lifecycle.

Data-use controls depend on the personal or managed workspace. Personal-workspace training opt-out covers new Codex task content, while the distinct Codex **Include environments** setting controls use of additional full-environment context and is not changed by the ChatGPT toggle. Business, Enterprise and Edu content is excluded from training by default, subject to documented organizational settings. Environment sharing, injected secrets, repo credentials, cloud network access, model availability, limits, retention and residency require current first-party checks.

## Related

- [OpenAI](../../../../../../../producers/sub/o/sub/openai/) — canonical producer organization.

## Official resources

- [OpenAI Codex](https://openai.com/codex/)
- [Codex developer documentation](https://developers.openai.com/codex)
- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540)
- [Using Codex Cloud and its task environments](https://help.openai.com/en/articles/20001545-using-codex-cloud)
- [Codex and ChatGPT data controls](https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt)
