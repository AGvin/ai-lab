# Qwen Omni

Qwen Omni groups multimodal understanding and speech interaction models with release-specific input and output contracts.

## Decision and Operational Boundaries

- Qwen3.8-Omni-Flash produces text; the separate Realtime identity produces text and audio. Do not promise speech output merely from the Omni family name.
- Keep HTTP analysis separate from persistent realtime sessions, history limits, and transport-specific features.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3.8-Omni-Flash](./sub/models/sub/qwen3-8-omni-flash/) |
| Includes | [Qwen3.8-Omni-Flash-Realtime](./sub/models/sub/qwen3-8-omni-flash-realtime/) |

## Primary Sources

- [Alibaba Cloud: qwen omni](https://www.alibabacloud.com/help/en/model-studio/qwen-omni)
- [Alibaba Cloud: qwen3 8 omni flash](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-omni-flash)
- [Alibaba Cloud: qwen3 8 omni flash realtime](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-omni-flash-realtime)
- [Alibaba Cloud: realtime](https://www.alibabacloud.com/help/en/model-studio/realtime)
