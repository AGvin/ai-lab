# Documentation Requirements

## Requirements

- Identify IBM watsonx Orchestrate as IBM's producer-operated agentic platform whose current primary enterprise identity combines agent operations, orchestration, governance, optimization, catalog/discovery, and builder surfaces around a centralized control plane.
- Preserve its placement under `ai-management-platforms` because the current product explicitly centers organization-wide control of agents across internal and external sources, even though agent building and multi-agent orchestration are first-class capabilities.
- Keep IBM watsonx.governance as a separate canonical service identity: governance/compliance lifecycle management and Orchestrate's operational agent control plane overlap but are not aliases.
- Keep model identities, third-party agents, Agent Connect ecosystem participants, and independently durable tools/frameworks outside this service identity.
- Treat cloud/region availability, feature-level GA/private-preview state, integrations, supported external frameworks/protocols, catalog contents, pricing, and plan eligibility as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains an organization-wide managed agent control-plane identity rather than a generic workflow engine or assistant workspace.
- Feature-level preview state is not generalized to the whole product and product availability is not generalized across all regions/environments.
- Producer provenance resolves to IBM.

## Scoped original-source qualification — 2026-11-06

- IBM watsonx Orchestrate exposes a managed Agentic Control Plane for enterprise-wide discovery, scheduling, evaluation, observability, governance, identity, auditing and optimization of IBM-built or external agents. IBM's July 2, 2026 announcement notes the June 2026 launch on AWS and IBM Cloud; features and deployment support have distinct regional/account eligibility.
- The agent catalog/builder, Agent Connect, interoperability through A2A and OpenTelemetry and governed execution are capabilities or integrations of the Orchestrate service, not proof of IBM authorship of every connected LangGraph, CrewAI, model, third-party tool or externally hosted agent.
- IBM watsonx.governance remains a separately cataloged governance/compliance service rather than an alias of Orchestrate. Policies, managed-agent trust, data retention, regional availability, automation and published performance/cost savings require verified tenant/workload settings.
- Verified first-party source 1: https://www.ibm.com/products/watsonx-orchestrate/agent-control-plane
- Verified first-party source 2: https://www.ibm.com/new/announcements/introducing-the-agentic-control-plane
- Source acceptance credits current governance/control service identity and bounded publisher claims, not name aliases as new entities, metadata or reader repairs, independent compliance/security/runtime verification, full freshness, root-wide schema/cache/CI/render, clean pass, final delivery or merge.
