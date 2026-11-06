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

## Scoped original-source qualification — 2026-11-06

- Cohere Model Vault is a Cohere-operated managed isolated single-tenant inference deployment for supported Cohere model families; customers select dedicated capacity/model tiers and call serving endpoints without managing the underlying GPU stack. Keep this separate from shared Cohere Platform SaaS API, customer-operated private deployments, North workspace and model provenance.
- Standard Vault and Encrypted Vault are security/deployment options of the same managed product. Confidential-computing and remote-attestation claims apply specifically to supported Encrypted configurations and hardware, not every Standard vault or arbitrary third-party model. Operational limits, supported models, GPU options, scaling, region, isolation and pricing are provider-scoped, mutable.
- Dedicated single-tenancy must not be marketed as complete independently certified confidentiality or as evidence that customer data is never stored; review exact access, keys, retention and deployment policy before use.
- Verified first-party source 1: https://docs.cohere.com/docs/model-vault
- Verified first-party source 2: https://docs.cohere.com/docs/model-vault/encrypted
- Verified first-party source 3: https://docs.cohere.com/docs/model-vault/standard/supported-models
- Source acceptance covers service identity and publisher-scoped limits, not full lifecycle freshness, authenticated provider execution, independent security/legal assurance, root-wide schema/cache/CI/render, reader repairs, clean passes or final delivery.
