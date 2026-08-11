# Media Creation Model Selection

Choose specialist models for generated images, video, speech, music, sound, editing, and spatial media by the exact creative assignment and delivery requirements.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers image generation and editing, video generation and editing, speech generation, dubbing, music and sound generation, audio enhancement, synthetic/identity media, and 3D or spatial generation.

Generative-media selection is specialist-first rather than language-model-scale-first. The exact model or artifact, revision, runtime behavior, generation parameters, input references, output format, rights boundary, and review process are part of the evaluated assignment.

## Evaluation dimensions

Use modality-specific evidence. Depending on the task, measure prompt/reference adherence, composition, identity consistency where authorized, typography, artifacts, edit locality, temporal consistency, motion, audio synchronization, pronunciation, prosody, timing, originality risk, and delivery-format validity.

Also measure the workflow outcome: first-pass acceptance, accepted candidates per bounded generation budget, retries, edit effort, reviewer time, latency to terminal artifact, and cost per accepted result.

The generator must not be the sole approver of its own output. Use deterministic technical checks plus an independent QC model or human reviewer calibrated to the assignment.

## Candidate evaluation set

The current retained concrete media candidate from the legacy corpus is deliberately narrow. It is a **starting point for a text-to-image experiment, not a cross-media ranking**.

| Candidate | Evaluate for | Evidence state | Main boundary |
| --- | --- | --- | --- |
| [FLUX.1-schnell](../../../reference/sub/producers/sub/black-forest-labs/sub/flux/sub/flux-1/sub/models/sub/flux-1-schnell/) | Rapid local/private text-to-image concept generation and comparison against another exact approved image route | Current provider-published downloadable text-to-image model with Apache-2.0 license and low-step inference guidance; legacy AI Lab candidate hypothesis | Exact revision, runtime, precision, encoders/VAE, resolution, peak memory, prompt adherence, defect rate, rights workflow, and cost per accepted artifact require assignment-level measurement |

A legacy page calling another model a general “candidate for comparison” is not enough to add it here. A candidate entry requires a concrete task-fit hypothesis and current evidence sufficient to define what should be evaluated. New image/video/audio models can be added when that threshold is met without creating a universal ranking.

### Speech synthesis and dubbing

For text-to-speech, dubbing, voice conversion, or other speech-generation candidates, define the exact model/artifact, language, voice or identity boundary, input text/audio conditions, output format, quality tier, and permitted use. Depending on the assignment, evaluate:

- intelligibility and pronunciation;
- language, accent, terminology, names, numbers, and abbreviations;
- naturalness, prosody, pace, emotion, and style control;
- speaker or character consistency and long-form continuity;
- clipping, noise, breaths, silence, loudness, and delivery-format validity;
- first-audio latency, streaming stability, cancellation, and synthesis duration when those properties affect the model decision;
- correction effort, reviewer time, and accepted-result rate.

A pleasant short sample does not prove consistent long-form or production behavior. Streaming latency and concurrency are deployment-dependent evidence, not immutable model facts.

For multilingual speech generation, evaluate each language/accent separately. Ukrainian production claims should include pronunciation and stress for representative names, terminology, numerals, dates, abbreviations, and qualified native review where appropriate.

## Rights and provenance

Record applicable rights, consent, identity restrictions, privacy constraints, provenance, disclosure requirements, voice/model license, and permitted use before adoption. Technical capability does not establish a right to clone, imitate, publish, or commercially use a voice or other identity-conditioned output.

## Ownership boundary

A real-time voice assistant is a multi-component solution that may combine VAD, ASR, reasoning, tools, TTS, networking, interruption control, and recovery. Selecting the complete conversational stack is broader workflow/service selection and does not belong in this model-selection subtree.

Hosted voice catalogs, provider pricing/retention/regions, runtime choice, hardware planning, and end-to-end operational architecture remain outside model-selection ownership. They may be recorded only as evidence conditions when comparing exact generation models.

Operational infrastructure lifecycle and broader service/hardware selection belong outside model-selection ownership. Link intrinsic model facts from [Model Reference](../../../reference/).
