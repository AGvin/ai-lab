# OpenAI Agents API

## Relations

- Produced by: [OpenAI](../../../../../producers/sub/o/sub/openai/)

## Service purpose

OpenAI Agents API provides a managed Codex harness for durable cloud-agent sessions. OpenAI introduced it in **public beta on September 10, 2026**. The service manages sessions, orchestration, context compaction, and recovery while the application supplies tools and chooses an execution environment. [Introduction](https://openai.com/index/introducing-the-agents-api/); [service overview](https://developers.openai.com/api/docs/guides/agents-api/overview).

## Access and execution

Applications create agents and sessions through the API, send input, and receive events and outputs. Agents can work with files, commands, tools, MCP connections, and artifacts when those capabilities are configured. The environment may be an OpenAI-hosted sandbox, a self-hosted environment, or a supported partner sandbox. OpenAI's managed harness and the chosen sandbox operator are separate operational responsibilities.

The OpenAI Agents SDK is installable software with its own runtime choices. Codex, ChatGPT Work, underlying models, MCP servers, plugins, skills, vaults, and sandbox-provider services also retain their own identities. Shared agent concepts or billing do not collapse those boundaries.

## Service conditions

The launch's public-beta designation does not establish general availability. Check current API documentation for lifecycle, session behavior, supported environments, tool permissions, retention, regions, quotas, and operational limits. Model usage, tools, and hosted execution can be billed separately under current service terms. Customer-reported launch outcomes describe those customers' configurations and do not establish independent performance guarantees.

## Official resources

- [Agents API introduction](https://openai.com/index/introducing-the-agents-api/)
- [Agents API overview](https://developers.openai.com/api/docs/guides/agents-api/overview)
