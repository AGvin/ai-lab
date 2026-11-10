# Documentation Requirements

## Requirements

- Present Chroma Cloud as the hosted, production-grade, fully managed distributed Chroma service and keep it distinct from the self-managed/open-source Chroma engine.
- Keep dense/sparse/full-text search, collection forking, dashboard, Sync, and managed indexing as service capabilities rather than separate canonical entities.
- Treat regions, pricing, indexing implementation, limits, operational metrics, and availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Chroma Cloud remains managed vector/search infrastructure.
- Producer provenance resolves to Chroma.

## Scoped original-source qualification — 2026-11-07

- Hosted Chroma Cloud is a managed search/database service distinct from the open-source/self-hosted Chroma engine; index operations and collection forking are managed-service features.
- Publisher documentation: https://docs.trychroma.com/cloud/getting-started
- Scoped service identity/source boundary only; no authenticated runtime, license/security assurance, whole-repository validation, clean pass or final delivery credit.
