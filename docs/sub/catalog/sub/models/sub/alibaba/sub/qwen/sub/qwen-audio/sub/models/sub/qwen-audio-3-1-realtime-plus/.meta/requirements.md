# Documentation Requirements

## Requirements

- Identify Qwen-Audio-3.1-Realtime-Plus as the released duplex speech model `qwen-audio-3.1-realtime-plus`.
- Preserve current text/audio input and text/audio output, function calling, web search, voice cloning, and real-time interaction behavior only while supported by first-party documentation.
- Keep the current limitation that web search and function calling cannot be enabled together unless first-party behavior changes.
- Keep this model distinct from Qwen-Audio 3.0 variants, Qwen Omni realtime models, TTS-only Qwen3-TTS variants, and hosting protocols.
- Treat context limits, audio-turn retention, voices, languages, transports, pricing, rate limits, regions, and protocol behavior as freshness-sensitive.

## Decision and Operational Boundaries

- qwen-audio-3.1-realtime-plus is the hosted duplex model for text/audio input and text/audio output.
- Function Calling and web search cannot be enabled together; the application must choose the supported tool configuration for a session.
- Voice cloning is separate from consent to clone a voice; treat uploaded voice samples and streamed conversations as sensitive data.
- Use the documented realtime session and regional authentication contract; a model response does not authorize a remote tool action.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete 3.1 realtime-plus model identity.
- Mutable serving/voice/protocol facts remain version- and region-scoped.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
