# CAMEL

CAMEL (`camel-ai`) is a community-maintained Python multi-agent framework for role-playing agent societies, collaborative workflows, simulated environments, and synthetic-data generation. It is a released software framework, not a hosted agent service or a benchmark dataset.

## Release and compatibility

At the October 16, 2026 source check, the latest **non-prerelease** GitHub release was **v0.2.90** (March 22, 2026). The upstream `master` branch package manifest declares **0.2.91a7**, an unreleased development version; it is not the currently published stable release. The source manifest targets **Python >=3.10,<3.15**, with the `mcp` dependency restricted to `>=1.3,<2`. Pin the **chosen released distribution** and optional extras independently rather than assuming that current `master` dependency bounds describe every older published release. The project is Apache-2.0-licensed.

## Agent and operational boundaries

CAMEL provides communication and role-playing agents, workforce orchestration, memory, simulated environments, tool and model integrations, and synthetic-data workflows. Community claims about very large agent societies should not be read as production throughput guarantees; use measured results from the target configuration.

When agents can invoke interpreters, browsers or external APIs, isolate execution environments and limit credentials, filesystem/network access, resource consumption and model cost. Human-in-the-loop tool approval must be explicitly configured; it does not automatically authorize every tool invocation. Treat synthetic data, prompts, traces and provider traffic according to their actual privacy and retention requirements.

## Official resources

- [CAMEL website](https://www.camel-ai.org/)
- [Documentation](https://docs.camel-ai.org/)
- [Official repository](https://github.com/camel-ai/camel)
- [Release history](https://github.com/camel-ai/camel/releases)
- [Agents reference](https://docs.camel-ai.org/key_modules/agents)
- [Human-in-the-loop tool approval](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_human_in_loop_and_tool_approval)
- [CAMEL-AI Community](../../../../../producers/sub/c/sub/camel-ai/)
