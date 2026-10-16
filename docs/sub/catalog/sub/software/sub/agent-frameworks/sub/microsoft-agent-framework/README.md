# Microsoft Agent Framework

Microsoft Agent Framework 1.0 is Microsoft's production-ready, open-source framework for tool-using agents, Harness Agents, and explicit functional/graph workflows. It combines ideas from AutoGen and Semantic Kernel while retaining a distinct current API and product identity. .NET and Python are the main production-ready SDKs; the separately maintained Go SDK is in public preview with narrower support for some orchestration features.

## Execution and migration boundaries

Agents handle open-ended tool use and conversational work; workflows give applications explicit execution order, state, handoffs, checkpoints and review gates. The framework can run on infrastructure selected by the application team and integrate with hosted model/agent services; it is **not itself** the Microsoft Foundry Agent Service. Use the official migration guides to evaluate changes in AutoGen event-driven orchestration and Semantic Kernel behavior instead of assuming drop-in compatibility. Keep tool permissions, external providers, network access, secrets and state durability under application control.

## Official resources

- [Official documentation](https://learn.microsoft.com/en-us/agent-framework/)
- [Official repository](https://github.com/microsoft/agent-framework)
- [Current architecture and Go preview caveat](https://learn.microsoft.com/en-us/agent-framework/overview)
- [AutoGen migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/)
- [Migration guide index](https://learn.microsoft.com/en-us/agent-framework/migration-guide/)
