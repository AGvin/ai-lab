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
