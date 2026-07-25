# Choosing Perception and Evaluation Models and Workflows

Use this guide to select an exact model, service, deployment, or smallest practical workflow for image, document, video, audio, or multimodal understanding and for evaluating model-generated or human-produced artifacts.

## Translations

- English

## Status

Initial canonical guidance verified on 2026-07-25. Multimodal models, accepted media, resolution handling, context limits, endpoints, prices, licenses, regional availability, and evaluator behavior change; verify the complete assignment before adoption.

## Define the workload first

Perception and evaluation are not one interchangeable capability. Separate the actual work:

- image classification, tagging, captioning, comparison, and visual question answering;
- object, region, text, symbol, face, product, defect, or anomaly localization;
- spatial, geometric, count, relationship, chart, map, diagram, UI, screenshot, and scene understanding;
- optical character recognition (OCR), handwriting recognition, and document transcription;
- layout, reading order, table, form, key-value, field, checkbox, signature-presence, and document-structure extraction;
- document classification, splitting, retrieval preparation, and evidence-grounded question answering;
- video captioning, event recognition, temporal localization, continuity, motion, and multi-shot understanding;
- audio event, acoustic scene, music, and non-speech understanding;
- combined image, video, audio, document, and text reasoning;
- deterministic validation of files, schemas, dimensions, timing, counts, checksums, or constraints;
- automated evaluation using task-specific metrics;
- model-as-a-judge or multimodal-model-as-a-judge triage;
- qualified human review and adjudication.

Do not select from one aggregate multimodal benchmark. A model can answer broad scene questions while failing small text, exact counts, table cells, diagrams, spatial relationships, long video, or evidence localization. A model can also produce the expected final answer while misperceiving the input and compensating through prior knowledge or guessing.

## Freeze the assignment unit

Treat a recommendation as a claim about one complete perception or evaluation assignment. Record:

- exact downloadable artifact and revision, or exact API service, model ID, endpoint, region, and snapshot when exposed;
- provider, runtime, hardware, weight format, quantization, prompts, parameters, tools, permissions, and output schema;
- input modalities, containers, codecs, dimensions, resolution, color space, page count, duration, frame rate, sample rate, channels, and compression;
- preprocessing, resizing, tiling, frame sampling, page rendering, OCR, audio extraction, chunking, and ordering;
- target objects, regions, fields, relations, events, times, speakers, evidence, and required granularity;
- reference answers, annotations, schemas, rubrics, tolerances, uncertainty representation, and abstention policy;
- whether the assignment requires perception only, reasoning over perceived evidence, or both;
- whether evaluated content can contain untrusted text or instructions;
- quality tier and risk classification;
- privacy, retention, residency, biometric, copyright, confidentiality, and permitted-use boundaries;
- evaluation suite, reviewers, calibration set, evidence, limitations, and verification date.

Create a separate assignment when a material field changes. Do not transfer results between native images and rendered pages, one resolution and another, short and long video, sparse and dense frame sampling, one document family and another, one quantization and another, or perception and judge roles without evidence.

## Set task-specific acceptance gates

Use the repository's five [quality tiers](../combined-workloads/#quality-tiers) and translate the selected tier into observable gates.

| Tier | Perception and evaluation gate |
| --- | --- |
| Exploration | Produce labeled observations or rankings quickly; visible misses, uncertain grounding, and manual correction are acceptable, but output is not approved for consequential use |
| Concept draft | Capture the central visual, document, temporal, or acoustic content well enough for review; identify uncertainty and missing evidence |
| Working result | Meet declared extraction, grounding, localization, consistency, and technical thresholds; pass required validators and disclose known limitations |
| Production quality | Pass all pre-registered task, subgroup, calibration, adversarial, privacy, safety, and independent review gates required for deployment |
| Exceptional quality | Add stricter fine-grained perception, expert annotation, multi-reviewer adjudication, robustness, provenance, and specialist validation where the extra value justifies the cost |

