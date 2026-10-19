# Gemini 3.5 Transcribe

Speech-to-text model documented with unary gemini-3.5-transcribe and streaming gemini-3.5-transcribe-live serving forms; transport names do not establish distinct trained models.

## Relations

- Member of: [Gemini](../../../../)

## Scope and boundaries

- Product integrations in Gemini/Android and API transport details remain outside intrinsic model identity.

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe>
- <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/>

## Source-scoped operating boundaries

- Unary requests accept up to one hour of audio, reduced to 30 minutes when diarization or word timestamps are enabled. Streaming sessions are limited to ten minutes and do not provide diarization or word timestamps. [Transcription model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe).
- Vocabulary biasing cannot be combined with diarization or word timestamps. Up to eight speakers are supported, but attribution above two speakers is experimental. Verify attribution before using it to assign statements to people. [Feature compatibility](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe).
- This transcription model does not expose function calling, code execution, or generative reasoning. Do not infer voice synthesis or Live-agent tool execution from its streaming endpoint. [Capability matrix](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe).
