# LangGraph

LangGraph is LangChain Inc.'s open-source low-level orchestration framework and runtime for building long-running, stateful agents and workflows. It focuses on execution infrastructure such as durable execution, streaming, persistence, and human-in-the-loop control rather than providing the higher-level agent abstractions owned by LangChain.

## Runtime and platform boundary

LangGraph can be used as an open-source runtime with application-selected model providers, tools, and persistence backends. LangSmith provides related hosted capabilities such as tracing, evaluation, deployment, and development tooling; those platform services are a separate adoption surface rather than a requirement for the LangGraph package itself.

Stateful deployments should treat checkpoint storage, sensitive state and memory, tool permissions, provider credentials, interruption/approval semantics, and production observability as explicit operational boundaries.

## Related framework

- [LangChain](../langchain/) — higher-level agent framework built on LangGraph's runtime capabilities.

## Official resources

- [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph repository](https://github.com/langchain-ai/langgraph)
- [LangChain Inc.](../../../../../producers/sub/l/sub/langchain-inc/)
