# Documentation Requirements

## Requirements

- Present Auth0 for AI Agents as an agent-specific managed identity/access surface for authentication, delegated access, scoped credentials, and authorization in AI-agent applications.
- Keep generic Auth0 CIAM capabilities outside this profile unless they directly define the agent-specific product surface.
- Keep tool execution/integration platforms separate even when Auth0 supplies the credentials used by those integrations.
- Treat product availability, supported flows, token-vault behavior, limits, integrations, and packaging as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains agent identity/access-first rather than generic IAM or integration ownership.
- Producer provenance resolves to Auth0.