Do not use a fluent explanation, high judge score, or correct final label as the only gate. Production claims should include evidence that the required input elements were actually detected and grounded.

## Separate perception, reasoning, and judgment

Use explicit stages where the distinction matters:

```text
input -> deterministic preparation -> perception and extraction -> evidence record -> reasoning or transformation -> deterministic checks -> independent evaluation -> human approval
```

A combined multimodal model may perform several stages in one call, but the evaluation should still distinguish:

- **perception failure:** the relevant object, text, relation, event, or sound was missed or misread;
- **grounding failure:** a claim lacks a valid region, page, timestamp, source span, or other evidence pointer;
- **reasoning failure:** the evidence was perceived correctly but used incorrectly;
- **instruction failure:** the model ignored task constraints or followed instructions embedded in untrusted content;
- **format failure:** the semantic result may be useful but does not satisfy the schema or technical contract;
- **judge failure:** the evaluator accepted a defective result or rejected a correct one.

This taxonomy prevents a correct guess from hiding a perception defect and prevents a judge's disagreement from being mistaken for generator failure.

## Select the smallest complete workflow

Start with constraints that can eliminate candidates:

1. Reject artifacts or services whose modalities, limits, license, region, privacy, retention, or permitted use do not cover the assignment.
2. Reject routes that cannot preserve the required resolution, page order, timestamps, channels, duration, or evidence granularity.
3. Use deterministic parsers, decoders, renderers, metadata tools, OCR, geometry, or schema validators when they solve the requirement more reliably than a general model.
4. Evaluate eligible candidates on a frozen representative and adversarial suite.
5. Compare total cost and latency per accepted image, page, document, minute, event, extraction, or evaluated artifact.
6. Choose the least expensive complete assignment that consistently reaches the tier, then define a separately validated fallback.

The smallest complete workflow may combine:

- native file parsing and metadata validation;
- specialized OCR, layout, detection, segmentation, or audio-event models;
- a general multimodal model for semantic interpretation;
- deterministic calculators, geometry, table, or schema logic;
- a separately calibrated model judge for triage;
- qualified human review for ambiguous, high-value, or consequential cases.

Do not use a general multimodal model to estimate a value that can be read exactly from structured source data. Do not replace a visual check with extracted text when color, position, shape, damage, or visual context is material.

## Image and visual-scene understanding

Define whether the model must identify, count, compare, localize, describe, or reason. Test:

- small, distant, occluded, rotated, reflected, transparent, repeated, or partially cropped objects;
- exact counts, duplicates, absence, and negative constraints;
- 2D and 3D spatial relationships, direction, ordering, containment, contact, and overlap;
- perspective, scale, depth, shadows, reflections, and camera effects;
- text at different sizes, fonts, orientations, scripts, contrast, blur, and compression;
- charts, axes, legends, units, annotations, tables, diagrams, maps, screenshots, UI state, and icons;
- color, texture, material, defect, damage, anatomy, geometry, and fine detail;
- multiple images, before-and-after comparisons, visual differences, and cross-image identity or product consistency;
- adversarial or irrelevant visual text that attempts to redirect the evaluator.

When localization matters, require bounding boxes, polygons, masks, keypoints, or explicit region references and score them independently from the verbal answer. A correct label with an incorrect region is not a grounded success.

## Document perception and extraction

Separate native-document parsing from page-image perception. Preserve the original file and record whether text, tables, links, form fields, annotations, metadata, reading order, or accessibility structure were available natively.

Evaluate, as applicable:

- printed and handwritten OCR;
- characters, words, lines, paragraphs, and reading order;
- page, section, heading, list, footnote, header, footer, and figure structure;
- tables, merged cells, row and column spans, repeated headers, nested tables, and cell relationships;
- key-value pairs, entities, selection marks, signatures or stamps, and confidence;
- document type, splitting, attachments, and page association;
- layout coordinates and source spans;
- equations, code, diagrams, charts, and mixed scripts;
- scans, photographs, skew, perspective, shadows, folds, stains, blur, low contrast, handwriting, and compression;
- long documents, cross-page references, appendices, repeated forms, and conflicting versions.

