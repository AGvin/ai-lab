# Documentation Requirements

## Requirements

- Identify Qwen-Audio as the Qwen speech-to-speech / real-time audio conversation model series.
- Preserve the series boundary around streaming audio/text interaction and speech output while keeping Qwen Omni, Qwen TTS-only models, generic ASR/TTS services, and Model Studio separate.
- Materialize current released concrete models where versioned real-time behavior or output contract materially changes reader decisions.
- Treat voices, cloned-voice support, languages, context, transports, tools/search, regions, pricing, quotas, audio formats, and lifecycle aliases as freshness-sensitive.
- Preserve Qwen Team production provenance.

## Validation

- Qwen-Audio remains a model series rather than a WebSocket/AOQ service protocol.
- Speech-to-speech and TTS-only identities are not conflated.
