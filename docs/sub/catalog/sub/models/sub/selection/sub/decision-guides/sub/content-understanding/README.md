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

## Candidate evaluation set

These candidates preserve useful hypotheses from the legacy perception, speech, and model-reference guides after current first-party identity/capability revalidation. Provider modality support establishes **eligibility to test**, not reliability for the stated understanding task.

| Candidate | Evaluate for | Evidence state | Main boundary |
| --- | --- | --- | --- |
| [Gemma 4 E2B Instruct](../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) | Lowest-footprint bounded local/private image, document, UI, or short-audio understanding experiments | Provider-documented multimodal model; legacy AI Lab candidate hypothesis | Compact size and accepted modalities do not establish OCR, grounding, ASR, timestamp, diarization, or target-language quality |
| [Gemma 4 E4B Instruct](../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) | Stronger compact local multimodal experiments for OCR-adjacent document, chart, UI, image, and short-audio understanding | Provider-documented multimodal model; legacy AI Lab candidate hypothesis | Stored/runtime footprint and task-specific accuracy must be measured; it is not a calibrated evaluator by default |
| [Gemini 3.6 Flash](../../../reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/) | High-frequency hosted analysis of mixed text, image, PDF, video, or audio inputs where broad modality/tool support matters | Current provider-documented multimodal capabilities; AI Lab task accuracy unverified here | Exact API surface, preview features, data path, sampling/coverage, and assignment-specific precision require current evaluation |
| [GPT-5.6 Sol](../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/sol/) | Difficult document, screenshot, chart, UI, and mixed-evidence reasoning where a capability-first hosted route is worth testing | Current provider positioning for complex multimodal reasoning/tool work; AI Lab task accuracy unverified here | Provider positioning does not establish grounding, coverage, or best accepted-result cost and requires independent evidence |
| [Claude Sonnet 5](../../../reference/sub/producers/sub/anthropic/sub/claude/sub/sonnet/sub/models/sub/sonnet-5/) | Long documents, screenshots, technical analysis, and instruction-heavy multimodal understanding | Current provider-documented knowledge-work, vision, coding, and agentic capabilities; AI Lab task accuracy unverified here | Long context and provider claims do not prove complete page/figure coverage, grounding, or judge calibration |
| [Mistral Small 4](../../../reference/sub/producers/sub/mistral-ai/sub/mistral-small/sub/models/sub/mistral-small-4/) | Self-hosted image and document understanding when one open-weight multimodal generalist is also being evaluated for reasoning/coding/agent roles | Current provider-documented multimodal model plus explicit legacy AI Lab image/document hypothesis | Large-model infrastructure and generalist breadth do not establish OCR/layout/grounding accuracy; compare against compact or hosted multimodal routes on representative evidence |
| [Whisper](../../../reference/sub/producers/sub/openai/sub/whisper/) | Discovery baseline for local/private multilingual ASR, transcription, speech translation, and language-identification experiments | Provider-documented ASR family; legacy AI Lab candidate hypothesis | A material evaluation or recommendation must pin an exact checkpoint/model/artifact and runtime; family-level capability does not establish language, timestamp, speed, or memory outcomes |

Candidate membership does not imply recommendation state. Pin the exact identity used by the evaluation, record the modality/input distribution and date, and recheck mutable hosted surfaces when they materially affect the comparison.

### Non-model diarization pipeline

`pyannote/speaker-diarization-community-1` remains useful for evaluating local speaker diarization, but upstream identifies it as a **pretrained `pyannote.audio` pipeline**, not one canonical trained-model identity. It is therefore intentionally absent from this model-candidate table and from Model Reference. Its software/pipeline ownership now lives under [`pyannote.audio`](../../../../../../sub/software/sub/model-and-data-platforms/sub/model-libraries/sub/pyannote-audio/), where access, licensing, offline use, telemetry, and pipeline boundaries are documented.

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

Do not force a diarization pipeline into the canonical model taxonomy merely because an older page lived under `models/`. Use its proper software/pipeline owner and keep model selection limited to actual model identities.

### Short-audio multimodal understanding

A multimodal model that accepts audio may be useful for bounded audio understanding, transcription, translation, or follow-up reasoning, but audio-input support alone does not establish streaming, timestamps, diarization, long-form transcription, or target-language accuracy. Evaluate the actual clip duration, language, task, output contract, and evidence requirements.

### Multilingual speech

Evaluate every language, accent, and code-switch pattern separately. For Ukrainian production claims, include representative regional/speaker variation, technical terminology, names, numerals, dates, abbreviations, code-switching, and qualified native review where linguistic quality matters.

## Ownership boundary

Real-time voice-agent stacks combine VAD/end-of-turn detection, networking, ASR, reasoning, tools, TTS, interruption control, and recovery. Selecting that complete stack is broader solution/workflow selection and does not belong here merely because models are components.

Hosted speech endpoints, service pricing/retention/regions, runtime choice, hardware planning, privacy operations, and end-to-end conversational architecture remain outside model-selection ownership. This page may record those conditions only when they are necessary evidence boundaries for comparing exact models.

A model accepting a modality is not proof that it is reliable for the required understanding task. Link intrinsic capabilities and limits from [Model Reference](../../../reference/) and keep task evidence here.
