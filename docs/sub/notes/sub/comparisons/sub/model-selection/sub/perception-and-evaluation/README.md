# Choosing Perception and Evaluation Models and Workflows

Select an exact model, service, deployment, or smallest practical workflow for image, screenshot, document, video, audio, multimodal understanding, and output evaluation.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Guidance verified on 2026-07-25. Accepted media, resolution handling, context, endpoints, prices, licenses, regional availability, and evaluator behavior change; verify the complete assignment before adoption.

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

## Candidate routes

### Hosted multimodal models

Evaluate exact [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/), [GPT-5.6](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/), [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/), or another approved model when their current modality, context, file, region, retention, and tool support matches the assignment.

Hosted breadth does not prove OCR precision, temporal coverage, judge calibration, or data eligibility.

### Local models and tools

Use local OCR, document parsers, computer-vision models, audio tools, or downloadable multimodal models when offline operation, privacy, latency, or reproducibility matters. Name every exact artifact, runtime, precision, resolution, sampling rule, and hardware profile.

### Hybrid workflow

A practical route often uses deterministic extraction and validation first, a multimodal model for interpretation, and an independent reviewer or human for disputed or high-impact decisions.

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
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../disclaimer/)
