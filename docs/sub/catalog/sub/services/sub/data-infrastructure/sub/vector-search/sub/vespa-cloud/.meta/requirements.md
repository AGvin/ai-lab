# Documentation Requirements

## Requirements

- Identify Vespa Cloud as the released, independently operated managed cloud deployment platform for Vespa search/ranking applications.
- Keep Vespa Cloud separate from self-managed/open-source Vespa software under `software/data-infrastructure/vector-search/vespa`, even though both run the Vespa engine.
- Preserve the managed-service operating boundary: tenants, production applications, zones/regions, autoscaling, automated deployment and platform upgrades, endpoint security, and managed operations.
- Treat supported regions/cloud providers, tenancy models, trial/enterprise plans, quotas, SLA, privacy/security controls, cost and availability as freshness-sensitive.
- Do not create individual service identities for Vespa Cloud dev/staging/prod zones, application packages, CLI features, or Vespa Cloud Enclave solely based on a deployment mode.
- Preserve Vespa.ai as current producer with a reciprocal `produces` link.

## Validation

- Managed Vespa Cloud identity remains distinct from self-hosted Vespa software.
- Official Vespa Cloud references match the entity metadata.
- Managed features are not attributed to standalone self-managed Vespa by default.
- Reciprocal Vespa.ai producer relation is present.

## Scoped original-source qualification — 2026-11-07

- Vespa Cloud is Vespa.ai's managed search/ranking deployment and operations service, distinct from open-source self-hosted Vespa. Application zones and enclaves are deployment variants, not separate service identities.
- Publisher source: https://docs.vespa.ai/en/cloud/
- Scope: existing managed service identity and producer boundary only; no authenticated API, security/privacy, full-repository, clean-pass or final gate certification.
