# Documentation Requirements

## Requirements

- Identify Qwen3-ASR-0.6B using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-asr/models/qwen3-asr-0-6b`.
- Preserve canonical membership in `catalog/models/alibaba/qwen/qwen3-asr` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Qwen3-ASR-0.6B is a released Apache-2.0 model for language identification and speech-to-text across 30 languages and 22 Chinese dialects.
- Keep transcription separate from translation, speech synthesis, speaker authentication, and timestamp alignment; timestamps can require the separate ForcedAligner.
- In the documented `qwen-asr` toolkit, streaming requires the vLLM backend and does not support batch inference or returned timestamps. The later -hf checkpoints are native-Transformers packaging, not independently trained peer identities.
- Recordings and transcripts remain sensitive; authorize capture and review recognition errors before consequential use.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
