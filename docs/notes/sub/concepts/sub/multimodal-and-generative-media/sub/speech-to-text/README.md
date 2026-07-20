# Speech-to-Text

Speech-to-text converts spoken audio into written transcripts and may also identify language, timestamps, speakers, or confidence values.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

An automatic speech-recognition system processes acoustic features and predicts text tokens. Accuracy depends on language, accent, microphone quality, noise, overlapping speakers, domain vocabulary, and audio compression.

## Practical use

- Meeting and interview transcription.
- Voice interfaces and commands.
- Subtitle generation.
- Search and summarization of recordings.
- Accessibility workflows.

## Trade-offs and limitations

Transcripts can omit punctuation, confuse names, or produce plausible words for unclear audio. Speaker diarization and word-level timestamps are separate capabilities and may have different error rates.

## Good practice

Preserve the original audio for verification. Provide domain vocabulary where supported. Mark low-confidence sections and review names, numbers, dates, and consequential statements.

## Common mistakes

- Treating a transcript as a verbatim legal record.
- Discarding audio after transcription.
- Ignoring consent and privacy requirements.
- Summarizing before correcting critical transcription errors.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Text-to-Speech](../text-to-speech/)
- [Multimodal Context](../multimodal-context/)
- [Data Privacy](../../../safety-privacy-and-reliability/sub/data-privacy/)
