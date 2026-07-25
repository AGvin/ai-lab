# Choosing Translation and Localization Models and Workflows

Use this guide to select an exact model, service, deployment, or smallest practical workflow for a defined language pair, direction, content type, quality tier, privacy boundary, and budget.

## Translations

- English

## Status

Initial canonical guidance verified on 2026-07-25. Language support, product features, pricing, provider terms, and model behavior change; verify the complete assignment before adoption.

## Define the workload first

Translation conveys content from a source language into a target language. Localization includes translation but also adapts terminology, product conventions, formats, UI constraints, and locale-specific behavior. A capable prose translator is therefore not automatically a complete localization system.

Separate the work into the actual content classes:

- general prose, with the intended audience, register, and document context;
- technical documentation, including established terminology, code, commands, links, and markup;
- software localization and resource bundles with protected syntax;
- UI strings with screen context, character or pixel limits, and interaction state;
- structured documents and markup whose syntax and non-translatable regions must survive;
- high-volume batch translation, including throughput, quota, retry, and unit-cost constraints;
- legal, medical, safety, financial, contractual, immigration, certified, or other high-risk material requiring qualified human control;
- multilingual review and quality evaluation, which may be a separate assignment from translation.

Do not choose from a general model leaderboard or assume one universally best translator. Source and target direction, domain, format, context, deployment, glossary support, and review regime can change the result materially.

## Freeze the assignment unit

Treat a recommendation as a claim about one complete assignment, not a model family. Record:

- exact downloadable artifact and revision, or exact API service, selected model, endpoint, region, and snapshot when exposed;
- provider, runtime, hardware, weight format, quantization, prompts, parameters, tools, permissions, and decoding settings;
- source and target language, script, region or variant, and direction;
- domain, content type, input distribution, segment context, and document context;
- file format, protected syntax, translatability metadata, and parser or renderer versions;
- approved, forbidden, and context-sensitive terms; style guide and terminology-database versions;
- translation-memory version, match policy, provenance rules, and approval state;
- required quality tier and risk classification;
- privacy, confidentiality, retention, residency, copyright, and permitted-use boundaries;
- evaluation-set version, reviewers and their independence, evidence, limitations, and verification date.

Create a separate assignment when any material field changes. Evaluate `A → B` and `B → A` independently. Do not transfer results between directions, neighboring languages, scripts, regional variants, domains, hosted and local deployments, or different quantizations without evidence.

## Set task-specific acceptance gates

Use the repository's five [quality tiers](../combined-workloads/#quality-tiers) rather than inventing a parallel scale. Translate the selected tier into observable gates for this workload.

| Tier | Translation and localization gate |
| --- | --- |
| Exploration | Meaning and terminology may be provisional; label the output as unapproved and require manual review before reuse |
| Concept draft | Preserve critical meaning and protected syntax well enough for stakeholder review; do not publish or merge the result |
| Working result | Pass required parsers and deterministic checks, meet the declared semantic and terminology threshold, and disclose known limitations |
| Production quality | Pass all format and rendering checks, meet pre-registered linguistic thresholds, and receive the required independent bilingual or specialist approval |
| Exceptional quality | Add stricter domain, style, consistency, accessibility, rendering, and editorial review where the extra quality has demonstrated value |

For every tier, state whether deterministic validation alone, sampled human review, or full human review is allowed. Deterministic checks can prove structural properties but cannot approve material linguistic judgments.

## Select the smallest complete workflow

Start with constraints that can eliminate candidates:

1. Reject assignments whose license, permitted use, pair, feature, format, or context support does not cover the workload.
2. Reject routes that violate privacy, confidentiality, residency, or offline requirements.
3. Protect or extract syntax and non-translatable content before translation where the format permits it.
4. Measure eligible candidates on a frozen representative suite.
5. Compare total cost and latency per accepted result, including validation, correction, review, retry, and escalation.
6. Choose the least expensive assignment that consistently reaches the tier, then define a separately validated fallback.

A translation engine alone may not be the smallest complete system. Translation memory, terminology control, local parsing, deterministic validation, and qualified review can reduce both failure cost and model cost.

## Terminology, glossary, and translation memory

### Terminology controls

Define approved, forbidden, and context-sensitive terminology with domain, part of speech, source, owner, and effective version. Test morphology and inflection: literal replacement is insufficient when a target term must change case, gender, number, agreement, or grammatical form.

For hosted glossary features, dynamically verify availability for the exact source-target pair and requested API resource. Record unsupported terms and the fallback policy. Never describe glossary support at provider level when the selected pair or operation does not support it.

