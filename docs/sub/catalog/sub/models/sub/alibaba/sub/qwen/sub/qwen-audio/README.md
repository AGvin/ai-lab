# Qwen-Audio

This Qwen-Audio branch covers the current hosted realtime speech-conversation series.

## Decision and Operational Boundaries

- Keep speech-to-speech conversation separate from Qwen3-ASR transcription, Qwen3-TTS synthesis, and Qwen Omni multimodal members.
- Check each realtime model's input modalities and tools; the 3.1 Plus web-search and Function Calling options cannot be enabled together.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen-Audio-3.1-Realtime-Plus](./sub/models/sub/qwen-audio-3-1-realtime-plus/) |

## Primary Sources

- [Alibaba Cloud: qwen audio realtime user guides](https://www.alibabacloud.com/help/en/model-studio/qwen-audio-realtime-user-guides)
- [Alibaba Cloud: qwen audio 3 1 realtime plus](https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-realtime-plus)
