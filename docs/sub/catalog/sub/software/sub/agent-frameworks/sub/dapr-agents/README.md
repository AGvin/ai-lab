# Dapr Agents

**Dapr Agents** is the Dapr community's open-source Python agent framework built on the [Dapr application runtime](https://github.com/dapr/dapr). It provides durable, stateful and multi-agent workflows with actors, messaging, external tool invocation and integrations. The general-purpose Dapr sidecar/runtime is a separate project identity, not a synonym for Dapr Agents.

## Release and maturity

The [official v1.1.0 release](https://github.com/dapr/dapr-agents/releases/tag/v1.1.0) is dated **October 27, 2026**, and is not labeled prerelease. [Tagged package metadata](https://github.com/dapr/dapr-agents/blob/v1.1.0/pyproject.toml) requires Python **>=3.11,<3.15** and declares Apache-2.0. However, its package classifier still says **Pre-Alpha** and the repository's language-support roadmap retains 2025 predictions. Treat maturity and compatibility as version- and deployment-specific; do not infer verified production SLAs from a v1.x release.

## Deployment and security boundaries

Dapr Agents builds on Dapr Workflows, Actors, pub/sub, state stores and service invocation. A suitable Dapr sidecar, backing databases/brokers and LLM endpoints are independently configured dependencies. Durable retry/replay needs idempotent external side effects. Restrict state and messaging tenants, tool/MCP auto-discovery, network egress, credentials and service identities, and enforce retention, tracing redaction, backup and resource budgets. Publisher claims about scalability, availability and security have **not** been independently tested by AI Lab.

[Apache-2.0 software licensing](https://github.com/dapr/dapr-agents/blob/v1.1.0/LICENSE) does not clear external model, dataset, cloud processing or hosted-service rights.

## Relations

- Produced by: [Dapr Project](../../../../../producers/sub/d/sub/dapr-project/)

## Official resources

- [Dapr Agents source](https://github.com/dapr/dapr-agents)
- [v1.1.0 release](https://github.com/dapr/dapr-agents/releases/tag/v1.1.0)
- [Agent framework documentation](https://docs.dapr.io/developing-ai/dapr-agents/)
- [Tagged package metadata](https://github.com/dapr/dapr-agents/blob/v1.1.0/pyproject.toml)
- [Original Dapr runtime](https://github.com/dapr/dapr)
