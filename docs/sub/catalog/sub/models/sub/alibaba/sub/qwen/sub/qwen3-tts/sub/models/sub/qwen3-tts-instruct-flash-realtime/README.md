# Qwen3-TTS-Instruct-Flash-Realtime

qwen3-tts-instruct-flash-realtime is a released hosted text-to-speech model ID whose natural-language speaking-style control is documented in first-party release history and SDK references.

## Decision and Operational Boundaries

- As of 2026-10-19, the current speech-synthesis overview and realtime guide omit this ID while the SDK still documents it. Current regional availability is unconfirmed; confirm access before selecting it for a new integration.
- Keep instruction control on the Instruct identity; do not infer voice-cloning or voice-design capabilities merely from a realtime TTS name.
- Voice/language inventory and session controls are service-specific and are not inherited by open 12Hz checkpoints.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-TTS](../../../../) |

## Primary Sources

- [Alibaba Cloud: model release history](https://www.alibabacloud.com/help/en/model-studio/newly-released-models)
- [Alibaba Cloud: Qwen realtime TTS Python SDK](https://www.alibabacloud.com/help/en/model-studio/qwen-tts-realtime-python-sdk)
- [Alibaba Cloud: realtime tts user guide](https://www.alibabacloud.com/help/en/model-studio/realtime-tts-user-guide)
- [Alibaba Cloud: tts model](https://www.alibabacloud.com/help/en/model-studio/tts-model)