### Translation memory

Distinguish:

- exact matches that have the same source, relevant metadata, and approved target;
- fuzzy matches that require review under a declared similarity and context policy;
- machine-translated or unapproved entries that must not inherit approved status;
- conflicting memories, stale units, segmentation changes, and misaligned pairs;
- matches whose surrounding document, product state, or grammatical context changes the correct target.

Version the memory and preserve source, target, locale, provenance, reviewer, approval date, domain, product version, and supersession state. Do not replace a previously approved unit with model output without human approval. Protect confidential memories, glossaries, and terminology databases from providers or fallbacks not approved for that data.

Keep production memory separate from evaluation references. Freeze test references before candidate runs, restrict access by the translating assignment, and record any overlap so memory retrieval cannot leak answers into the evaluation.

## Validate software-localization integrity

Run deterministic format checks before model or human review wherever possible. Use parsers and format-aware validators rather than regular expressions alone.

### Protected syntax

Inventory and validate:

- named, positional, printf-style, and ICU-style placeholders;
- plural, gender, and select variants, including every target-locale branch;
- HTML and XML tags, nesting, attributes, entities, and translatable boundaries;
- Markdown links and destinations, images, code spans, code fences, and headings;
- filenames, paths, shell commands, identifiers, API names, configuration keys, and non-translatable tokens;
- escapes, accelerator keys, significant whitespace and newlines, and character or pixel limits.

