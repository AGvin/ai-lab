# Documentation Requirements

## Requirements

- Present Descope Agentic Identity Hub as the managed control plane for agent identities, protected resources, scoped tokens, credential connections, policy, and agent-access audit trails.
- Keep MCP protection and downstream credential brokering as identity/access capabilities rather than reclassifying the product as an integration platform or gateway.
- Treat supported authorization flows, SDKs, resource/connection behavior, integrations, limits, and availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains identity/access-first rather than integration- or governance-first.
- Producer provenance resolves to Descope.

## Scoped original-source qualification — 2026-11-06

- Descope's Agentic Identity Hub is the identity control plane for agents, MCP resources and credentials. Its documentation explicitly separates Resources (protected audiences, OAuth/JWT scope and access policies) from Connections (stored upstream OAuth tokens and API keys). Runtime token brokering with an intermediate gateway is recommended to avoid handing long-lived third-party secrets to an agent.
- Descope provides OAuth 2.1 authorization for protected APIs/MCP servers, first-party agent governance and outbound credential delegation, but is not itself the destination service or a general agent tool/integration platform. Token audience, issuer, revocation and policy checks must be verified at each resource boundary.
- Claims about user-to-agent-to-tool attribution, enforcement latency, audit retention and production privacy/security are provider-documented service behaviors rather than independent certification. Authentication patterns, service plans and integrations remain mutable.
- Verified first-party source 1: https://docs.descope.com/agentic-identity-hub
- Verified first-party source 2: https://docs.descope.com/agentic-identity-hub/use-cases
- Source acceptance credits the existing identity and provider-scoped capability boundaries only; no new entity or metadata, independently tested OAuth/IAM behavior, full freshness/privacy/legal/security audit, whole-repository schema/cache/CI/render, reader repair, clean pass, final gate or merge.
