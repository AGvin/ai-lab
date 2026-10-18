# Documentation Requirements

## Requirements

- Identify GPT-4o Transcribe Diarize as the concrete released model described by its official references.
- Preserve the exact published identifier, provenance, task, and lifecycle without creating separate nodes for aliases, settings, or hosting options.
- Render all visible current entity relations and use descriptive official-source links.

## Content specification

- The API reference lists a 16,000-token context window, 2,000-token maximum output, and a June 1, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-4o-transcribe-diarize).

## Validation

- The documented access surface and published lifecycle are explicit.
- The model is distinct from its base model, sibling models, or alternative deployment services.


## Source-scoped operating boundaries

- OpenAI announced deprecation on August 26, 2026 and scheduled API shutdown for February 26, 2027. The notice names gpt-transcribe and gpt-live-transcribe as replacements; that does not establish feature-for-feature migration parity [API deprecations](https://developers.openai.com/api/docs/deprecations).
- Diarization is available through the Transcription API, not the Realtime API. Speaker segments and optional speaker references support attribution within a recording; they are not independent verification of a person’s identity [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).

## Source evidence

- [gpt-4o-transcribe-diarize model reference](https://developers.openai.com/api/docs/models/gpt-4o-transcribe-diarize).
- [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
