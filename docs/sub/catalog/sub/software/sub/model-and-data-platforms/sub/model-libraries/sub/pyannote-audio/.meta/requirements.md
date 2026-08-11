# Documentation Requirements

## Requirements

- Document `pyannote.audio` as an open-source Python/PyTorch speaker-diarization toolkit and model library, not as a trained model identity.
- State that the library provides pretrained diarization models and pipelines and supports training or fine-tuning on user data.
- Distinguish the `pyannote.audio` software library from pretrained pipeline artifacts loaded through it, including `pyannote/speaker-diarization-community-1`.
- Preserve the useful legacy Community-1 operational boundary: it is a speaker-diarization pipeline that assigns speaker labels over time; it does not transcribe speech and does not establish real-world speaker identity.
- State that current Community-1 access requires accepting the Hugging Face repository conditions before download and that the pipeline can subsequently be copied and used offline according to the upstream instructions.
- State that Community-1 is distributed under CC-BY-4.0 while the `pyannote.audio` library repository is MIT-licensed; do not conflate software and pipeline licensing.
- Preserve assignment-level evaluation requirements for diarization: diarization error rate, overlap, short turns, speaker-count assumptions, segmentation stability, recording conditions, long recordings, alignment with ASR timestamps, correction effort, runtime, and memory.
- Preserve the identity boundary that neutral diarization labels such as `SPEAKER_00` are within-recording labels unless a separate authorized speaker-identification process establishes identity.
- Mention that upstream documents optional anonymous telemetry in `pyannote.audio`; require privacy-sensitive deployments to verify current telemetry configuration and data handling rather than assuming local inference alone proves a complete privacy posture.
- Link model-selection guidance to the applicable content-understanding model-selection node rather than treating this software profile as a model recommendation.

## Validation

- `pyannote.audio` is not classified as a canonical model.
- Community-1 is described as a pretrained pipeline/artifact consumed through the library, not as the software library itself.
- Software and pipeline licenses are not merged.
- Diarization is not conflated with transcription, speaker identification, authentication, or real-world identity.
- Local/offline operation is not presented as proof of complete privacy without checking software telemetry and the surrounding workflow.
