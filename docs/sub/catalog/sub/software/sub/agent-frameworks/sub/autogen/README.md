# AutoGen

AutoGen is Microsoft's open-source framework for building agentic and multi-agent applications. Its current architecture spans a lower-level Core runtime for message passing and local or distributed execution, a higher-level AgentChat API for common multi-agent patterns, and Extensions for model, tool, and execution integrations.

## Current status

AutoGen is currently in maintenance mode and is community managed. Microsoft recommends [Microsoft Agent Framework](../microsoft-agent-framework/) for new projects as the production-ready successor, while existing AutoGen users can continue using the framework and migrate when appropriate.

AutoGen Studio remains useful for prototyping multi-agent workflows, but upstream documentation does not position it as a production-ready application.

## Operational boundary

AutoGen can coordinate agents, tools, code execution, event-driven workflows, and human participation. Deployments that execute generated code or expose tools should treat sandboxing, filesystem and network access, credentials, model-provider data flow, and human approval gates as explicit security boundaries.

## Official resources

- [AutoGen documentation](https://microsoft.github.io/autogen/)
- [AutoGen repository](https://github.com/microsoft/autogen)
- [Microsoft](../../../../../producers/sub/m/sub/microsoft/)
