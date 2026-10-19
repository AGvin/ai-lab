# Documentation Requirements

## Requirements

- Identify Qwen3-TTS-Instruct-Flash-Realtime as the released instruction-controlled Qwen3 TTS model ID recorded in first-party release history and SDK documentation.
- Preserve its documented natural-language speaking-style control; keep snapshot equivalence date-scoped and do not infer current callability from release history.
- Keep this model distinct from Qwen3-TTS-Flash-Realtime, voice-design/voice-clone variants, date snapshots, Qwen-Audio, and CosyVoice.
- Treat voice inventory, languages, audio formats, latency, protocol, snapshot equivalence, regions, pricing, and rate limits as freshness-sensitive.

## Decision and Operational Boundaries

- qwen3-tts-instruct-flash-realtime is a released hosted text-to-speech model ID whose natural-language speaking-style control is documented in first-party release history and SDK references.
- As of 2026-10-19, the current speech-synthesis overview and realtime guide omit this ID while the SDK still documents it. Current regional availability is unconfirmed; confirm access before selecting it for a new integration.
- Keep instruction control on the Instruct identity; do not infer voice-cloning or voice-design capabilities merely from a realtime TTS name.
- Voice/language inventory and session controls are service-specific and are not inherited by open 12Hz checkpoints.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the released Instruct model identity; current availability is not inferred from the stable identifier.
- Snapshot IDs remain serving versions rather than duplicate models.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
