# AgentOps SDK

**AgentOps SDK** is an installable Python observability library for tracing, debugging and replaying AI agent, LLM and tool activity. Its source supports `pip install agentops`, initialization through `agentops.init(...)` and decorators for instrumenting sessions, agents, operations and workflows.

## SDK versus dashboard

The SDK sends instrumentation events to a configured collector or the AgentOps service. The hosted **AgentOps dashboard** and separately deployable `app/` application are different deployment surfaces: installing the SDK does not install or authenticate either backend. Framework integrations and OpenTelemetry behavior depend on specific SDK and dependency versions.

## Telemetry and security

Capturing prompts, tool arguments, exceptions and responses may expose credentials, customer records or other sensitive content. Before production use, configure selective capture/redaction, authorized export destinations and restricted API keys, and verify retention and third-party processing. Do not embed credentials in client code or infer safety from tracing alone.

The source has an [MIT license](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/LICENSE), which does not license underlying model providers, user data or third-party infrastructure. This is a source-backed profile; no agent execution, package installation or runtime telemetry validation was performed.

## Official resources

- [Pinned source/quickstart](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/README.md)
- [Python package metadata](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/pyproject.toml)
- [Source license](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/LICENSE)
- [AgentOps documentation](https://docs.agentops.ai/introduction)
