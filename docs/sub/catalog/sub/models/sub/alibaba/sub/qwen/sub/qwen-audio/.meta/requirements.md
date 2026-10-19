# Documentation Requirements

## Requirements

- Identify Qwen-Audio as the Qwen speech-to-speech / real-time audio conversation model series.
- Preserve the series boundary around streaming audio/text interaction and speech output while keeping Qwen Omni, Qwen TTS-only models, generic ASR/TTS services, and Model Studio separate.
- Materialize current released concrete models where versioned real-time behavior or output contract materially changes reader decisions.
- Treat voices, cloned-voice support, languages, context, transports, tools/search, regions, pricing, quotas, audio formats, and lifecycle aliases as freshness-sensitive.
- Preserve Qwen Team production provenance.

## Decision and Operational Boundaries

- This Qwen-Audio branch covers the current hosted realtime speech-conversation series.
- Keep speech-to-speech conversation separate from Qwen3-ASR transcription, Qwen3-TTS synthesis, and Qwen Omni multimodal members.
- Check each realtime model's input modalities and tools; the 3.1 Plus web-search and Function Calling options cannot be enabled together.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen-Audio remains a model series rather than a WebSocket/AOQ service protocol.
- Speech-to-speech and TTS-only identities are not conflated.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
