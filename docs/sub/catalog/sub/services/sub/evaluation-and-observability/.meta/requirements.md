# Documentation Requirements

## Requirements

- Present Evaluation and Observability Services as the service catalog owner for producer-operated platforms whose primary identity is tracing, inspecting, evaluating, measuring, or improving AI applications and agents and which do not provide a complete independently self-managed product identity.
- Keep installable or fully self-hostable observability/evaluation products under `catalog/software/evaluation-and-observability/`.
- Treat hybrid architectures by the product's durable control-plane ownership rather than by the mere existence of a customer-hosted collector or data plane.
- List every materialized direct child exactly once.

## Validation

- Service and software identities are not duplicated solely because a product supports both SaaS and local collectors.
- Navigation matches the materialized direct children.
