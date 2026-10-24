# Documentation Requirements

## Requirements

- Identify Qwen3-TTS-12Hz-1.7B-Base using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-tts/models/qwen3-tts-12hz-1-7b-base`.
- Preserve canonical membership in `catalog/models/alibaba/qwen/qwen3-tts` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Qwen3-TTS-12Hz-1.7B-Base is a released Apache-2.0 12Hz speech-synthesis checkpoint. Standard voice cloning uses synthesis text, reference audio (`ref_audio`), and its transcript (`ref_text`); the Base checkpoint also supports downstream fine-tuning.
- Use the corresponding Qwen3TTSModel operation and its required inputs; Base, CustomVoice, and VoiceDesign are separate checkpoints, not interchangeable flags.
- Setting `x_vector_only_mode=True` uses only the reference speaker embedding and removes the `ref_text` requirement, but may reduce cloning quality.
- The 12Hz label describes the speech-token representation, not the output waveform sample rate; latency and memory depend on the selected runtime.
- Verify authorization for reference recordings and intended voice use; synthesized speech is not proof of speaker consent or authenticity.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
