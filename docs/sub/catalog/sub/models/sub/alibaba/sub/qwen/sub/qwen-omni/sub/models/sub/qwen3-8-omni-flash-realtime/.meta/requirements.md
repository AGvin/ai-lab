# Documentation Requirements

## Requirements

- Identify Qwen3.8-Omni-Flash-Realtime as the released `qwen3.8-omni-flash-realtime` model identity for real-time audio/video interaction.
- Preserve the current streaming text/audio/video input and text/audio output boundary, tool calling, MCP integration, multichannel audio, and video aggregation only while supported by first-party Model Studio documentation.
- Keep it distinct from the non-realtime `qwen3.8-omni-flash` analysis model and from generic speech-to-text/text-to-speech services.
- Treat transport/session semantics, audio formats, supported channels/languages, regions, pricing, rate/session limits, tool availability, model aliases, and lifecycle snapshots as freshness-sensitive.
- Preserve permissions and trust boundaries around remote MCP tools and streamed external content; capability does not imply authorization to invoke a tool.

## Decision and Operational Boundaries

- qwen3.8-omni-flash-realtime is a separate persistent realtime interaction model with text/audio output and streaming audiovisual input.
- Remote MCP tools are supported, but authentication, approved tool access, and authorization of each consequential action belong to the application.
- WebSocket multichannel input supports 1, 2, or 4 channels; video aggregation is disabled by default and enabled by a session option. Do not flatten these into every transport's contract.
- Match workspace ID, regional endpoint, and API key, and distinguish session-history limits from the non-realtime model's context.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete realtime Qwen Omni model identity.
- Realtime transport/tool behavior is not generalized to all Qwen Omni models.
- Hosted-service details remain separate from trained-model identity.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
