# AutoGen

AutoGen is Microsoft's open-source framework for building agentic and multi-agent applications. Its current architecture spans a lower-level Core runtime for message passing and local or distributed execution, a higher-level AgentChat API for common multi-agent patterns, and Extensions for model, tool, and execution integrations.

## Current status

AutoGen is currently in maintenance mode and is community managed. Microsoft recommends [Microsoft Agent Framework](../microsoft-agent-framework/) for new projects as the production-ready successor, while existing AutoGen users can continue using the framework and migrate when appropriate.

AutoGen Studio remains useful for prototyping multi-agent workflows, but upstream documentation does not position it as a production-ready application.

## Operational boundary

AutoGen can coordinate agents, tools, code execution, event-driven workflows, and human participation. Deployments that execute generated code or expose tools should treat sandboxing, filesystem and network access, credentials, model-provider data flow, and human approval gates as explicit security boundaries.

## Runtime versions and code execution

The maintained AutoGen packages use Python 3.10+, with `autogen-core` for the lower-level runtime, `autogen-agentchat` for common agent patterns, and optional `autogen-ext` model, tool and executor integrations. Older AutoGen 0.2 tutorials use distinct packages and imports and should not be mixed with maintained AgentChat instructions without migration.

`LocalCommandLineCodeExecutor` runs generated commands on the **host**. `DockerCommandLineCodeExecutor` runs commands in a container and requires `autogen-ext[docker]`, but callers must still limit mounted directories, Docker/socket permissions, secrets, networking and resource usage. AutoGen is in **maintenance mode**; for new feature work, Microsoft's separate Agent Framework is recommended, with migration assessment rather than assumed drop-in compatibility.

## Official resources

- [AutoGen documentation](https://microsoft.github.io/autogen/)
- [AutoGen repository](https://github.com/microsoft/autogen)
- [Current Python installation](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/installation.html)
- [Code executor security](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/command-line-code-executors.html)
- [Migration to Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/)
- [Microsoft](../../../../../producers/sub/m/sub/microsoft/)
