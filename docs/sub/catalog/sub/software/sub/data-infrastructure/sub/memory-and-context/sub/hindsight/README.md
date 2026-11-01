# Hindsight

Hindsight is an open-source, self-hostable long-term memory system for AI agents published by Vectorize. It organizes durable agent context into memory banks and exposes **retain** (ingest), **recall** (retrieve), and **reflect** (reason over stored information) operations. Its memory-first software identity is distinct from a hosted model API, a full agent framework, and from the separately operated **Hindsight Cloud** service.

## Scope and release

- The [official v1.1.0 release](https://github.com/vectorize-io/hindsight/releases/tag/v1.1.0) was published **2026-10-21**. Hindsight supports local Docker deployment, PostgreSQL-backed configurations, SDK/API access and an MCP integration; backend capabilities, storage modes, LLM integrations and performance change by version and deployment.
- The system extracts entities, relationships and temporal facts, consolidates observations, and retrieves context through multiple search strategies. This is a reusable memory system rather than a vector database product or a replacement for policy-bound agent reasoning.
- Hindsight Cloud, enterprise deployments and any object-storage or managed capabilities are separate commercial and operational choices. The open-source source-code **MIT** license is not proof of free hosted service usage, model data rights, support terms or regulatory compliance.

## Privacy, security, and reliability

Long-term memory can retain personal/confidential information and make it available to future agents. Before exposing an API or MCP server, enforce authentication and bank-level tenant authorization, encrypt data and backups, limit retention and deletion rights, and restrict network reachability. Verify tenant isolation and auditability in the actual deployed edition; a memory bank ID alone is not an access-control guarantee.

Hosted LLM/embedding providers may receive retained content, retrieval context or prompts even when the Hindsight storage server is self-hosted. Select model endpoints and region deliberately, check processor agreements and local-provider configuration, and test deletion/restore flows. Beware stale or contradictory facts and prompt injection in untrusted remembered text; retrieval/reflect output is not a trusted instruction source.

Benchmark scores published by Vectorize or linked collaborators are release-, dataset-, evaluation- and environment-specific; they have **not** been independently reproduced by AI Lab.

## Relations

- Produced by: [Vectorize AI, Inc.](../../../../../../../producers/sub/v/sub/vectorize-ai-inc/)

## Official resources

- [Hindsight source repository](https://github.com/vectorize-io/hindsight)
- [Hindsight v1.1.0 release](https://github.com/vectorize-io/hindsight/releases/tag/v1.1.0)
- [Hindsight documentation](https://hindsight.vectorize.io/)
- [Installation and deployment](https://hindsight.vectorize.io/developer/installation)
- [Model provider configuration](https://hindsight.vectorize.io/developer/models)
- [MIT software license](https://github.com/vectorize-io/hindsight/blob/main/LICENSE)
- [Vectorize product and deployment overview](https://vectorize.io/)
