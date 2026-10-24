# Documentation Requirements

## Requirements

- Identify Cohere Model Vault as Cohere's managed dedicated single-tenant inference deployment service for Cohere models.
- Preserve the infrastructure boundary: customers provision an isolated managed deployment and call it through Cohere-compatible APIs without operating the serving stack themselves.
- Preserve Standard Vault and Encrypted Vault as deployment/security modes of the same product unless future lifecycle establishes independently durable services; confidential-computing/attestation claims must remain mode- and hardware-specific.
- Keep Cohere Platform shared SaaS API access, customer-operated private deployments, cloud-provider offerings, North workspace, Compass retrieval, and underlying Cohere model identities separate.
- Treat supported model/version inventory, GPU options, regions, encryption/attestation hardware, performance tiers, provisioning workflow, capacity/waitlists, pricing, quotas, and lifecycle as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Model Vault remains managed infrastructure rather than a trained model or self-managed runtime.
- Dedicated/single-tenant hosting is not generalized into customer-operated self-hosting.
- Producer provenance resolves bidirectionally to Cohere.
