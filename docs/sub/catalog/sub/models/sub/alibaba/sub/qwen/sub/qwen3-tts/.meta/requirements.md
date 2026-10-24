# Documentation Requirements

## Requirements

- Identify Qwen3-TTS as Qwen's released text-to-speech model series, including hosted realtime models and independently released 12Hz open checkpoints.
- Preserve the series boundary around text-to-audio speech synthesis; keep Qwen-Audio speech-to-speech, Qwen Omni, voice-cloning/design service operations, CosyVoice, and generic Model Studio TTS serving separate.
- Materialize stable named model identities where instruction/voice-control behavior materially changes reader decisions; keep date snapshots as serving versions rather than peer canonical identities.
- Treat voices, languages, audio formats, latency, interaction protocol, regions, pricing, quotas, snapshots, and lifecycle aliases as freshness-sensitive.
- Preserve Qwen Team producer provenance.

## Decision and Operational Boundaries

- Qwen3-TTS includes hosted realtime model IDs and released 12Hz open checkpoints for speech synthesis, preset voices, voice design, and voice cloning.
- Keep Base, CustomVoice, and VoiceDesign checkpoints distinct: reference-audio cloning, preset-voice synthesis, and description-based voice design have different input contracts.
- Do not transfer hosted voice inventories, API limits, or latency claims to local weights; runtime and streaming support require exact package/checkpoint verification.
- Use authorized voice samples and treat voice identity as sensitive input; speech synthesis does not establish consent or authenticity.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen3-TTS remains a model series rather than a WebSocket service identity.
- Stable model IDs and snapshots are not conflated.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
