# Documentation Requirements

## Requirements

- Identify Qwen3-Embedding using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-embedding`.
- Preserve canonical membership in `catalog/models/alibaba/qwen` and its reciprocal `has-member` relation.
- Preserve the canonical `produced-by` relation to `catalog/producers/q/qwen-team` and the reciprocal producer relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Released text-embedding checkpoints at 0.6B, 4B, and 8B for vector retrieval and related representation tasks.
- Preserve the exact member's input/output and license contract; do not turn toolkit options, quantizations, or hosted aliases into peer model identities.
- Embedding dimensions and preprocessing must remain consistent across queries and indexed documents; similarity does not establish source correctness or access permission.
- Keep reranking as a separate model/stage rather than inferring an answer-generation contract.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
