# Documentation Requirements

## Requirements

- Present `ai-management-platforms/` as the canonical service owner for producer-operated control-plane products whose primary identity is organization-wide AI inventory, governance, policy, access, cost, risk/compliance, provider/model/agent administration, or related lifecycle management across multiple AI capabilities.
- Keep threat-protection-first products under AI security, tracing/evaluation-only products under evaluation/observability, request-routing/brokering products under gateways, agent identity/auth products under agent identity/access, and ordinary admin surfaces with their canonical parent product.
- Treat customer-side collectors, proxies, connectors, or enforcement components as supporting data-plane pieces when the producer still operates the durable control plane.
- Preserve software/service separation when an independently self-managed AI-management product also exists.

## Validation

- Children are organization-wide managed AI governance/control-plane identities rather than narrow admin modules.
- Security, identity, observability, and gateway capabilities remain secondary unless they are the durable product center.
- Navigation matches validated materialized direct children.
