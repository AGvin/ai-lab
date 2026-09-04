# pyannote.audio

`pyannote.audio` is an open-source Python/PyTorch toolkit for speaker diarization. It provides pretrained models and pipelines and supports training or fine-tuning on task-specific data.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Provenance

- [Hervé Bredin](../../../../../../../producers/sub/h/sub/herve-bredin/) — original/current package author and producer of `pyannote.audio`; this authorship is not rendered as corporate ownership of the library.

## Software boundary

`pyannote.audio` is software, not a canonical trained-model identity. Pretrained artifacts loaded through the library remain distinct entities or pipeline artifacts.

The legacy AI Lab model tree placed `pyannote/speaker-diarization-community-1` under models. Current upstream documentation identifies Community-1 as a pretrained speaker-diarization pipeline loaded through `pyannote.audio`, so that old placement must not be used to classify the pipeline as a model.

## Community-1 pipeline

Community-1 assigns speaker labels to time regions in audio. It does not produce a transcript and does not establish a speaker's real-world identity. Neutral labels such as `SPEAKER_00` distinguish speakers within the processed recording unless a separate authorized identification process establishes identity.

Current upstream instructions require accepting the Hugging Face repository conditions before downloading Community-1. The pipeline can then be copied locally and used offline. The Community-1 repository is licensed under CC-BY-4.0; the `pyannote.audio` software repository uses the MIT license.

For practical evaluation, measure diarization error rate, overlapping speech, short turns, speaker-count assumptions, segmentation stability, recording conditions, long-recording behavior, alignment with the selected ASR output, correction effort, runtime, and memory.

## Privacy boundary

Local or offline inference does not by itself establish the privacy posture of the complete workflow. Upstream documents optional anonymous telemetry in `pyannote.audio`; privacy-sensitive deployments should verify the current telemetry configuration together with storage, logs, access, and downstream processing.

## Related pages

- [Model Libraries](../..)
- [Content Understanding Model Selection](../../../../../../../models/sub/selection/sub/content-understanding/)

## Sources

- [pyannote.audio package metadata](https://github.com/pyannote/pyannote-audio/blob/main/pyproject.toml)
- [pyannote.audio repository](https://github.com/pyannote/pyannote-audio)
- [Community-1 pipeline](https://huggingface.co/pyannote/speaker-diarization-community-1)
