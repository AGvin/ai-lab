# Documentation Requirements

## Requirements

- Identify Qwen-Audio-3.1-Realtime-Plus as the released duplex speech model `qwen-audio-3.1-realtime-plus`.
- Preserve current text/audio input and text/audio output, function calling, web search, voice cloning, and real-time interaction behavior only while supported by first-party documentation.
- Keep the current limitation that web search and function calling cannot be enabled together unless first-party behavior changes.
- Keep this model distinct from Qwen-Audio 3.0 variants, Qwen Omni realtime models, TTS-only Qwen3-TTS variants, and hosting protocols.
- Treat context limits, audio-turn retention, voices, languages, transports, pricing, rate limits, regions, and protocol behavior as freshness-sensitive.

## Validation

- The node remains the concrete 3.1 realtime-plus model identity.
- Mutable serving/voice/protocol facts remain version- and region-scoped.
