# Documentation Requirements

## Requirements

- Identify Gemini 3.5 Transcribe as Google's released speech-to-text Gemini model introduced in August 2026.
- Preserve the two official serving forms, `gemini-3.5-transcribe` for unary transcription and `gemini-3.5-transcribe-live` for Live API transcription, as serving/version routes of the same documented trained-model identity unless upstream evidence establishes separate trained models.
- Preserve source-backed transcription capabilities such as speaker diarization, word-level timestamps, custom vocabulary, and smart transcription while keeping endpoint limits and feature matrices freshness-sensitive.
- Keep product integrations in Gemini/Android and API transport details outside intrinsic model identity.

## Validation

- The model is not treated as preview merely because adjacent Gemini audio models remain preview-only; current Google deprecation/model documentation lists the Transcribe models outside the preview section.
- Unary and live endpoints are not duplicated as peer model identities without independent upstream identity evidence.
- Mutable limits and availability remain source-scoped.

## Verified identity and provenance

Speech-to-text model documented with unary gemini-3.5-transcribe and streaming gemini-3.5-transcribe-live serving forms; transport names do not establish distinct trained models.

## Source-scoped operating boundaries

- Unary requests accept up to one hour of audio, reduced to 30 minutes when diarization or word timestamps are enabled. Streaming sessions are limited to ten minutes and do not provide diarization or word timestamps. [Transcription model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe).
- Vocabulary biasing cannot be combined with diarization or word timestamps. Up to eight speakers are supported, but attribution above two speakers is experimental. Verify attribution before using it to assign statements to people. [Feature compatibility](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe).
- This transcription model does not expose function calling, code execution, or generative reasoning. Do not infer voice synthesis or Live-agent tool execution from its streaming endpoint. [Capability matrix](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe>
