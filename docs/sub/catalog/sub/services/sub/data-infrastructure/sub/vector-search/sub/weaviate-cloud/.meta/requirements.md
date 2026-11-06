# Documentation Requirements

## Requirements

- Present Weaviate Cloud as the fully managed Weaviate service and keep it distinct from self-managed/open-source Weaviate Database.
- Treat shared database technology as product lineage rather than a reason to collapse the managed service into the software identity.
- Keep embeddings, hybrid search, generative integrations, and Query Agent features secondary while managed vector/search operation remains primary.
- Treat plans, regions, SLAs, pricing, operational features, and availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Weaviate Cloud remains a managed vector/search service identity.
- Producer provenance resolves to Weaviate.

## Scoped original-source qualification — 2026-11-07

- Weaviate Cloud is the provider-operated managed deployment of Weaviate; the open-source/self-managed database and cloud operation have distinct lifecycle and responsibility boundaries.
- Publisher documentation: https://docs.weaviate.io/cloud
- Qualification covers the existing service identity/source boundary only. No authenticated runtime testing, independent security/licensing assessment, full-repository checks, clean pass or final gate is claimed.
