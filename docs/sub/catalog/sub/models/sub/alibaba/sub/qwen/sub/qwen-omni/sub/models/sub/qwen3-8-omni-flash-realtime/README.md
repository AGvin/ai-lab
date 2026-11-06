# Qwen3.8-Omni-Flash-Realtime

qwen3.8-omni-flash-realtime is a separate persistent realtime interaction model with text/audio output and streaming audiovisual input.

## Decision and Operational Boundaries

- Remote MCP tools are supported, but authentication, approved tool access, and authorization of each consequential action belong to the application.
- WebSocket multichannel input supports 1, 2, or 4 channels; video aggregation is disabled by default and enabled by a session option. Do not flatten these into every transport's contract.
- Match workspace ID, regional endpoint, and API key, and distinguish session-history limits from the non-realtime model's context.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen Omni](../../../../) |

## Primary Sources

- [Alibaba Cloud: qwen3 8 omni flash realtime](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-omni-flash-realtime)
- [Alibaba Cloud: realtime](https://www.alibabacloud.com/help/en/model-studio/realtime)
