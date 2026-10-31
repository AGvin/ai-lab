# Deep Agents

Deep Agents is LangChain's open-source agent harness for long-horizon, multi-step work. It builds on LangChain's agent abstractions and uses the LangGraph runtime for execution, streaming and human intervention.

## Capabilities and scope

The harness provides filesystem operations, subagents, context management and memory, with configurable tools, backends, skills and human approval controls. Available shell execution and persistence depend on the selected backend and configuration; pin the package and integration versions before deployment.

The reusable SDK is distinct from Deep Agents Code, the ready-to-use terminal coding application built on it. The SDK alone is not a hosted agent service.

## Execution boundaries

Tools and execution environments determine the agent's authority. Built-in filesystem permission rules do not cover custom tools, MCP filesystem tools or sandbox `execute`; prompts alone cannot isolate side effects.

Running tools in a remote sandbox does not move the host agent, its credentials or unrelated host tools into that sandbox. Configure controls for each execution surface and protect state, credentials and network access separately.

## Relations

- Produced by: [LangChain Inc.](../../../../../producers/sub/l/sub/langchain-inc/)

## Official resources

- [Overview](https://docs.langchain.com/deepagents)
- [Source](https://github.com/langchain-ai/deepagents)
- [Filesystem permissions](https://docs.langchain.com/oss/python/deepagents/permissions)
- [Sandbox deployment boundaries](https://docs.langchain.com/oss/python/deepagents/sandboxes)
