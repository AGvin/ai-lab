# Choosing Perception and Evaluation Models and Workflows

Select the smallest practical perception and evaluation workflow that reaches the required coverage, grounding, calibration, privacy, and cost target for image, screenshot, document, video, audio, multimodal, or judging work.

## Translations

- English
- [Українська](./l10n/uk_UA/)

**Status:** Compact local multimodal candidates and broader comparison structure updated on 2026-07-27. Accepted media, resolution handling, context, endpoints, prices, licenses, regional availability, and evaluator behavior change; verify the complete assignment before adoption.

## Quick picks

| Need | Start with | AI or model type | Scale | Route | Main reason |
| --- | --- | --- | --- | --- | --- |
| Compact private multimodal analysis | [Gemma 4 E2B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e2b-instruct/) | Multimodal general-purpose instruct model | SLM | Local or self-hosted | Lowest-footprint current canonical route for bounded image, document, UI, and short-audio experiments |
| Stronger compact local multimodal analysis | [Gemma 4 E4B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e4b-instruct/) | Multimodal general-purpose instruct model | SLM | Local or self-hosted | More compact-model capacity while retaining text, image, audio, OCR, document, and function-calling support |
| Fast hosted multimodal analysis | [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) | Multimodal general-purpose model | LLM | Hosted | Broad modality support, long context, native tools, and lower-latency loops |
| High-capability document or screenshot reasoning | [GPT-5.6 Sol](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/) or [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) | General-purpose multimodal reasoning model | LLM | Hosted | Strong reasoning, long-document handling, and complex instruction following |
| Reproducible extraction | Deterministic OCR, parsers, and exact specialist models | Specialist tools and models | Varies | Local or self-hosted | Provenance, repeatability, and measurable field or region accuracy |
| Model-based output evaluation | Independent calibrated judge plus deterministic validators | Evaluation workflow | Varies | Hosted, local, or hybrid | One model score is not proof; calibration and independent evidence are required |
| High-risk acceptance decision | Deterministic checks plus independent model and qualified human review | Hybrid evaluation workflow | Mixed | Hybrid | Separates measurable properties, ambiguous interpretation, and accountable approval |

These are starting routes, not universal rankings. The complete modality, sampling, evidence, and judge configuration is part of the evaluated assignment.

## Economical SLM candidates

