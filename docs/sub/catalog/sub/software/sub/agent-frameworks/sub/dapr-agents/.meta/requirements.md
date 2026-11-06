# Documentation Requirements

## Requirements

- Catalog Dapr Agents as a separately installable Dapr Authors Python framework for durable LLM agent workflows and multi-agent coordination, not the underlying general-purpose Dapr runtime, generic Dapr Workflow APIs, or a managed hosted agent service.
- Preserve the original non-prerelease **v1.1.0** date **2026-10-27**, Apache-2.0 software license, and tagged package Python **>=3.11,<3.15**. Explicitly disclose the conflicting **Pre-Alpha** classifier and outdated 2025 language-support roadmap; published v1.x is not independent proof of full production readiness.
- Differentiate first-party functionality from its required Dapr sidecar and backends: durable workflows, actors, pub/sub, state stores, messaging, observability, service invocation, model-provider and MCP tool integrations require separate runtime configurations.
- Require version compatibility tests, workflow idempotency and replay checks, network and credential isolation, state-store and messaging tenant controls, MCP tool allowlists, backup/recovery and secrets/trace redaction. Security and performance figures are publisher-reported, not independently reproduced.
- Attribute original producer to the open-source Dapr Project/Authors with one canonical reciprocal `produced-by` / `produces` pair; do not infer Microsoft corporate ownership or CNCF security certification.
- The framework's Apache-2.0 license does not license third-party models, data, provider contracts, or hosted infrastructure. No actual Kubernetes deployment, benchmark, security audit, whole-catalog build or final rendered-reader validation was performed.

## Validation

- One Dapr Agents software triad, one direct agent-frameworks child index entry and one separately represented Dapr Project producer with reciprocal canonical relation.
- Original source, version, license and runtime-risk caveats are explicit. Only scoped authored verification is in scope before final eight-root clean cycles and publication gates.
