# Documentation Requirements

## Requirements

- Identify BentoML as an open-source self-managed inference/deployment platform for packaging, serving, and scaling AI model/application workloads.
- Preserve its primary placement under integrated inference platforms: BentoML combines model/service packaging, serving, deployment configuration, and operational tooling rather than being only a low-level inference engine.
- Keep BentoML software identity distinct from producer-operated BentoCloud or other hosted delivery surfaces unless a separately materialized service identity is independently justified.
- Render the standard `entity-relations` block from validated current-entity relations and preserve BentoML as the producer.
- Treat release versions, supported model/runtime integrations, cloud deployment targets, GPU/runtime compatibility, APIs, performance claims, and hosted-service behavior as mutable facts requiring current first-party verification.
- Include current official BentoML documentation and repository references.

## Validation

- BentoML remains a self-manageable software platform, not a hosted-only service or a duplicate low-level engine identity.
- The `produces` / `produced-by` relation pair is materially consistent.
- BentoCloud-specific facts are not generalized onto the self-managed software identity without evidence.
