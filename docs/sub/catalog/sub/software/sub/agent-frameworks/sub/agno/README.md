# Agno

Agno is an open-source Python framework for building and running AI agents and agentic systems with models, tools, memory, knowledge, teams, and workflows.

## SDK, runtime and security boundaries

Agno includes an agent-building **Python SDK**, the **AgentOS** service runtime, and an **AgentOS UI** for platform management. You can build agents with the SDK without requiring the UI or any particular hosted provider; deploying the service and connecting a control plane are distinct operational choices.

For exposed AgentOS APIs, explicitly configure and verify JWT authentication and endpoint scopes. JWT user-data isolation is opt-in, shared tool/resource objects need safe concurrent access, and reverse-proxy, database and network controls remain the operator's responsibility. Use human approvals for sensitive tool execution. The upstream project also documents per-run telemetry (without prompt/message/output bodies) and the `AGNO_TELEMETRY=false` opt-out; assess actual privacy requirements independently.

## Official resources

- [Official website](https://www.agno.com/)
- [Official documentation](https://docs.agno.com/)
- [Official repository](https://github.com/agno-agi/agno)
- [AgentOS deployment overview](https://docs.agno.com/agent-platform/overview)
- [Security and authorization](https://docs.agno.com/features/security-and-auth)
