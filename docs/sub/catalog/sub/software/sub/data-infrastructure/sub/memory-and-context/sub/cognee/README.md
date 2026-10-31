# Cognee

Cognee is an open-source/self-hosted AI memory platform centered on persistent long-term memory and knowledge-graph infrastructure for agents.

## Scope and boundaries

Graph and vector storage, ingestion, retrieval, and framework integrations support the same memory-first software identity. Supported stores, providers, deployment modes, APIs, and performance depend on the selected release and configuration.

Local-file ingestion can read files accessible to the Cognee process. Shared API deployments need explicit file-access controls, and API-mode MCP needs those controls on the MCP host too because that host opens local paths before uploading them.

## Relations

- Produced by: [`catalog/producers/t/topoteretes`](../../../../../../../producers/sub/t/sub/topoteretes/)

## Official resources

- <https://github.com/topoteretes/cognee>
- <https://www.cognee.ai/>
- [Deployment security and local-file controls](https://docs.cognee.ai/setup-configuration/security)
