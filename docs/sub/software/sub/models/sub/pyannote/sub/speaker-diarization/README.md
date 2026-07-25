# Speaker Diarization

pyannote speaker-diarization pipelines identify who spoke when in an audio recording.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Scope

Speaker diarization assigns time segments to speaker labels. It does not produce the transcript itself and does not establish a real-world identity unless a separate, authorized speaker-identification process is used.

Evaluate diarization together with the transcription and alignment pipeline. A low diarization error rate can still produce unusable output when segment boundaries, overlap handling, or transcript alignment fail on the target recording.

## Documented versions

- [Community-1](./sub/community-1/) — gated local diarization pipeline used as a candidate in the current model portfolio profiles.

## Evaluation dimensions

- diarization error rate and its components;
- overlapping speech and short-turn handling;
- speaker-count assumptions;
- segmentation and timestamp stability;
- language, channel, noise, and domain variation;
- runtime, memory, batching, and long-recording behavior;
- alignment with the selected ASR system;
- access, license, privacy, and telemetry requirements.

## Related pages

- [pyannote models](../..)
- [Speech and Conversation](../../../../../../../notes/sub/comparisons/sub/model-selection/sub/speech-and-conversation/)

## Sources

- [pyannote.audio repository](https://github.com/pyannote/pyannote-audio)
