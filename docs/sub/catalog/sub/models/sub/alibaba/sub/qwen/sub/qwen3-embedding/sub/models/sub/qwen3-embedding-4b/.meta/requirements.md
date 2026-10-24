# Documentation Requirements

## Requirements

- Identify Qwen3-Embedding-4B using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-embedding/models/qwen3-embedding-4b`.
- Preserve canonical membership in `catalog/models/alibaba/qwen/qwen3-embedding` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Qwen3-Embedding-4B is an Apache-2.0 text-embedding checkpoint with 32K context and selectable output dimensions from 32 to 2560.
- Use the documented instruction-aware query format and compatible document preprocessing; preserve the selected dimension and normalization throughout the index.
- Vectors encode similarity for retrieval/classification/clustering; they do not generate answers or provide standalone reranker scores.
- Changing the embedding model or representation settings can require re-embedding the corpus; protect embedded content with the same access controls as its source documents.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
