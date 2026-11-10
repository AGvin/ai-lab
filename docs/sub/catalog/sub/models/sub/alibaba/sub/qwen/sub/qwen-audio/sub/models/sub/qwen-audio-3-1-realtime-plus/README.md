# Qwen-Audio-3.1-Realtime-Plus

qwen-audio-3.1-realtime-plus is the hosted duplex model for text/audio input and text/audio output.

## Decision and Operational Boundaries

- Function Calling and web search cannot be enabled together; the application must choose the supported tool configuration for a session.
- Voice cloning is separate from consent to clone a voice; treat uploaded voice samples and streamed conversations as sensitive data.
- Use the documented realtime session and regional authentication contract; a model response does not authorize a remote tool action.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen-Audio](../../../../) |

## Primary Sources

- [Alibaba Cloud: qwen audio 3 1 realtime plus](https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-realtime-plus)
- [Alibaba Cloud: qwen audio realtime user guides](https://www.alibabacloud.com/help/en/model-studio/qwen-audio-realtime-user-guides)
- [Alibaba Cloud: qwen audio realtime model access](https://www.alibabacloud.com/help/en/model-studio/qwen-audio-realtime-model-access)
