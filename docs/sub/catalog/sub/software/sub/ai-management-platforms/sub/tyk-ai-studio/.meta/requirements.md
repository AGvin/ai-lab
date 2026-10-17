# Documentation Requirements

## Requirements

- Identify Tyk AI Studio as a comprehensive AI management/control-plane platform rather than only an LLM gateway.
- Describe its current self-managed and hybrid deployment models, Community and Enterprise editions, and hub-and-spoke architecture only from current Tyk documentation.
- Cover provider/model administration, gateway policy, users/RBAC, usage and cost controls, portals/chat, data sources, tools, plugins, and edge gateways as platform components without creating duplicate canonical products for embedded components unless independent lifecycle evidence appears.
- Distinguish Tyk AI Studio from Tyk's general API-management products.
- Keep edition-specific capabilities, licensing, deployment requirements, and supported integrations freshness-sensitive.
- Preserve the AGPL-3.0 Community core and separately licensed Enterprise boundary. Do not present Enterprise budget enforcement, advanced SSO, fine-grained RBAC, guardrail filters or audit trail as universal Community features.
- Distinguish the embedded gateway-lite used by chat, testing and proxying from the full Edge Gateway data plane. The embedded gateway has no filters, middleware or plugins; hub-and-spoke edge deployment does not by itself enable Enterprise-only features.
- Render the standard `entity-relations` block from validated current-entity relations; producer provenance resolves reciprocally to Tyk Technologies.

## Validation

- The page does not reduce AI Studio to a model gateway.
- Community/Enterprise differences are not generalized across both editions.
- Gateway capabilities are attributed to the correct embedded or Edge Gateway surface and edition.
- The Tyk Technologies producer inverse resolves to this canonical software identity.
