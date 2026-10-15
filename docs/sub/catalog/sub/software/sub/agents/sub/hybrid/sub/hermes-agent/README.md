# Hermes Agent

Hermes Agent is Nous Research's open-source personal AI agent spanning self-managed execution and vendor-managed Hermes Cloud instances. The same agent core supports CLI, desktop and messaging access, persistent memory, reusable skills, scheduled tasks, subagent delegation, MCP-connected tools, and configurable model providers.

## Persistence and execution boundary

Hermes can run in user-controlled local, containerized, SSH, VPS or remote environments, or as a Hermes Cloud agent operated by Nous Research. Hermes Desktop can connect to its local runtime, a user-hosted remote backend or a Hermes Cloud instance. Using a hosted model API alone is not the same as hosting the agent runtime. Memory can retain durable context, skills define reusable procedures, cron jobs execute scheduled tasks, subagents delegate work, and terminal/browser/file/MCP tools can act on external systems.

Those same capabilities are trust boundaries. Review provider and channel credentials, memory retention, skill writes, scheduled-task scope, subagent permissions, terminal/browser/filesystem access, MCP servers, remote backends, and human approval requirements before using Hermes with sensitive accounts, repositories, or data.

## Official resources

- [Hermes Agent](https://hermes-agent.nousresearch.com/)
- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs/)
- [Hermes Agent repository](https://github.com/NousResearch/hermes-agent)
- [Nous Research](../../../../../../../producers/sub/n/sub/nous-research/)
