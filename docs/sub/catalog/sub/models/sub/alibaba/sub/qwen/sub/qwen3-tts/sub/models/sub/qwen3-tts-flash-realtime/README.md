# Qwen3-TTS-Flash-Realtime

qwen3-tts-flash-realtime is the hosted realtime text-to-speech identity for general preset-voice synthesis.

## Decision and Operational Boundaries

- Keep instruction control on the Instruct identity; do not infer voice-cloning or voice-design capabilities merely from a realtime TTS name.
- Voice/language inventory and session controls are service-specific and are not inherited by open 12Hz checkpoints.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-TTS](../../../../) |

## Primary Sources

- [Alibaba Cloud: realtime tts user guide](https://www.alibabacloud.com/help/en/model-studio/realtime-tts-user-guide)
- [Alibaba Cloud: tts model](https://www.alibabacloud.com/help/en/model-studio/tts-model)
- [Alibaba Cloud: qwen3 tts flash realtime](https://www.alibabacloud.com/help/en/model-studio/qwen3-tts-flash-realtime)
