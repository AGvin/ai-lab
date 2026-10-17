# Documentation Requirements

## Requirements

- Define model selection for image, video, speech/speaker, audio, and document understanding by measurable task evidence.
- Preserve the deterministic-tools-first rule from the legacy perception guide.
- Require exact modality, sampling/coverage, evidence-localization, output-schema, and uncertainty conditions when material.
- Preserve relevant coverage, precision/recall, omission, hallucination, provenance, and inconclusive metrics.
- Preserve useful concrete model-candidate hypotheses from legacy perception, speech, and model-reference pages only after current first-party identity/capability verification; present them as task-specific evaluation candidates, not as copied quick-pick rankings.
- For every retained candidate, distinguish provider-documented modality/capability eligibility from AI Lab evidence for the exact understanding task; state the limitation or missing evidence that must be tested.
- Preserve a family-level candidate only as a discovery/benchmark starting point when the legacy hypothesis was family-level and require an exact checkpoint/model/artifact before a material recommendation or evaluation result.
- Preserve speech-recognition evaluation dimensions when applicable: WER/CER, omissions/insertions/repetitions, terminology/names/numbers, timestamps/segments, long-recording stability, accents/noise/overlap/channel conditions, and failed/no-output cases.
- Include `gemini-3.5-transcribe`, `cohere-transcribe-03-2026`, and `granite-speech-5-0-470m-turboctc` as current ASR evaluation candidates when their exact serving/deployment, language, licensing, and workload boundaries match the assignment.
- Treat Gemini 3.5 Transcribe diarization, word-level timestamps, custom vocabulary, smart transcription, and unary/live serving as candidate eligibility evidence rather than proof of target-language or recording-condition quality; keep unary and Live API routes as serving forms of the same documented trained-model identity unless upstream evidence changes that boundary.
- Treat Cohere Transcribe language coverage, file limits, API/private-deployment availability, and Granite Speech 5 runtime/benchmark compatibility as freshness-sensitive; keep the Apache-2.0 Granite Speech 5.0 470M TurboCTC checkpoint scoped to its documented English ASR role rather than generalizing it across languages.
- Compare ASR candidates on the target language/accent/noise/overlap/recording-length/timestamp/diarization requirements and accepted-result cost rather than from provider feature lists or generic speech benchmarks.
- Preserve diarization evaluation dimensions when applicable: diarization error rate, overlap, short turns, speaker-count assumptions, segment stability, long recordings, transcript alignment, and correction effort.
- State that diarization does not establish real-world identity and that an older pipeline placement under `models/` does not prove canonical model identity.
- Treat `pyannote/speaker-diarization-community-1` as a pretrained diarization pipeline used through the canonical `pyannote.audio` software/library owner under `catalog/software/model-and-data-platforms/model-libraries/pyannote-audio/`; do not relabel the pipeline as a model merely to fit this subtree.
- For short-audio multimodal models, distinguish audio-input support from evidence for streaming, timestamps, diarization, long-form ASR, or target-language quality.
- Require per-language/accent/code-switch evaluation rather than transferring speech results across languages or recording conditions.
- Distinguish accepting an input modality from being reliable for a specific understanding task.
- Recheck mutable hosted availability, aliases, preview capabilities, limits, prices, and provider surfaces at decision time when they materially affect a candidate comparison.
- Keep QC/judging ownership in `../evaluation-and-quality-control/` rather than mixing it into content-understanding pages.
- Keep complete voice-agent stacks, hosted speech-service selection, runtime/software selection, hardware planning, privacy operations, and end-to-end conversational architecture outside this model-selection subtree.
- Link canonical model facts from `../../../../../reference/`.

## Validation

- Deterministic evidence sources are not replaced by model assertions when available.
- Useful legacy model-candidate hypotheses are not discarded merely because they were embedded in legacy model-reference or mixed speech/perception pages.
- Every retained model candidate is framed as an evaluation starting point with explicit task scope and evidence boundary, not as an unsupported current winner.
- Gemini 3.5 Transcribe, Cohere Transcribe, and Granite Speech 5 remain distinct ASR evaluation routes with explicit language/deployment/evidence boundaries rather than a copied provider-feature ranking.
- Gemini unary/live serving forms are not duplicated as independent trained models without upstream evidence, and Granite Speech 5 English scope is not generalized to unsupported languages.
- Media and audio sampling limitations remain explicit.
- Family-level or modality-support claims are not treated as proof of exact speech-task quality.
- A family-level candidate is not presented as a concrete recommendation without pinning an exact model/checkpoint/artifact.
- Diarization is not conflated with transcription, speaker identification, authentication, or canonical model identity.
- Community-1 is not retained as an unresolved model residual after `pyannote.audio` software ownership has been materialized.
- Evaluation/QC task guidance is separated from content-understanding task guidance.
- No complete voice-agent workflow or hosted-service comparison is migrated into this page.
