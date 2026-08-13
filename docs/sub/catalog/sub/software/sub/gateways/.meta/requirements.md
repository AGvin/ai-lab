# Documentation Requirements

## Requirements

- Present Gateways as the canonical software catalog index for gateway and routing software positioned between AI clients or applications and one or more model backends.
- Explain that gateways coordinate access and traffic policy but do not execute models themselves and are not remote model providers.
- Preserve the conceptual request path from client/application through an AI gateway to local runtimes, private deployments, or hosted model APIs.
- Summarize representative gateway capabilities: stable multi-backend endpoints, aliases and routing, retries/fallback/load balancing, authentication and key isolation, rate limits/quotas/budget controls, caching, and shared telemetry.
- Preserve the distinction between model gateways and broader API-management gateways.
- List every materialized direct child exactly once and keep concrete product facts with child profiles.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` selectors.

## Validation

- Navigation matches the materialized direct children.
- The page clearly distinguishes gateways from inference runtimes and hosted model APIs.
- The page does not claim ownership of underlying runtime or hosted-service identities.
- The page contains no temporary-placeholder wording.
