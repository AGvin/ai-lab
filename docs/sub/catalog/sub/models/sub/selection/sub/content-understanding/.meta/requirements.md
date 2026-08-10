# Documentation Requirements

## Requirements

- Define model selection for image, video, speech/speaker, audio, and document understanding by measurable task evidence.
- Preserve the deterministic-tools-first rule from the legacy perception guide.
- Require exact modality, sampling/coverage, evidence-localization, output-schema, and uncertainty conditions when material.
- Preserve relevant coverage, precision/recall, omission, hallucination, provenance, and inconclusive metrics.
- Preserve speech-recognition evaluation dimensions when applicable: WER/CER, omissions/insertions/repetitions, terminology/names/numbers, timestamps/segments, long-recording stability, accents/noise/overlap/channel conditions, and failed/no-output cases.
- Preserve diarization evaluation dimensions when applicable: diarization error rate, overlap, short turns, speaker-count assumptions, segment stability, long recordings, transcript alignment, and correction effort.
- State that diarization does not establish real-world identity and that an older pipeline placement under `models/` does not prove canonical model identity.
- For short-audio multimodal models, distinguish audio-input support from evidence for streaming, timestamps, diarization, long-form ASR, or target-language quality.
- Require per-language/accent/code-switch evaluation rather than transferring speech results across languages or recording conditions.
- Distinguish accepting an input modality from being reliable for a specific understanding task.
- Keep QC/judging ownership in `../evaluation-and-quality-control/` rather than mixing it into content-understanding pages.
- Keep complete voice-agent stacks, hosted speech-service selection, runtime/software selection, hardware planning, privacy operations, and end-to-end conversational architecture outside this model-selection subtree.
- Link canonical model facts from `../../../reference/`.

## Validation

- Deterministic evidence sources are not replaced by model assertions when available.
- Media and audio sampling limitations remain explicit.
- Family-level or modality-support claims are not treated as proof of exact speech-task quality.
- Diarization is not conflated with transcription, speaker identification, or authentication.
- Evaluation/QC task guidance is separated from content-understanding task guidance.
- No complete voice-agent workflow or hosted-service comparison is migrated into this page.
