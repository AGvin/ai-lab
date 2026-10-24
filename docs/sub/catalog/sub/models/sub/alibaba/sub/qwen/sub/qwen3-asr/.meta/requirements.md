# Documentation Requirements

## Requirements

- Identify Qwen3-ASR using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-asr`.
- Preserve canonical membership in `catalog/models/alibaba/qwen` and its reciprocal `has-member` relation.
- Preserve the canonical `produced-by` relation to `catalog/producers/q/qwen-team` and the reciprocal producer relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Released 0.6B/1.7B speech-recognition models with a separately named ForcedAligner companion for timestamp alignment.
- Preserve the exact member's input/output and license contract; do not turn toolkit options, quantizations, or hosted aliases into peer model identities.
- Recognition returns text; forced alignment requires supplied text and returns timing. Neither produces speech or establishes speaker identity.
- Treat recordings as sensitive, authorize capture/transcription, and review transcripts before consequential use.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
