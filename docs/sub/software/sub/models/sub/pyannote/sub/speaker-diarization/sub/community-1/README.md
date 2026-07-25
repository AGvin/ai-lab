# Speaker Diarization Community-1

`pyannote/speaker-diarization-community-1` is a downloadable pyannote speaker-diarization pipeline used as a local candidate in the current model-portfolio profiles.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- Artifact: `pyannote/speaker-diarization-community-1`
- Primary workload: speaker diarization
- Access: gated Hugging Face repository; users must accept the model conditions and use an authorized access token for download
- License: CC-BY-4.0
- Deployment: downloadable pipeline for local processing through compatible pyannote.audio tooling

Access gating, license obligations, runtime dependencies, and any telemetry or account requirements must be verified again before operational adoption.

## Selection guidance

Consider Community-1 for batch or local diarization when recordings are allowed to remain on the target system. Validate:

- diarization error rate on the actual language, channel, speaker count, noise, overlap, and recording length;
- segmentation boundaries and short turns;
- alignment with the exact ASR checkpoint and transcript timestamps;
- peak VRAM and RAM, processing time, concurrency, and failure recovery;
- handling of uncertain speaker count and overlapping speech;
- output format stability and downstream correction workflow.

Do not use diarization labels as real-world identity claims. Labels such as `SPEAKER_00` distinguish voices within the processed recording unless a separate authorized identification process establishes identity.

## Evidence boundary

Artifact identity, access form, license, and intended diarization role are provider-documented. Accuracy, hardware fit, privacy posture, alignment quality, and accepted-result cost remain runtime- and workload-specific.

## Related pages

- [Speaker Diarization](../..)
- [pyannote models](../../../..)
- [Speech and Conversation](../../../../../../../../../notes/sub/comparisons/sub/model-selection/sub/speech-and-conversation/)

## Sources

- [Community-1 model card](https://huggingface.co/pyannote/speaker-diarization-community-1)
- [pyannote.audio repository](https://github.com/pyannote/pyannote-audio)