Require a schema with field meaning, type, cardinality, source evidence, missing-value policy, normalization, and validation rules. A plausible value without a valid source span or region should fail evidence-grounded extraction.

For retrieval preparation, evaluate whether chunks preserve headings, table context, page references, and source traceability. Retrieval success on a few questions does not prove faithful document conversion.

## Video and temporal understanding

Freeze:

- native video versus sampled frames;
- sampling rate, key-frame policy, scene detection, clip length, overlap, audio inclusion, and ordering;
- target event duration and required temporal precision;
- whether camera cuts, repeated actions, identities, objects, or causality span multiple shots;
- whether the answer must reference exact timestamps or frames.

Measure:

- event and action recognition;
- temporal order, duration, start and end boundaries;
- object permanence, count, identity, state changes, and continuity;
- motion direction, interaction, causality, and camera movement;
- dialogue, sound, visual event, and subtitle synchronization;
- long-context recall and evidence retrieval;
- performance under altered sampling, compression, speed, missing frames, and unrelated scenes.

A model that sees only sampled frames cannot establish what happened between them. State the sampling limitation rather than presenting an inference as direct observation.

## Audio and non-speech perception

Separate speech recognition from acoustic understanding. Test, as required:

- sound-event presence, absence, count, timing, and overlap;
- acoustic scene, ambience, environment, and recording conditions;
- music, instruments, rhythm, structure, genre, and transitions;
- alarms, impacts, machinery, animals, vehicles, and safety-relevant signals;
- clipping, silence, noise, reverberation, channel differences, and codec artifacts;
- synchronization between audio and image or video events.

Use the [Speech and Conversation](../speech-and-conversation/) guide for ASR, diarization, TTS, and realtime voice interaction. Do not infer a real person's identity, health, emotion, intent, or protected traits from acoustic features without a separately permitted and validated process.

## Evaluation system design

### Use deterministic checks first

Before model judgment, run every applicable deterministic validator:

- file existence, checksum, MIME type, decode, dimensions, color space, alpha, page count, duration, frame rate, sample rate, channels, and codec;
- JSON, XML, CSV, subtitle, annotation, or domain schema validation;
- required keys, data types, ranges, units, counts, uniqueness, and referential integrity;
- exact text, regex, terminology, protected-token, and forbidden-content checks;
- geometric containment, overlap, distance, alignment, bounding-box, and mask checks;
- table dimensions, totals, formulas, and cross-field consistency;
- timestamp ordering, coverage, gaps, overlap, and synchronization;
- source-span or evidence-pointer validity.

A model judge should not decide facts that a deterministic validator can establish exactly.

### Define the rubric per sample or failure class

For open-ended work, provide explicit criteria tied to the sample or declared class:

- required facts and evidence;
- prohibited unsupported claims;
- severity definitions;
- allowed alternatives and equivalent forms;
- handling of uncertainty, ambiguity, missing information, and abstention;
- weighting and terminal acceptance rule.

Avoid one vague instruction such as “score quality from 1 to 10.” It hides disagreements between correctness, completeness, grounding, style, safety, and technical validity.

### Calibrate model judges against humans

A model judge is a measured component, not an authority. Validate it on representative human-adjudicated cases and report:

- agreement, accuracy, precision, recall, false-accept, and false-reject rates by failure class;
- rank, pairwise, or score correlation where meaningful;
- calibration of confidence or score bands;
- position consistency after swapping candidate order;
- sensitivity to length, style, formatting, names, provider, and model family;
- self-preference or same-family preference;
- stability across repeated runs and prompt variants;
- robustness to instructions embedded in evaluated images, documents, audio transcripts, or outputs;
- performance on near-ties, adversarial defects, missing evidence, and out-of-distribution cases.

