# AgentScope

AgentScope is an open-source Python 3.11+ framework for building tool-using and multi-agent systems, including teams, pipelines and optional external model integrations. Its authorship is attributed to the SysML team of Alibaba Tongyi Lab.

## Release and compatibility

The verified published baseline is **v2.0.10 (2026-10-12)** under **Apache-2.0**. Its package metadata retains a **Beta** classifier despite the project's production-ready description. Pin the selected release and independently check provider SDK, MCP/A2A and deployment compatibility before adoption.

## Runtime and operations

**AgentScope 2.0** integrates capabilities from the formerly separate AgentScope Runtime project (tool sandboxing, Agent-as-a-Service APIs and observability). The [standalone runtime repository](https://github.com/agentscope-ai/agentscope-runtime) now recommends migrating to AgentScope 2.0 for ongoing development. Voice and some workflow capabilities remain experimental; verify the selected release.

Choose trusted sandbox execution backends, explicit tool authorizations, network limits, scoped credentials, protected service endpoints and appropriate trace retention. Neither an example adapter nor a sandbox name establishes safe isolation by itself.

## Relations

- Produced by: [Alibaba Group](../../../../../producers/sub/a/sub/alibaba-group/)

## Official resources

- [AgentScope source](https://github.com/agentscope-ai/agentscope)
- [Published v2.0.10 metadata](https://pypi.org/project/agentscope/2.0.10/)
- [Documentation](https://docs.agentscope.io/)
- [Runtime migration reference](https://github.com/agentscope-ai/agentscope-runtime)
