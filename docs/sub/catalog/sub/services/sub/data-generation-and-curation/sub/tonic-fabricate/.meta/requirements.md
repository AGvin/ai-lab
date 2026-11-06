# Documentation Requirements

## Requirements

- Present Tonic Fabricate as a managed synthetic-data generation product for creating relational databases, files/datasets, mock APIs, and repeatable generation workflows for development, testing, and AI workloads.
- Keep Fabricate distinct from Tonic Structural, Tonic Textual, and other Tonic products unless those products are independently materialized later.
- Treat supported connectors/formats, generation agents, workflow/MCP/API features, pricing, limits, and package tiers as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Fabricate remains data-generation/curation-first rather than generic ETL or data infrastructure.
- Producer provenance resolves to Tonic.ai.

## Scoped original-source qualification — 2026-11-06

- Tonic Fabricate's current official documentation describes a hosted synthetic-data generator for realistic relational databases, free text/files, mock APIs, agent-driven data plans/validation and exportable development/test workloads. The data may be produced from prompts or existing schemas; enterprise live database connections, API calls, workflows and MCP interfaces are plan- and release-dependent.
- Keep Tonic Fabricate distinct from Tonic Structural (de-identification from sensitive structured source data) and Tonic Textual (unstructured redaction/synthesis). Generated synthetic data can still require privacy leakage checks when uploaded production examples, secrets or existing DB connections are used; a vendor's zero-source-data default is not a blanket compliance certificate.
- Tonic's documented May 2026 enterprise live-connections GA and separate beta/preview history should be read by version. Model access, costs, generation quality, exported file consistency, tenancy, SOC 2 scope and retention depend on contract and date.
- Verified first-party source 1: https://www.tonic.ai/products/fabricate
- Verified first-party source 2: https://docs.tonic.ai/fabricate
- Verified first-party source 3: https://www.tonic.ai/product-release-notes/fabricate
- Acceptance credits historical or current service identity and publisher-scoped data creation/handling boundaries only. It does not establish current Gretel hosting, redistributable data/model rights, new identity/metadata, independent privacy/compliance/security checks, full freshness, whole-repo schema/cache/CI/render, reader repair, clean pass, final delivery or merge.