Recent primary research reports position, self-preference, modality-neglect, and adversarial visual biases in model-as-a-judge systems. Use those results as reasons to measure the deployed judge, not as universal correction factors. Relevant research includes [Judging the Judges](https://arxiv.org/abs/2406.07791), [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819), [Fooling the LVLM Judges](https://aclanthology.org/2025.emnlp-main.1182/), and [MM-JudgeBias](https://aclanthology.org/2026.acl-long.1162/).

### Reduce avoidable judge bias

For pairwise evaluation:

- blind provider, model, and author identity when they are not part of the criterion;
- randomize candidate order and repeat with swapped positions;
- treat inconsistent swaps as judge uncertainty rather than forcing a winner;
- separate criteria before producing an overall result;
- use deterministic tie rules and permit `tie`, `both fail`, and `insufficient evidence`;
- prevent evaluated content from becoming evaluator instructions;
- use a judge from a different model family where practical, but still calibrate it;
- send high-risk, close, contradictory, or unsupported cases to human adjudication.

Do not average several correlated judge calls and call the result independent verification. Independence depends on model family, prompt, evidence, failure modes, and reviewer process, not call count.

## Report measurable outcomes

Pre-register the eligible unit: image, object, region, field, table cell, page, document, frame, event, clip, audio segment, artifact, pair, or judgment. Keep no-output, decode, timeout, policy-blocked, schema-invalid, and failed attempts in the denominator when they occur under deployed conditions.

| Outcome | Numerator / denominator |
| --- | --- |
| Terminal acceptance | Eligible units meeting every declared perception, grounding, reasoning, format, and review gate after permitted correction or escalation / all eligible units |
| Exact or normalized extraction accuracy | Correct extracted fields, spans, cells, labels, or relations under the frozen normalization policy / all applicable reference units |
| Detection or localization quality | True-positive, false-positive, false-negative, intersection-over-union, boundary, keypoint, or mask outcomes under declared matching and threshold rules / all eligible annotated units |
| Evidence-grounding pass | Eligible claims whose cited region, page, source span, frame, timestamp, or audio segment supports the claim / all eligible claims requiring evidence |
| Hallucination rate | Eligible outputs containing at least one unsupported object, field, event, relation, quote, or claim / all eligible outputs, with unsupported item counts also reported |
| Temporal localization | Eligible events whose predicted interval satisfies the declared overlap or boundary tolerance / all eligible reference events |
| Technical validity | Eligible artifacts passing each named decoder, schema, dimension, page, duration, channel, timing, or evidence-pointer check / all eligible artifacts scheduled for that check |
| Judge false acceptance | Defective human-adjudicated cases accepted by the judge / all defective human-adjudicated cases |
| Judge false rejection | Correct human-adjudicated cases rejected by the judge / all correct human-adjudicated cases |
| Judge order consistency | Eligible pairwise cases with equivalent decision after candidate-order swap / all eligible swapped cases |
| Human disagreement | Eligible cases without initial reviewer agreement / all independently reviewed cases, with adjudicated outcomes reported separately |
| Latency | End-to-end time from input readiness to terminal disposition, including preparation, inference, validation, judging, review, and escalation |
| Cost per accepted result | Total model, API, GPU, storage, transfer, annotation, review, and escalation cost / accepted terminal units |

Report outcomes by modality, task, resolution, length, language, subgroup, and failure condition. Aggregate accuracy can hide systematic failures on small text, long documents, overlap, low contrast, particular scripts, or consequential fields.

## Candidate assignments

These candidates are starting points for evaluation, not quality rankings. Product facts below were rechecked against primary sources on 2026-07-25; verify current model IDs, endpoints, accepted media, limits, licenses, infrastructure, and pricing before deployment.

### OpenAI GPT-5.6 tiers

**Candidate role:** Hosted image and document-image perception with text reasoning, tools, and structured output.

OpenAI's current [model catalog](https://developers.openai.com/api/docs/models) states that GPT-5.6 Sol, Terra, and Luna support text and image input with text output, multilingual and vision capabilities. The exact [GPT-5.6 Terra model page](https://developers.openai.com/api/docs/models/gpt-5.6-terra), for example, distinguishes image input from unsupported native audio and video input and exposes image-detail behavior, context, tools, and snapshots. Canonical repository pages describe the [GPT-5.6 family](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/) and tiers.

Before evaluation:

- pin the exact tier and snapshot when available, endpoint, reasoning effort, image detail, prompt, tools, schema, organization or project, region behavior, and data controls;
- render documents or extract native text deliberately and record which representation the model received;
- test small text, diagrams, charts, counts, spatial relations, multiple images, and evidence localization separately;
- measure token, latency, and cost effects of original or high-detail images and long context;
- do not infer native audio or video understanding from image capability or tool access.

Use Sol, Terra, and Luna as separate assignments. A cheaper tier may be preferable for high-volume extraction only after it passes the exact suite.

### Google Gemini 3.6 Flash

**Candidate role:** Hosted high-throughput multimodal understanding across text, image, video, audio, and PDF inputs with text output.

Google's current [Gemini 3.6 Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash) lists text, image, video, audio, and PDF input, text output, a stable model code, large context, thinking, structured outputs, tools, and current consumption options. The canonical repository page records the [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) identity and verified profile.

Before evaluation:

- pin the stable or explicit version, API, project, region behavior, thinking level, media resolution, file handling, frame or audio processing, and output schema;
- test each modality and combined-modality assignment separately;
- record how long video, audio, PDF pages, frames, timestamps, and file references are represented and billed;
- verify unsupported output modalities and preview tools independently;
- measure grounding, temporal evidence, long-context retrieval, latency, quota, and total accepted-result cost.

Do not treat support for a media type as proof of fine-grained perception, native frame coverage, or production-quality evidence localization.

### Mistral Small 4

**Candidate role:** Open or hosted text-and-image perception and document understanding where Apache-2.0 weights and controlled deployment justify enterprise-scale hardware.

Mistral's official [Mistral Small 4 announcement](https://mistral.ai/news/mistral-small-4/) describes an Apache-2.0 multimodal model with text and image input for document understanding and multimodal analysis. The canonical [Mistral Small 4 page](../../../../../../../software/sub/models/sub/mistral-ai/sub/mistral-small/sub/mistral-small-4/) records the exact identity, access forms, architecture, context, API alias, pricing snapshot, and substantial official infrastructure guidance.

Before evaluation:

- pin the exact open artifact or hosted API model, revision, runtime, precision, quantization, prompt, reasoning mode, image preprocessing, and schema;
- verify dependency licenses and actual local hardware, memory, startup, throughput, and concurrency;
- evaluate hosted and open deployments separately;
- test document layout, small text, charts, screenshots, localization, and long-context evidence rather than relying on provider benchmark claims;
- compare total self-hosted cost with hosted cost per accepted result.

Do not interpret “open” or active-parameter counts as evidence that the model fits a consumer GPU.

### Qwen3-VL artifacts

**Candidate role:** Open text, image, and video perception baseline with multiple dense and mixture-of-experts sizes, instruct and thinking variants, and controlled self-hosted deployment.

The official [Qwen3-VL repository](https://github.com/QwenLM/Qwen3-VL) publishes code, deployment guidance, model references, and an Apache-2.0 repository license. It describes upgraded visual perception, spatial and video understanding, agent interaction, dense and mixture-of-experts architectures, and multiple sizes. Exact model-card licenses, revisions, dependencies, precision, and deployment support must be checked for the selected artifact.

Before evaluation:

- name the exact size, architecture, instruct or thinking variant, repository and weight revision, runtime, precision, quantization, visual tokenization, and media preprocessing;
- verify whether the selected artifact supports the required image count, video, resolution, context, structured output, and language;
- measure actual VRAM, RAM, storage, load time, throughput, frame coverage, and quality on target hardware;
- evaluate spatial, OCR, document, video, grounding, and judge assignments independently;
- do not transfer results from a flagship or FP8 deployment to a smaller or quantized artifact.

### Google Cloud Document AI

**Candidate role:** Managed specialized OCR, layout, form, field, classification, splitting, and retrieval-preparation workflows requiring structured document evidence.

Google Cloud's current [Document AI processor list](https://docs.cloud.google.com/document-ai/docs/processors-list) distinguishes OCR, form parser, layout parser, pretrained, custom extraction, classification, and splitting processors. Current layout-parser documentation describes text, tables, lists, context-aware chunks, bounding boxes, and optional image or table annotations.

Before evaluation:

- pin the processor type, processor and version IDs, project, location, endpoint, schema, file type, page limits, options, and client-library version;
- distinguish OCR, form parsing, layout parsing, pretrained fields, custom extraction, classification, and splitting;
- evaluate text, handwriting, reading order, tables, fields, bounding boxes, chunks, and source traceability separately;
- record Cloud Storage, IAM, logging, retention, residency, processor lifecycle, and review workflow;
- validate generated figure or table descriptions independently because generative annotations can introduce unsupported content.

### Azure Document Intelligence

**Candidate role:** Managed OCR, layout, prebuilt, and custom document extraction for Microsoft cloud and enterprise workflows.

Microsoft's current [Document Intelligence overview](https://learn.microsoft.com/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0) distinguishes Read, Layout, prebuilt, and custom models. The current [`prebuilt-layout` documentation](https://learn.microsoft.com/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0) describes extraction of text, tables, selection marks, figures, and document structure for supported file types.

Before evaluation:

- pin the resource, endpoint, region, API version, model ID, feature flags, schema, SDK, and supported input contract;
- distinguish Read, Layout, prebuilt, custom extraction, custom classification, and composed routes;
- verify current deprecations and migration guidance rather than reusing an older model ID or API assumption;
- evaluate OCR, handwriting, reading order, tables, fields, selection marks, figures, coordinates, and confidence independently;
- record storage, authentication, private networking, retention, training data, deletion, quota, and price assumptions.

## Choose local, hosted, or hybrid deployment

| Dimension | Local | Hosted | Hybrid |
| --- | --- | --- | --- |
| Privacy and residency | Can keep approved media and documents offline; still requires access, cache, logs, backups, telemetry, and deletion controls | Must satisfy provider processing, retention, region, review, and training-use terms | Classify and route inputs explicitly; OCR or redaction after upload does not protect the original media |
| Capability | Can compose exact OCR, detector, diarizer, VLM, and validator components | May offer current large multimodal context, specialized processors, scaling, and managed file handling | Define which modalities, evidence, quality, and context are lost on fallback |
| Operations | Measure model size, RAM or VRAM, preprocessing, batching, loading, media decoding, and maintenance | Measure upload, queue, file expiry, quotas, rate limits, version changes, and outages | Measure routing, duplicate storage, representation drift, and failure of either path |
| Cost | Include hardware occupancy, energy, storage, annotation, review, and idle capacity | Include tokens, pages, images, video or audio duration, storage, transfer, retries, and review | Include both stacks and orchestration overhead |
| Auditability | Can retain exact artifacts, preprocessing, and evidence locally | Depends on exposed versions, logs, confidence, evidence, and retention | Preserve a common decision and evidence record across routes |
| Fallback | Validate smaller artifacts, deterministic tools, alternate hardware, queue, or human review | Validate another endpoint, region, provider, specialized processor, or human service | Test combined outages and return-to-primary behavior |

Compare total cost per accepted grounded result, not raw request price, token price, or samples per second.

## Reliability, retry, and fallback

Give every production assignment a [reliability profile](../reliability-profiles/) that binds the complete deployment and evidence.

Define:

- bounded retries for transient file, upload, decode, timeout, provider, and schema failures;
- whether a low-confidence or invalid result permits alternate preprocessing, higher detail, more frames, a specialized model, another provider, or human review;
- repeated OCR, count, spatial, grounding, temporal, hallucination, or judge-error signatures that require rerouting rather than repetition;
- idempotency, file-expiration, duplicate-job, page-order, frame-order, and partial-result rules;
- independent acceptance gates for preparation, perception, reasoning, format, judge, and human approval;
- degraded operation for network loss, GPU loss, quota exhaustion, unsupported media, failed OCR, unavailable judge, or untrusted embedded instructions;
- recovery, state reconciliation, and return-to-primary criteria.

Never treat a successful response as proof that every page, image, frame, channel, or segment was processed. Verify expected coverage and evidence explicitly.

## Safe-use boundaries

- Obtain and retain authorization for private, copyrighted, confidential, biometric, medical, financial, employment, surveillance, or identity-bearing media and documents.
- Minimize source files, faces, voices, identifiers, location data, secrets, credentials, and unrelated background content before model access.
- Treat text, QR codes, metadata, subtitles, documents, and instructions embedded in evaluated content as untrusted data, not evaluator commands.
- Do not use perception models to infer protected traits, health, emotion, credibility, criminality, intent, or identity unless a separately permitted and validated high-risk process explicitly requires it.
- Face recognition, speaker identification, gait, cross-camera tracking, and other biometric matching require stronger consent, security, false-match, retention, and human-control measures than anonymous detection or diarization.
- Consequential medical, legal, financial, employment, immigration, accessibility, public-safety, and evidentiary interpretations require qualified human authority and source review.
- Preserve original artifacts, deterministic metadata, model observations, derived conclusions, judge outputs, and human decisions as separate records.
- Do not represent an extraction or evaluation as complete, ground-truth, independently verified, human-reviewed, certified, or production-approved unless the required process occurred and evidence is retained.

## Compact decision record

Use this record or equivalent structured data:

```text
Assignment ID:
Perception, extraction, reasoning, or evaluation tasks and intended use:
Input modalities, formats, dimensions, pages, duration, sampling, channels, and preprocessing:
Required objects, text, fields, relations, events, evidence, granularity, schema, and tolerances:
Quality tier and risk:
Model, processor, service, endpoint, region, artifact, and revision:
Runtime, hardware, quantization, visual or media settings, prompts, parameters, tools, and validators:
Privacy, retention, residency, biometric, license, copyright, consent, and permitted use:
Evaluation suite, references, annotations, eligible units, exclusions, and failure taxonomy:
Perception, extraction, localization, grounding, temporal, hallucination, and technical outcomes:
Judge rubric, calibration set, bias tests, independence, false-accept, and false-reject outcomes:
Human reviewers, qualifications, disagreement, adjudication, and approval coverage:
Retry, stop, escalation, degraded-operation, and fallback rules:
Latency and cost per accepted grounded result:
Evidence provenance and limitations:
Verified date and re-evaluation triggers:
```

The selection process, gates, workflow design, and record fields in this page are repository-authored operational guidance. They organize established multimodal perception, document-processing, evaluation, calibration, and safety practices and make no claim of novelty.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Generative Media](../generative-media/)
- [Speech and Conversation](../speech-and-conversation/)
- [Choosing Model Portfolios for Combined Workloads](../combined-workloads/)
- [Defining Model Reliability Profiles](../reliability-profiles/)
- [Models](../../../../../../../software/sub/models/)
- [Benchmarks](../../../../../benchmarks/)
- [Disclaimer](../../../../../../../disclaimer/)
