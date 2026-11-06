# Arcade

Arcade is an enterprise agent tool/action execution and integration platform with user-scoped authorization, OAuth credential handling, governed tool calls and MCP gateway capabilities.

## Product scope

Arcade Cloud, supported marketplace installations and full self-hosted Kubernetes/Helm deployments are delivery modes of the same platform. Managed tool servers, policy/audit services and OAuth brokerage are platform components. The separately cataloged Arcade MCP framework is a distinct installable developer library, not the full commercial execution platform.

## Operations and boundaries

Self-hosted deployment needs OIDC, databases, workers, gateways and RBAC configured per the supported deployment chart. Enforce individual-user OAuth scopes and human approval for high-impact actions; never hand raw reusable tokens to a model. The commercial platform must not be described as universally MIT-licensed merely because its SDK or related Arcade MCP framework uses MIT. Features, plans, API versions, quotas and hosted availability can change.

## Relations

- Produced by: [Arcade AI, Inc.](../../../../../../../producers/sub/a/sub/arcade-ai-inc/)

## Official resources

- [Official site](https://www.arcade.dev/)
- [Platform documentation](https://docs.arcade.dev/en/home)
- [Self-hosted Helm deployment](https://docs.arcade.dev/en/operate/deploy/helm)