| Candidate | Model type | Parameters | Architecture | Modalities | Access | Best fit | Main limitation | Sources |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| [Gemma 4 E2B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e2b-instruct/) | General-purpose multimodal instruct model | 2.3B effective; 5.1B including embeddings | Dense | Text, image, audio; video as frames | Open-weight; Apache-2.0 | Bounded private image description, UI or screenshot inspection, document extraction experiments, and short-audio understanding | Compact quality ceiling, short audio limit, and unproven calibration as an evaluator | [Official model card](https://ai.google.dev/gemma/docs/core/model_card_4) · [Hugging Face](https://huggingface.co/google/gemma-4-E2B-it) |
| [Gemma 4 E4B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e4b-instruct/) | General-purpose multimodal instruct model | 4.5B effective; 8B including embeddings | Dense | Text, image, audio; video as frames | Open-weight; Apache-2.0 | Stronger compact OCR, document, chart, UI, image, and short-audio experiments where local control matters | Stored parameter size and multimodal components exceed the effective count; still not a calibrated judge by default | [Official model card](https://ai.google.dev/gemma/docs/core/model_card_4) · [Hugging Face](https://huggingface.co/google/gemma-4-E4B-it) |

These SLMs are economical candidates for bounded perception, not automatic replacements for dedicated OCR, document parsers, detection models, audio systems, or calibrated evaluators. Measure field, region, page, frame, and event coverage plus human correction cost.

A model that accepts images or audio is not automatically suitable as a judge. Perception capability, evaluation reliability, scale class, deployment, and accepted-result cost are independent properties.

## Broader candidate routes

| Route | AI or model type | Best fit | Main limitation | Evidence to recheck |
| --- | --- | --- | --- | --- |
| [Gemma 4 E2B](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e2b-instruct/) or [E4B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e4b-instruct/) | Compact multimodal general-purpose model | Offline, private, edge, laptop, or controlled multimodal analysis with official local artifacts | Compact quality ceiling, runtime modality support, and no default judge calibration | Exact artifact, projection or encoder files, runtime, resolution, audio and video limits, hardware, and task evidence |
| [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) | Multimodal general-purpose model | High-frequency multimodal analysis, files, images, video, audio, structured output, and Google-native tools | Hosted data path, changing API behavior, preview features, and assignment-specific precision | Exact model alias, modalities, resolution and file limits, tools, region, data terms, price, and task evidence |
| [GPT-5.6 Sol](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/sol/) | General-purpose multimodal reasoning model | Difficult document, screenshot, chart, UI, and mixed-evidence reasoning where maximum capability matters | Paid hosted access, provider limits, and need for exact endpoint and workflow validation | Exact endpoint, accepted modalities, context, region, data terms, price, and evaluation evidence |
| [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) | General-purpose multimodal and agentic model | Long documents, screenshots, technical analysis, review, and instruction-heavy evaluation | Hosted access, provider terms, and unproven calibration on the target rubric | Exact model, modality support, context, data terms, price, rubric, and bias tests |
| Deterministic OCR and document parsers | Specialist deterministic software | Native text extraction, OCR, layout parsing, tables, forms, schemas, and reproducible provenance | Cannot resolve all semantic ambiguity or judge task compliance | Exact engine and version, language support, layout coverage, confidence behavior, and error distribution |
| Local specialist vision, audio, or document models | Specialist local models | Offline, low-latency, reproducible, or controlled narrow processing | Hardware, artifact, runtime, modality, and quality ceiling are pipeline-specific | Exact artifact, precision, runtime, resolution, sampling, hardware, license, and benchmark evidence |
| Independent model judge or jury | Evaluation model or multi-model workflow | Pairwise comparison, rubric scoring, triage, and scalable review after calibration | Position, style, verbosity, identity, self-preference, and correlated-error bias | Exact judge model, prompt, order randomization, calibration set, abstention policy, and human-overturn rate |

## Workload view

| Workload | Prefer | Escalate or reject when |
| --- | --- | --- |
| Image and screenshot description | Gemma 4 E2B or E4B for bounded private work; validated hosted model for harder cases | Small text, counts, relations, crop boundaries, or required state cannot be grounded reliably |
| UI, chart, diagram, and visual debugging | Multimodal model plus DOM, accessibility, screenshot, or geometry evidence | The model produces a plausible description without proving the expected state or defect |
| OCR and structured extraction | Native text extraction, OCR, layout parser, schema validation, then model interpretation | Reading order, fields, tables, checkboxes, page linkage, or provenance cannot be preserved |
| Long document understanding | Hosted multimodal model or staged parser-and-model workflow | Pages, figures, citations, or required cross-page relationships are skipped or hallucinated |
| Video or audio event understanding | Exact multimodal or specialist model with explicit sampling and timestamps | Sampling cannot cover the event, timing is material, or evidence localization is missing |
| Generated-media review | Deterministic technical checks plus independent multimodal review | The generator is the sole evaluator or required identity, consent, provenance, or rights checks are absent |
| Model-output judging | Calibrated independent judge, jury, deterministic metrics, or human review | Bias tests fail, disagreement is high, evidence is unavailable, or severity exceeds model authority |

## Define the assignment

Separate:

- image and screenshot description;
- UI, layout, chart, diagram, and visual-debug analysis;
- OCR and structured extraction;
- document understanding across text, tables, forms, figures, and page layout;
- video and audio event understanding;
- generated-media quality review;
- task-compliance, safety, policy, or factuality evaluation;
- pairwise comparison, ranking, scoring, jury, and acceptance decisions.

Record exact model or endpoint, region, runtime, hardware, accepted modalities, resolution, page or frame sampling, audio handling, prompt, schema, tools, context, rubric, quality tier, risk, data boundary, and verification date.

Do not transfer results between media types, resolutions, page counts, frame sampling, audio conditions, model versions, or judge prompts without evidence.

## Deterministic tools first

Use non-model tools where they can prove a property:

- file type, dimensions, duration, codec, checksums, and corruption;
- OCR engine output and confidence;
- PDF text and structure extraction;
- schema, required-field, range, and cross-field validation;
- image diff, pixel, bounding-box, color, and geometry checks;
- accessibility-tree, DOM, layout, and screenshot test output;
- audio levels, silence, clipping, and channel metadata;
- source citations, identifiers, and evidence retrieval.

Models should interpret ambiguous evidence, not replace available validators.

## Perception quality

### Images and screenshots

Measure object, attribute, relation, count, text, layout, state, defect, and instruction-grounding accuracy. Include small text, cropped elements, dense interfaces, unusual aspect ratios, and adversarial or irrelevant content.

For UI review, provide the expected state, viewport, interaction context, and deterministic test results. A plausible description is not proof that the page works.

### OCR and documents

Measure character or word error, reading order, table structure, key-value extraction, checkbox and form state, page linkage, figure and caption association, citations, and missing or duplicated content.

Distinguish native text extraction, OCR, document layout parsing, and multimodal reasoning. Preserve page and region provenance for every extracted claim.

### Video and audio

Define frame or clip sampling, temporal granularity, event boundaries, audio use, and coverage. Measure missed events, false events, sequence, timing, speaker or sound attribution, and evidence localization.

A sparse sample cannot establish that an event did not occur outside sampled regions.

## Evaluation and judging

A judge assignment requires:

- explicit acceptance criteria or rubric;
- allowed evidence and required citations;
- output schema with pass, fail, or inconclusive states;
- severity and blocking rules;
- calibration set with known outcomes;
- independence from the worker where material;
- tie, disagreement, abstention, and escalation policy.

Test position, order, verbosity, style, identity, and self-preference bias. Shuffle candidate order, hide irrelevant metadata, normalize formatting where appropriate, and include adversarially confident but incorrect outputs.

Do not use one model score as proof of quality. Combine deterministic metrics, calibrated model review, multiple independent judges, or qualified human review according to risk.

## Quality gates

| Tier | Minimum gate |
| --- | --- |
| Exploration | Approximate understanding with visible uncertainty |
| Concept draft | Useful structured findings for discussion; not authoritative |
| Working result | Required extraction, grounding, and task-compliance thresholds met |
| Production quality | Deterministic checks, calibrated independent review, provenance, and documented limitations |
| Exceptional quality | Additional specialist review, subgroup analysis, and deeper evidence coverage |

## Generated-media evaluation

For image, video, or audio candidates, evaluate both technical validity and assignment-specific quality:

- prompt and reference adherence;
- required and forbidden content;
- composition, consistency, identity, text, motion, timing, or audio quality;
- visible artifacts and protected regions;
- rights, consent, provenance, watermark, and disclosure requirements;
- edit effort and accepted-result cost.

The generator must not be the sole evaluator of its own output.

## Reliability and fallback

Report malformed output, missing evidence, unsupported claims, hallucinated text, skipped pages or frames, judge disagreement, and inconclusive cases separately.

Retry only transient or formatting failures likely to improve under the same assignment. Escalate repeated perception, grounding, coverage, bias, or capability failures to a different model, deterministic process, or human reviewer.

A fallback must pass the same modality, data, provenance, quality, and risk gates.

## Data and safety boundaries

Images, documents, recordings, and screenshots can expose personal, confidential, biometric, credential, health, financial, location, and bystander data. Record collection purpose, permitted routes, retention, region, access, transfer, and deletion.

Treat safety and policy classifiers as bounded components with measured false-positive and false-negative costs. Do not represent a model decision as legal, medical, security, or compliance approval unless the required qualified process actually occurred.

## Outcome metrics

Report:

- field, region, page, frame, or event coverage;
- precision, recall, error, and inconclusive rates by material subgroup;
- evidence-grounded claim rate;
- schema and deterministic-validator pass rates;
- first-pass and terminal acceptance;
- judge agreement, calibration, bias tests, and human overturn rate;
- latency, throughput, retries, correction effort, reviewer time, and cost per accepted result.

Preserve raw outputs and evidence references where privacy permits.

## Decision record

```text
Assignment, modality, quality tier, and risk:
Exact model, endpoint or artifact, runtime, hardware, and region:
Input formats, resolution, pages, frames, clips, audio, and sampling:
Prompt, schema, tools, evidence, and deterministic validators:
Rubric, judge independence, calibration, bias tests, and human coverage:
Accuracy, coverage, grounding, agreement, latency, effort, and cost outcomes:
Retry, stop, abstention, escalation, fallback, and degraded-operation rules:
Privacy, retention, provenance, limitations, verified date, and triggers:
```

## Related pages

- [AI Model Selection and Team Design](../..)
- [Generative Media](../generative-media/)
- [Speech and Conversation](../speech-and-conversation/)
- [Combined Workloads](../combined-workloads/)
- [Reliability Profiles](../reliability-profiles/)
- [Gemma 4](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/)
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../disclaimer/)

## Sources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 E2B Instruct](https://huggingface.co/google/gemma-4-E2B-it)
- [Gemma 4 E4B Instruct](https://huggingface.co/google/gemma-4-E4B-it)
