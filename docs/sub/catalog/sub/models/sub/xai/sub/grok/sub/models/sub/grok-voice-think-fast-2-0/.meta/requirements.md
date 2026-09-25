# Documentation Requirements

## Requirements

- Identify Grok Voice Think Fast 2.0 as xAI's current flagship real-time speech-to-speech voice model, released on 2026-07-29.
- Preserve current text/audio input to text/audio output, reasoning, function calling, web/X/collections search, remote MCP, and real-time WebSocket conversation capabilities only while first-party documentation supports them.
- Treat `grok-voice-latest` as the mutable latest alias currently routing to this concrete model rather than a separate model identity.
- Keep voice inventory, session limits, telephony/SIP behavior, pricing, transport events, clusters, rate limits, and tool availability freshness-sensitive.

## Validation

- The model remains distinct from Grok Voice Transcribe 2.0 speech-to-text.
- The mutable latest alias is not materialized separately.
