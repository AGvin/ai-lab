# Documentation Requirements

## Requirements

- Identify Qwen3-Reranker-4B using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-reranker/models/qwen3-reranker-4b`.
- Preserve canonical membership in `catalog/models/alibaba/qwen/qwen3-reranker` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Qwen3-Reranker-4B is an Apache-2.0 text reranker with 32K context for instruction/query/document relevance scoring.
- Score supplied candidates using the documented yes/no token scoring contract; do not treat it as a vector embedding or a calibrated probability of factual truth.
- Allocate context to the instruction, query, and candidate together and document truncation; runtime generation APIs alone do not ensure correct reranker scoring.
- Restrict candidate inputs to authorized material and enforce result access independently of relevance.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
