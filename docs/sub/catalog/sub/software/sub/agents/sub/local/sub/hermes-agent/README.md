# Hermes Agent

Hermes Agent is Nous Research's open-source, self-hostable personal AI agent. Its current product surface combines CLI/desktop and messaging access with persistent memory, reusable skills, scheduled tasks, subagent delegation, MCP-connected tools, and configurable model providers.

## Persistence and execution boundary

Hermes can run in user-controlled local, containerized, remote, VPS, SSH, and other self-managed environments. Its usefulness comes from persistent and unattended capabilities: memory can carry durable context, skills can encode reusable procedures, cron jobs can run automatically, subagents can work in isolated task contexts, and terminal/browser/file/MCP tools can act on external systems.

Those same capabilities are trust boundaries. Review provider and channel credentials, memory retention, skill writes, scheduled-task scope, subagent permissions, terminal/browser/filesystem access, MCP servers, remote backends, and human approval requirements before using Hermes with sensitive accounts, repositories, or data.

## Official resources

- [Hermes Agent](https://hermes-agent.nousresearch.com/)
- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs/)
- [Hermes Agent repository](https://github.com/NousResearch/hermes-agent)
- [Nous Research](../../../../../../../producers/sub/n/sub/nous-research/)
