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
