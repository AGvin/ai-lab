# Documentation Requirements

## Requirements

- Identify Qwen3.8-Omni-Flash-Realtime as the released `qwen3.8-omni-flash-realtime` model identity for real-time audio/video interaction.
- Preserve the current streaming text/audio/video input and text/audio output boundary, tool calling, MCP integration, multichannel audio, and video aggregation only while supported by first-party Model Studio documentation.
- Keep it distinct from the non-realtime `qwen3.8-omni-flash` analysis model and from generic speech-to-text/text-to-speech services.
- Treat transport/session semantics, audio formats, supported channels/languages, regions, pricing, rate/session limits, tool availability, model aliases, and lifecycle snapshots as freshness-sensitive.
- Preserve permissions and trust boundaries around remote MCP tools and streamed external content; capability does not imply authorization to invoke a tool.

## Validation

- The node remains the concrete realtime Qwen Omni model identity.
- Realtime transport/tool behavior is not generalized to all Qwen Omni models.
- Hosted-service details remain separate from trained-model identity.
