# Documentation Requirements

## Requirements

- Present Qdrant Managed Cloud as Qdrant's producer-operated managed vector/search service, distinct from self-managed Qdrant software.
- Keep cluster operation, scaling, monitoring, upgrades, backups, disaster recovery, and hybrid-cloud support as service capabilities rather than separate entities.
- Treat cloud regions, plans, pricing, limits, SLAs, infrastructure providers, and operational features as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The service remains vector/search-first rather than generic cloud infrastructure.
- Producer provenance resolves to Qdrant.

## Scoped original-source qualification — 2026-11-07

- Qdrant Managed Cloud is a managed deployment and operations service for the Qdrant vector database, separate from self-hosted Qdrant software; backups, scaling and provider availability are plan-specific.
- Publisher documentation: https://qdrant.tech/documentation/cloud/
- Scoped service identity/source boundary only; no authenticated runtime, license/security assurance, whole-repository validation, clean pass or final delivery credit.
