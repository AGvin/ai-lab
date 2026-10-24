# Tyk AI Studio

Tyk AI Studio is Tyk Technologies' AI management platform for administering model-provider access, users, usage, chat, data sources and tools.

## Deployment and gateway boundaries

Community and Enterprise support self-managed deployment, including hub-and-spoke topology. A standalone instance includes an embedded gateway-lite for chat, testing and proxying; it has no filters, middleware or plugins. Hub-and-spoke deployments use the full Edge Gateway data plane for distributed request processing.

The gateway, portal, chat and integrations are platform components. AI Studio remains distinct from Tyk's general API-management products.

## Editions and operations

The Community core uses AGPL-3.0. Enterprise requires a separate license and provides capabilities such as budget enforcement, advanced SSO, fine-grained RBAC, guardrail filters and audit trails. Confirm the edition and gateway surface before relying on a control.

Pin the release, check integration compatibility and plan persistent storage and access policies for the selected deployment.

## Relations

- Produced by: [Tyk Technologies](../../../../../producers/sub/t/sub/tyk-technologies/)

## Official resources

- [Overview and edition comparison](https://tyk.io/docs/ai-management/ai-studio/overview)
- [Deployment options](https://tyk.io/docs/ai-management/ai-studio/installation/overview)
- [Core concepts and gateway surfaces](https://tyk.io/docs/ai-management/ai-studio/core-concepts)
- [Source and licensing](https://github.com/TykTechnologies/ai-studio)
