# Qwen3-TTS

Qwen3-TTS includes hosted realtime model IDs and released 12Hz open checkpoints for speech synthesis, preset voices, voice design, and voice cloning.

## Decision and Operational Boundaries

- Keep Base, CustomVoice, and VoiceDesign checkpoints distinct: reference-audio cloning, preset-voice synthesis, and description-based voice design have different input contracts.
- Do not transfer hosted voice inventories, API limits, or latency claims to local weights; runtime and streaming support require exact package/checkpoint verification.
- Use authorized voice samples and treat voice identity as sensitive input; speech synthesis does not establish consent or authenticity.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3-TTS-12Hz-0.6B-Base](./sub/models/sub/qwen3-tts-12hz-0-6b-base/) |
| Includes | [Qwen3-TTS-12Hz-1.7B-Base](./sub/models/sub/qwen3-tts-12hz-1-7b-base/) |
| Includes | [Qwen3-TTS-12Hz-1.7B-CustomVoice](./sub/models/sub/qwen3-tts-12hz-1-7b-customvoice/) |
| Includes | [Qwen3-TTS-12Hz-1.7B-VoiceDesign](./sub/models/sub/qwen3-tts-12hz-1-7b-voicedesign/) |
| Includes | [Qwen3-TTS-Flash-Realtime](./sub/models/sub/qwen3-tts-flash-realtime/) |
| Includes | [Qwen3-TTS-Instruct-Flash-Realtime](./sub/models/sub/qwen3-tts-instruct-flash-realtime/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)
- [Alibaba Cloud: realtime tts user guide](https://www.alibabacloud.com/help/en/model-studio/realtime-tts-user-guide)
- [Alibaba Cloud: tts model](https://www.alibabacloud.com/help/en/model-studio/tts-model)
