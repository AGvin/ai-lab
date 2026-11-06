# Documentation Requirements

## Requirements

- Identify Qwen3-ForcedAligner-0.6B using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-asr/models/qwen3-forcedaligner-0-6b`.
- Preserve canonical membership in `catalog/models/alibaba/qwen/qwen3-asr` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Qwen3-ForcedAligner-0.6B is the released Apache-2.0 timestamp-alignment companion to Qwen3-ASR.
- It requires audio plus supplied text and returns alignment/timing; it is not an automatic transcription or speaker-recognition model.
- The documented boundary is up to five minutes of speech in eleven languages; do not transfer the ASR models' language inventory or long-audio behavior.
- Validate supplied transcript accuracy and consent to process the recording; alignment is not independent evidence that a transcript is correct.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
