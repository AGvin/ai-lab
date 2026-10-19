# Documentation Requirements

## Requirements

- Identify Qwen3-TTS-Instruct-Flash-Realtime as the stable instruction-controlled real-time Qwen3 TTS model ID.
- Preserve natural-language speaking-style/emotion control and current stable-snapshot equivalence only while first-party documentation supports it.
- Keep this model distinct from Qwen3-TTS-Flash-Realtime, voice-design/voice-clone variants, date snapshots, Qwen-Audio, and CosyVoice.
- Treat voice inventory, languages, audio formats, latency, protocol, snapshot equivalence, regions, pricing, and rate limits as freshness-sensitive.

## Decision and Operational Boundaries

- qwen3-tts-instruct-flash-realtime is the hosted realtime text-to-speech identity with natural-language instruction control of speaking style.
- Keep instruction control on the Instruct identity; do not infer voice-cloning or voice-design capabilities merely from a realtime TTS name.
- Voice/language inventory and session controls are service-specific and are not inherited by open 12Hz checkpoints.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the stable concrete Instruct model identity.
- Snapshot IDs remain serving versions rather than duplicate models.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
