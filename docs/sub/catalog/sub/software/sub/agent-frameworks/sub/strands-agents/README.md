# Strands Agents

Strands Agents is an open-source, model-agnostic framework for building AI agents with tools, MCP, structured output, sessions, memory, observability, evaluation and multi-agent patterns. It supports Python and TypeScript, with the agent loop executing in the application operator's process while model inference may use local or remote providers.

## Current SDK and harness packages

The actively maintained source is the [Strands Harness SDK monorepo](https://github.com/strands-agents/harness-sdk), containing lower-level Python `strands-agents` and TypeScript `@strands-agents/sdk`, assembled `strands-harness` and `@strands-agents/harness` packages, a terminal CLI and MCP helpers. The old standalone `sdk-typescript` repository was archived in June 2026 after its code moved to this monorepo. As of October 2026, Python and TypeScript releases are separately versioned; check the current changelog before relying on specific APIs.

Strands is not a hosted execution service. Tools can access the operator's files, network, secrets and external MCP servers unless the runtime constrains them; approved sandboxes and human intervention should be chosen separately from model-provider settings. Hosted Bedrock or other model APIs do not relocate the Strands SDK agent loop into an AWS-managed agent service.

## Official resources

- [Official website and documentation](https://strandsagents.com/)
- [Current Strands SDK/harness source](https://github.com/strands-agents/harness-sdk)
- [Official release changelog](https://strandsagents.com/changelog/)
