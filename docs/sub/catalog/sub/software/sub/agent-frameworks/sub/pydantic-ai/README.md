# Pydantic AI

Pydantic AI is a provider-agnostic Python agent framework built around typed data, tools, structured outputs, dependency injection, and a managed agent loop.

## Current framework and migration

Pydantic AI V2 (stable since June 23, 2026) builds on a typed Python agent loop with composable **capabilities** for tools, hooks, instructions and model settings. V1 applications should upgrade through the latest V1, address deprecation warnings, and then review V2's behavior changes. The published V1 security-fix commitment runs for *at least* six months after V2; it is not a confirmed end-of-support date.

The separately distributed [Pydantic AI Harness](../pydantic-ai-harness/) provides preassembled coding/research capabilities, workspaces and shell execution; these are not required to use the core framework. Code execution and agent tooling need explicitly selected workspace isolation, least-privilege permissions, credential scoping and appropriate tool approvals.

## Official resources

- [Official documentation](https://pydantic.dev/docs/ai/overview/)
- [Official repository](https://github.com/pydantic/pydantic-ai)
- [Version policy](https://pydantic.dev/docs/ai/project/version-policy/)
- [V1-to-V2 upgrade guide](https://pydantic.dev/docs/ai/project/changelog/)
- [Composable capabilities](https://pydantic.dev/docs/ai/capabilities/overview/)
