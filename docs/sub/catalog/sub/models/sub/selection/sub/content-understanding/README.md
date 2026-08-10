# Content Understanding Model Selection

Choose models for understanding images, video, speech, audio, and documents by measurable coverage, grounding, provenance, and error requirements.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers image understanding, video understanding, speech and speaker analysis, audio understanding, and document understanding, including OCR-adjacent interpretation, visual question answering, layout reasoning, event analysis, automatic speech recognition (ASR), transcription-adjacent understanding, speaker diarization, short-audio multimodal interpretation, and structured extraction.

Use deterministic tools first when they can prove a property: native text extraction, OCR output, parsers, schema validation, media metadata, geometry, accessibility/DOM state, timestamps, and checksums. Models should interpret ambiguous evidence rather than replace available validators.

## Evaluation dimensions

Define the exact modality, resolution, page/frame/clip sampling, audio conditions, evidence localization, output schema, and acceptable uncertainty. Measure relevant field, region, page, frame, segment, speaker, or event coverage together with precision, recall, omission, hallucination, and inconclusive rates.

For documents and OCR-adjacent work, preserve reading order, table/form structure, page linkage, figure/caption association, and source-region provenance. For video/audio, define temporal sampling and do not infer absence of an event outside sampled regions.

### Speech recognition and transcription

Evaluate an exact model/checkpoint and artifact against representative audio for the target language and domain. Depending on the assignment, measure:

- word or character error rate;
- omissions, unsupported insertions, repetitions, and silence handling;
- names, numbers, terminology, punctuation, casing, and formatting;
- segment boundaries and timestamp accuracy when the model is expected to provide them;
- long-recording stability where applicable;
- robustness to accents, dialects, noise, music, overlap, telephony, channel variation, and codec/sample-rate changes;
- failed/no-output cases rather than silently retrying them away.

Family-level speech-recognition claims do not establish the quality of a particular checkpoint, language, artifact, or deployment route. Runtime throughput and memory may be recorded as evidence context when they affect a model choice, but runtime/software/hardware selection itself belongs outside this model-selection subtree.

### Speaker diarization

Diarization answers who spoke when inside a recording; it does not transcribe speech or establish a person's real-world identity. For a candidate model or pipeline component, evaluate diarization error rate, overlap, short turns, speaker-count assumptions, segment stability, long recordings, alignment with the chosen transcript, and correction effort.

Do not force a diarization pipeline into the canonical model taxonomy merely because an older page lived under `models/`. Exact model/pipeline ownership must be established separately before reference material is created.

### Short-audio multimodal understanding

A multimodal model that accepts audio may be useful for bounded audio understanding, transcription, translation, or follow-up reasoning, but audio-input support alone does not establish streaming, timestamps, diarization, long-form transcription, or target-language accuracy. Evaluate the actual clip duration, language, task, output contract, and evidence requirements.

### Multilingual speech

Evaluate every language, accent, and code-switch pattern separately. For Ukrainian production claims, include representative regional/speaker variation, technical terminology, names, numerals, dates, abbreviations, code-switching, and qualified native review where linguistic quality matters.

## Ownership boundary

Real-time voice-agent stacks combine VAD/end-of-turn detection, networking, ASR, reasoning, tools, TTS, interruption control, and recovery. Selecting that complete stack is broader solution/workflow selection and does not belong here merely because models are components.

Hosted speech endpoints, service pricing/retention/regions, runtime choice, hardware planning, privacy operations, and end-to-end conversational architecture remain outside model-selection ownership. This page may record those conditions only when they are necessary evidence boundaries for comparing exact models.

A model accepting a modality is not proof that it is reliable for the required understanding task. Link intrinsic capabilities and limits from [Model Reference](../../../reference/) and keep task evidence here.
