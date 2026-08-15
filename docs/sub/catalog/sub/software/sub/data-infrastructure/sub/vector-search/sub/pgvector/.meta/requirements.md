# Documentation Requirements

## Requirements

- Identify pgvector as the open-source PostgreSQL extension for vector similarity search.
- Preserve its primary placement under `data-infrastructure/vector-search`; PostgreSQL-extension packaging is an implementation form rather than a separate taxonomy axis.
- Describe exact and approximate nearest-neighbor search only at the level supported by current upstream documentation; keep version-specific PostgreSQL, index, dimensionality, and performance details source-backed when expanded.
- Distinguish pgvector from hosted PostgreSQL providers that include the extension.
- Include the current official pgvector repository reference.

## Validation

- The page explains why pgvector shares a role-based group with standalone vector-search systems such as Qdrant.
- Hosted provider availability is not treated as pgvector's canonical product identity.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
