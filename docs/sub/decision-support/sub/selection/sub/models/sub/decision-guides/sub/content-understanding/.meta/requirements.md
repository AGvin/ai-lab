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
- Include `gemini-3.5-transcribe`, `cohere-transcribe-03-2026`, `granite-speech-5-0-470m-turboctc`, `granite-speech-5-0-2b`, and `granite-speech-4-1-2b-plus` as current speech evaluation candidates when their exact serving/deployment, language, licensing, timing/diarization, translation, and workload boundaries match the assignment.
- Treat Gemini 3.5 Transcribe diarization, word-level timestamps, custom vocabulary, smart transcription, and unary/live serving as candidate eligibility evidence rather than proof of target-language or recording-condition quality; keep unary and Live API routes as serving forms of the same documented trained-model identity unless upstream evidence changes that boundary.
- Treat Cohere Transcribe language coverage, file limits, API/private-deployment availability, and IBM Granite Speech runtime/benchmark compatibility as freshness-sensitive. Granite Speech 5.0 470M TurboCTC is an Apache-2.0 multilingual ASR checkpoint whose current card explicitly lists English, French, German, Spanish, Portuguese, Italian, and Japanese; do not preserve its earlier English-only card state as the current scope. Granite Speech 5.0 2B is a separate Apache-2.0 multilingual ASR and bidirectional speech-translation checkpoint with its own prompt, language, keyword-biasing, punctuation/capitalization, segmentation, and runtime boundaries. Granite Speech 4.1 2B Plus is a separate speaker-attributed transcription/word-timestamp checkpoint; its October 2026 update is in-place state, and its lack of punctuation/capitalization must not be inferred from the Speech 5 checkpoints.
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
- Gemini 3.5 Transcribe, Cohere Transcribe, Granite Speech 5.0 470M TurboCTC, Granite Speech 5.0 2B, and Granite Speech 4.1 2B Plus remain distinct evaluation routes with explicit language/deployment/evidence boundaries rather than a copied provider-feature ranking.
- Gemini unary/live serving forms are not duplicated as independent trained models without upstream evidence; the current multilingual scope of Granite Speech 5.0 470M is preserved without being generalized beyond its listed languages, and Speech 5.0 2B or Speech 4.1 2B Plus capabilities are not inherited across checkpoints.
- Media and audio sampling limitations remain explicit.
- Family-level or modality-support claims are not treated as proof of exact speech-task quality.
- A family-level candidate is not presented as a concrete recommendation without pinning an exact model/checkpoint/artifact.
- Diarization is not conflated with transcription, speaker identification, authentication, or canonical model identity.
- Community-1 is not retained as an unresolved model residual after `pyannote.audio` software ownership has been materialized.
- Evaluation/QC task guidance is separated from content-understanding task guidance.
- No complete voice-agent workflow or hosted-service comparison is migrated into this page.
