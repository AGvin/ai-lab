# Claude Agent SDK

Claude Agent SDK is Anthropic's installable agent SDK/runtime. It provides an agent loop, tool execution, sessions, hooks and MCP integrations in a developer-operated process.

## Execution and product boundaries

The developer operates the SDK process and its tools; Claude model inference occurs through a configured supported model-provider path, not locally merely because the SDK is installed. The SDK is separate from the [Claude Code](../../../agents/sub/hybrid/sub/claude-code/) coding-agent application, Claude Managed Agents hosted infrastructure, and general-purpose Messages API clients.

## Operational considerations

The agent can execute shell commands, modify files, use network tools and access credentials according to configuration. Restrict tool authority, isolate execution, protect provider secrets, require approval for consequential actions and specify logging/retention boundaries.

Languages, SDK versions, bundled runtime components, sessions, tool APIs and provider compatibility are mutable; check the selected SDK release before integration.

## Relations

- Produced by: [Anthropic](../../../../../producers/sub/a/sub/anthropic/)

## Official resources

- [Agent SDK overview](https://platform.claude.com/docs/en/agent-sdk/overview)
- [SDK and CLI differences](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