The [Unicode CLDR plural rules](https://cldr.unicode.org/index/cldr-spec/plural-rules) show why locale behavior cannot be reduced to an English singular/plural assumption. Exercise the categories and minimal pairs required by the target locale using current CLDR data or compatible tooling.

### Files and interchange formats

Require:

- JSON, YAML, PO, and resource-bundle parse success with schema or key-set checks where available;
- source-target key completeness and detection of unexpected added or removed units;
- XLIFF or equivalent interchange validation against the exact format version and supported modules;
- locale-tag, script, and directionality checks;
- target-locale number, date, time, currency, measurement, and unit-format checks;
- rendering, truncation, bidirectional-text, font, and pseudo-localization tests in representative screens.

[XLIFF 2.2 Committee Specification 01](https://docs.oasis-open.org/xliff/xliff-core/v2.2/cs01/xliff-core-v2.2-cs01-part1.html) is a structured localization interchange work product with a core and extended material, including optional modules for translation candidates and plural, gender, and select information. It is a committee specification, not a final OASIS Standard. Record the exact XLIFF version, approval stage, and implementation support rather than assuming every tool implements every module.

The [W3C Internationalization Tag Set 2.0](https://www.w3.org/TR/its20/) defines data categories relevant to localization workflows, including translatability, terminology, domain, directionality, localization notes, provenance, and quality information. Preserve equivalent metadata when it is present; this guidance does not require every project to adopt ITS.

Back translation, a second model's opinion, and the translating worker's self-report are diagnostic signals, not proof that meaning or structure is correct.

## Evaluate each language pair and direction

Build a versioned suite stratified by:

- language pair, script, region or variant, and direction;
- domain, content type, risk, and required quality tier;
- short segments, related multi-segment context, and full-document context;
- ordinary, ambiguous, noisy, adversarial, and historical-failure inputs;
- prose, technical documentation, UI, markup, and structured-resource formats;
- no match, fuzzy match, exact approved match, stale match, and conflicting glossary or memory state;
- locale-specific plural, gender, select, number, date, unit, directionality, and rendering behavior.

Freeze selection rules, references, prompts, tools, thresholds, exclusions, and reviewer instructions before execution. Prevent the worker from accessing hidden references. Use an independent bilingual reviewer for material linguistic judgments; a model must not be its sole production approver.

### Ukrainian evaluation slice

Evaluate English-to-Ukrainian and Ukrainian-to-English as separate assignments. For both directions, test:

- domain terminology and consistent treatment of official names;
- preserved meaning, with omissions, additions, and unsupported interpretation recorded separately;
- inflection, case, gender, agreement, plural behavior, and grammatical government;
- register, forms of address, natural word order, euphony, punctuation, typography, and idiomatic phrasing;
- transliteration only when the product or an authoritative rule requires it;
- preservation of technical identifiers and established technical terms.

Use the current [official Ukrainian Orthography](https://ulif.mon.gov.ua/system/files/pravopus-new.pdf) as an authoritative language reference. Require a proficient native Ukrainian reviewer before making a production-quality claim. Ukrainian results do not establish performance for another Slavic language, script, regional variant, direction, or domain.

## Report measurable outcomes

Pre-register the unit of analysis. An **eligible segment** is one scheduled source segment evaluated under the frozen assignment; an **eligible document** is one scheduled document evaluated end to end under those conditions. Exclude only invalid evaluation events outside the assignment, such as a corrupted fixture or harness failure. Report every exclusion and reason separately by segment and document. Provider failures, rejected output, blocked cases, and no-output cases remain eligible when they are part of the assignment or deployed conditions. Do not silently replace a failed case with a successful rerun.

Use separate segment and document populations wherever both are material. At minimum, report these formulas:

| Outcome | Numerator / denominator |
| --- | --- |
| Semantic acceptance | Eligible reviewed segments or documents meeting every pre-registered semantic gate / all eligible segments or documents in the declared review population; also report unreviewed eligible units |
| Critical-error rate | Eligible reviewed segments or documents containing at least one critical error / all eligible segments or documents in the same declared review population |
| Omission rate | Eligible reviewed segments or documents with at least one omitted required meaning unit / all eligible reviewed segments or documents that require translated content |
| Unsupported-addition rate | Eligible reviewed segments or documents with at least one unsupported addition / all eligible reviewed segments or documents that require translated content |
| Terminology accuracy | Correctly rendered applicable approved-term occurrences / all applicable approved-term occurrences in eligible reviewed source units; report forbidden-term occurrences / all eligible reviewed target units separately |
| Protected-syntax preservation | Protected placeholders, tags, links, identifiers, or other tokens preserved exactly under the format policy / all applicable protected tokens in eligible units; also report eligible units with every protected token correct / all eligible units containing protected tokens |
| Parser, schema, key-set, and render pass | Eligible files or documents passing the named validator / all eligible files or documents scheduled for that validator, separately for each validator |
| First-pass acceptance | Eligible segments or documents accepted without correction or escalation / all eligible segments or documents |
| Acceptance after correction | Eligible segments or documents accepted by a permitted same-assignment correction before escalation / all eligible first-pass failures for which policy permitted correction; also report terminal acceptance / all eligible segments or documents |
| Human-review and escalation rate | Eligible segments or documents receiving human review / all eligible segments or documents, split into full and sampled review; eligible units escalated / all eligible units |
| Consistency | Eligible repeated-case groups meeting the pre-registered semantic and structural consistency rule / all eligible repeated-case groups with the required repeat count; report groups made inconclusive by exclusions separately |
| Edit effort and reviewer time | Total measured edits or review time / accepted eligible segments or documents; include reviewed rejected units in the total effort numerator |
| Latency | End-to-end time from assignment start to terminal disposition for each eligible segment or document, including queue, correction, validation, review, and escalation; report accepted, rejected, blocked, abandoned, and no-output groups separately, with percentiles when the sample permits |
| Cost per accepted result | Total measured model, service, infrastructure, validation, correction, and review cost across all eligible attempts / accepted terminal segments or documents; also report eligible rejected and abandoned counts |

Use an MQM-style taxonomy and severity model or an equivalently explicit human rubric. [MQM](https://themqm.org/) is an analytic translation-quality-evaluation framework; tailor error types, severity, scoring, sampling, and thresholds to the translation specifications, and do not compare scores from differently configured evaluations as if they were the same measure.

BLEU, chrF, COMET, embeddings, or model judges may screen candidates and detect regressions only after calibration for this exact pair, direction, domain, and error cost. One automatic or judge score is not sufficient proof of production quality. WMT25's [automated translation evaluation shared-task findings](https://www2.statmt.org/wmt25/pdf/2025.wmt-1.23.pdf) provide current evidence for caution across linguistically diverse settings and for retaining reference-based evaluation; they do not establish a universal metric or repository ranking.

### Review regime by tier and risk

| Assignment | Minimum review rule |
| --- | --- |
| Exploration or concept draft | Deterministic checks plus review by the consumer before any consequential use |
| Working result, low-risk structured content | All deterministic checks and bilingual sampled review only when a validated sampling plan meets the declared error threshold |
| Production prose or user-facing localization | All deterministic checks and independent bilingual review at the coverage established by pair- and domain-specific evidence |
| High-risk, certified, or legally consequential content | Full review and approval by a qualified human appropriate to the jurisdiction and use; add specialist or certification controls where required |
| Deterministic-only acceptance | Limit to properties a validator can prove, such as parseability or placeholder identity; never treat it as linguistic approval |

Record reviewer identity or qualification, independence, instructions, disagreements, adjudication, and coverage. Reusing the translating model for correction is not independent review.

## Candidate assignments

These candidates are starting points for evaluation, not quality rankings. Product facts below were rechecked against primary sources on 2026-07-25; query current support and terms before deployment.

### DeepL API

**Candidate role:** Hosted dedicated-translation service for supported language pairs, resources, and features.

DeepL's [Languages API documentation](https://developers.deepl.com/docs/languages/using-the-languages-api) says `/v3/languages` reports language support by resource and optional capabilities. Its [supported-languages guidance](https://developers.deepl.com/docs/getting-started/supported-languages) directs integrations to query current support instead of hardcoding assumptions.

Before evaluation:

- query source and target support for the exact operation;
- verify source and target support for glossary and tag handling, and target-language support for formality and style rules, as required by the selected resource;
- record API endpoint, resource, language identifiers, availability status, and relevant parameters;
- record privacy, retention, residency, provider terms, rate limits, and price assumptions with their verification date;
- validate formatting and linguistic quality independently.

Do not infer that a feature exists for a pair because it exists elsewhere, or claim universal quality superiority.

### Google Cloud Translation - Advanced

**Candidate role:** Hosted service for supported text, batch, formatted-document, glossary, and customization workflows.

Google's current documentation covers [Document Translation](https://docs.cloud.google.com/translate/docs/advanced/translate-documents), [glossaries](https://docs.cloud.google.com/translate/docs/advanced/glossary), [adaptive translation](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation), and [language support](https://docs.cloud.google.com/translate/docs/languages). Document Translation attempts to preserve formatting for supported formats, while the documentation identifies limitations for cases such as scanned or complex PDFs and text boxes in some formats.

Before evaluation:

- name the exact selected model type, API operation, endpoint, project, location, and region;
- verify current pair, model, glossary, adaptive or custom, batch, and document-format support;
- record IAM, service-account permissions, Cloud Storage use, retention, residency, and data boundary;
- exercise stated size, page, layout, scan, text-box, and format limitations with representative documents;
- record quotas, rate limits, availability, price assumptions, and verification date.

Do not collapse managed NMT, Translation LLM, adaptive, or custom choices into one unnamed Google candidate, and do not claim a universal quality ranking.

### Meta NLLB-200 distilled 600M

**Candidate role:** Self-hosted research baseline for single-sentence, general-domain experiments and broad language coverage, including Ukrainian.

Bind experiments to `facebook/nllb-200-distilled-600M` at an exact revision. The exact [model-card revision used for this guide](https://huggingface.co/facebook/nllb-200-distilled-600M/blob/795a75074dfac69afd44712e16991627e7daf020/README.md):

- uses the `CC-BY-NC-4.0` license and lists Ukrainian as `ukr_Cyrl`;
- frames the artifact primarily for machine-translation research and single-sentence translation;
- says it is not released for production deployment;
- does not intend document translation, certified translation, or domain-specific medical or legal use;
- notes general-domain scope, possible mistranslation, and that training inputs did not exceed 512 tokens, with possible degradation on longer sequences.

Treat it as an experimental research baseline only. Do not recommend it for production, commercial, certified, document, or domain-specific high-risk translation without contrary current evidence, pair-specific evaluation, and an independent license and permitted-use review.

### General-purpose instruction-following models

**Candidate role:** Context-heavy, style-aware, explanation, terminology, adaptation, or review tasks for which flexible instructions add measurable value.

Evaluate the exact model or snapshot together with its provider or local artifact, system and user prompts, examples, context assembly, tools, decoding settings, runtime, and permissions. Test pair-specific semantic and format behavior across repeated runs.

These models may help when a service cannot express document context, audience, tone, conflicting terminology, or a structured review task. Their formatting flexibility does not replace parsers, placeholder checks, rendering, or independent bilingual approval. Do not rank a provider or model without reproducible evidence for the exact pair, direction, domain, scaffold, and tier.

## Choose local, hosted, or hybrid deployment

| Dimension | Local | Hosted | Hybrid |
| --- | --- | --- | --- |
| Privacy and residency | Can keep approved data offline; still requires local access, logging, and memory controls | Must satisfy provider processing, retention, region, and transfer terms | Classify and route data explicitly; sanitized traffic must not imply permission to send protected memories |
| License and use | Verify exact artifact, weights, dependencies, and permitted use | Verify service terms and acceptable-use constraints | Both paths must be permitted independently |
| Pair and features | Verify artifact codes, direction, glossary or TM integration, and actual quality | Query current pair, operation, region, and feature support | Define which features are lost on fallback |
| Operations | Measure hardware, RAM or VRAM, context, batching, throughput, cold start, and offline availability | Measure model visibility, availability, rate limits, quotas, latency, and provider version changes | Measure routing, redaction, transfer, duplicate work, and failure of either path |
| Cost | Include hardware occupancy, runtime, maintenance, review, and energy | Include requests, documents, storage, network, retries, and review | Include both stacks and routing overhead |
| Fallback | Validate a smaller artifact, CPU path, queue, or fail-closed state separately | Validate alternate endpoint, region, provider, queue, or human path separately | Test combined outages and re-entry to the primary route |

Compare total cost per accepted segment or document, not nominal token price or raw throughput. Record whether batching changes context, latency, ordering, or quality.

## Prefer a hybrid workflow when it reduces risk or cost

A bounded hybrid workflow can:

1. parse files locally, classify sensitivity, extract protected tokens, and reject malformed input;
2. retrieve only approved terminology and translation-memory units;
3. redact or minimize data and send only eligible content to the selected service or model;
4. restore protected syntax and run parsers, schema, key-set, terminology, and rendering checks;
5. route failed, ambiguous, novel, or high-risk cases to an independent bilingual reviewer;
6. approve new or changed memory units only after human review.

Do not hide a lower-quality or differently governed fallback behind the primary assignment's quality claim. Each route needs its own evaluation and data boundary.

## Reliability, retry, and fallback

Give every production assignment a [reliability profile](../reliability-profiles/) that binds the complete deployment and evidence.

Define:

- a bounded correction budget for repairable output defects;
- bounded backoff and an idempotency rule for transient service failures;
- stop conditions for repeated failure signatures, unsupported pairs, failed syntax, and exhausted budgets;
- escalation to a validated stronger assignment, deterministic process, qualified reviewer, or fail-closed queue;
- a separately tested degraded-operation profile for local hardware loss, provider outage, quota exhaustion, or network failure;
- recovery and return-to-primary criteria.

A low-confidence or unsupported pair must fail closed or escalate rather than fabricate. Never keep retrying the same assignment after evidence shows a capability gap.

## Safe-use boundaries

- Legal, medical, safety, financial, contractual, immigration, certified, and similarly consequential translations require qualified human control appropriate to the jurisdiction and use.
- Check privacy, confidentiality, copyright, provider terms, and residency before sending content, translation memories, glossaries, or reviewer notes to a hosted service.
- Minimize or redact personal data, secrets, credentials, and unnecessary context where appropriate, then verify that redaction did not remove needed meaning.
- Do not silently add, remove, weaken, or strengthen warnings, permissions, obligations, contraindications, deadlines, or safety instructions.
- Preserve approval and access boundaries; a provider substitution is a new data and quality decision.
- Do not represent generated output as certified, professionally translated, or human-reviewed unless the required process actually occurred and evidence is retained.

## Compact decision record

Use this record or equivalent structured data:

```text
Assignment ID:
Source and target language, script, variant, and direction:
Domain, content types, context, and input distribution:
Format and protected syntax:
Quality tier and risk:
Model, service, endpoint, region, artifact, and revision:
Runtime, hardware, quantization, prompts, parameters, and tools:
Glossary, terminology database, style guide, and translation memory:
Privacy, retention, residency, license, and permitted use:
Evaluation set, references, eligibility, and exclusions:
Deterministic validators and rendering checks:
Reviewer, independence, rubric, and coverage:
Semantic, critical-error, omission, addition, and terminology outcomes:
Placeholder, markup, parser, and render outcomes:
First-pass, correction, escalation, consistency, latency, and cost outcomes:
Retry, stop, escalation, degraded-operation, and fallback rules:
Evidence provenance and limitations:
Verified date and re-evaluation triggers:
```

The selection process, gates, workflow design, and record fields in this page are repository-authored operational guidance. They organize established localization and evaluation practices and make no claim of novelty.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Choosing Models for Coding](../coding/)
- [Choosing Model Portfolios for Combined Workloads](../combined-workloads/)
- [Defining Model Reliability Profiles](../reliability-profiles/)
- [Models](../../../../../../../software/sub/models/)
- [Benchmarks](../../../../../benchmarks/)
- [Disclaimer](../../../../../../../disclaimer/)
