# OpenCode

OpenCode is an open-source AI coding agent from Anomaly Innovations, Inc. It supports terminal, desktop, IDE-extension, SDK, non-interactive/automation, and remote-client workflows around the same local/client-controlled agent product.

## Agent and extension boundary

OpenCode can use repository-local instructions such as `AGENTS.md`, configurable primary agents and subagents, multiple model providers, reusable skills, executable plugins/custom tools, MCP servers, and configured references. These mechanisms extend the agent in different ways and should be reviewed separately rather than treated as interchangeable packages.

OpenCode's permission system can allow, ask, or deny actions at tool, path, command, or agent scope. Those rules are authorization and approval controls, not a sandbox: a permitted action executes with the access available to the OpenCode process. Treat repository instructions, generated diffs, shell execution, external directories, plugins, skills, MCP servers, provider credentials, network/data exposure, and unattended or background execution as explicit trust boundaries, and add OS/container/worktree isolation when stronger containment is required.

OpenCode Zen and other hosted model-access services are separate service surfaces; using hosted inference does not change the OpenCode agent itself into a hosted agent runtime.

## Related

- [Anomaly Innovations, Inc.](../../../../../../../producers/sub/a/sub/anomaly-innovations-inc/) — canonical producer organization.

## Official resources

- [OpenCode](https://opencode.ai/)
- [OpenCode documentation](https://opencode.ai/docs)
- [OpenCode repository](https://github.com/anomalyco/opencode)
- [OpenCode Terms of Service](https://opencode.ai/legal/terms-of-service)
