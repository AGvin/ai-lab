# Choosing Translation and Localization Models and Workflows

Select the least expensive validated model, service, deployment, or workflow that reaches the required quality tier for a defined language pair, direction, content type, privacy boundary, and budget.

## Translations

- English
- [Українська](./l10n/uk_UA/)

**Status:** Comparison structure updated on 2026-07-26. Language support, features, prices, terms, and model behavior change; verify the complete assignment before adoption.

## Quick picks

| Need | Start with | AI or model type | Scale | Route | Main reason |
| --- | --- | --- | --- | --- | --- |
| Compact private or offline draft route | [Phi-4 Mini Instruct](../../../../../../../software/sub/models/sub/microsoft/sub/phi/sub/phi-4/sub/mini-instruct/) | General-purpose multilingual instruct model | SLM | Local or self-hosted | Compact, multilingual, MIT-licensed candidate for constrained environments |
| Stronger local multilingual baseline | [Qwen3 8B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/8b/) | General-purpose multilingual reasoning and instruct model | SLM | Local or self-hosted | Open-weight baseline for private preprocessing, drafts, and terminology-aware experiments |
| High-volume conventional translation | DeepL API, Google Cloud Translation Advanced, or Azure AI Translator | Dedicated translation service | Not applicable | Hosted | Purpose-built language-pair, glossary, document, and batch features |
| Context-heavy or mixed-content translation | [GPT-5.6 Terra](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/terra/), [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/), or [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) | General-purpose language or multimodal model | LLM | Hosted | Document context, terminology reasoning, rewriting, review, and mixed-content handling |
| Production localization | Primary translation route plus deterministic validators and qualified bilingual review | Hybrid workflow | Mixed | Hosted, local, or hybrid | Structural checks, terminology control, escalation, and human approval are separable responsibilities |

These are starting routes, not universal rankings. Evaluate each language direction and content distribution separately.

## Economical SLM candidates

| Candidate | Model type | Scale | Architecture | Access | Best fit | Main limitation |
| --- | --- | --- | --- | --- | --- | --- |
| [Phi-4 Mini Instruct](../../../../../../../software/sub/models/sub/microsoft/sub/phi/sub/phi-4/sub/mini-instruct/) | General-purpose multilingual instruct model | SLM | Dense; 3.8B parameters | Open-weight; MIT | Compact local drafts, terminology-aware experiments, structured assistant workflows, and resource-constrained deployments | Not translation-specialized; quality, directionality, long-document behavior, and hardware fit require exact evaluation |
| [Qwen3 8B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/8b/) | General-purpose multilingual reasoning and instruct model | SLM | Dense; 8.2B total parameters | Open-weight; Apache-2.0 | Private preprocessing, summarization, draft translation, mixed technical content, and a stronger local baseline | Larger local cost than Phi-4 Mini; translation quality and accepted-result cost remain pair- and artifact-specific |

SLM is an economy-oriented filter, not proof of lower total cost. A smaller local model can lose its apparent saving through omissions, terminology errors, retries, slow inference, or bilingual correction effort.

Do not classify a quantized artifact as a separate smaller model. Quantization changes deployment characteristics, not the underlying model scale or translation evidence.

## Broader hosted routes

| Route | AI or model type | Best fit | Main limitation | Evidence to recheck |
| --- | --- | --- | --- | --- |
| DeepL API | Dedicated translation service | Supported language pairs, glossaries, document translation, and conventional production workflows | Pair, feature, region, document, retention, and pricing coverage vary | Exact API resource, supported languages, glossary/document behavior, terms, region, and current price |
| Google Cloud Translation Advanced | Dedicated translation service | Cloud-managed batch, glossary, document, and enterprise integration routes | Cloud configuration, region, data terms, and feature coverage require review | Exact edition, model/resource, region, glossary support, quotas, terms, and current price |
| Azure AI Translator | Dedicated translation service | Azure-centered enterprise translation, document, glossary, and workflow integration | Service configuration and supported features vary by operation and region | Exact resource, region, language pair, document support, terms, quotas, and current price |
| [GPT-5.6 Terra](../../../../../../../software/sub/models/sub/openai/sub/gpt/sub/gpt-5-6/sub/terra/) | General-purpose reasoning and language model | Context-heavy technical documents, terminology reasoning, rewriting, review, and mixed-content workflows | Hosted data path, mutable access and price, and need for structural validators | Exact endpoint, snapshot, region, context, data terms, price, and task evidence |
| [Claude Sonnet 5](../../../../../../../software/sub/models/sub/anthropic/sub/claude/sub/sonnet-5/) | General-purpose language and agentic model | Long documents, technical prose, review, rewriting, and instruction-heavy workflows | Hosted access, provider terms, and pair-specific quality require validation | Exact model, context, data terms, price, language direction, and reviewer evidence |
| [Gemini 3.6 Flash](../../../../../../../software/sub/models/sub/google/sub/gemini/sub/gemini-3-6-flash/) | Multimodal general-purpose model | Mixed text, image, PDF, audio, or document inputs and high-frequency hosted workflows | API behavior, supported operations, data terms, and output consistency change | Exact model alias, modalities, region, tools, data terms, price, and direction-specific evidence |

A dedicated translation service is not automatically better than a general model, and a general model is not automatically better because it handles more context. Compare the exact assignment, language direction, document structure, terminology, correction effort, and cost per accepted result.

## Workload view

| Workload | Prefer | Escalate or reject when |
| --- | --- | --- |
| Short general prose | Dedicated service or validated SLM route | Meaning, tone, directionality, or edit effort misses the required tier |
| Technical documentation | Terminology-controlled hosted model, dedicated service, or hybrid workflow | Protected literals, code, links, terminology, or document context are damaged |
| UI strings and resource files | Format-aware pipeline with dedicated or general model behind deterministic validators | Placeholders, plural branches, keys, escapes, or length constraints fail |
| High-volume batch translation | Lowest-cost route that passes a frozen representative suite | Retry, correction, latency, or review cost erases the unit-price advantage |
| Confidential or offline material | Validated local SLM or approved private deployment | Local quality cannot reach the required tier or hardware latency is unacceptable |
| High-risk legal, medical, financial, or public material | Approved route plus independent qualified bilingual review | Required expertise, accountability, or human approval is unavailable |
| Multimodal or mixed-content documents | Validated multimodal hosted route or staged extraction and translation workflow | Required modality, layout, extraction, data boundary, or rendering support is missing |

## Define the assignment

Record:

- exact downloadable artifact or API model, endpoint, region, and snapshot;
- runtime, hardware, quantization, prompts, parameters, tools, and permissions;
- source and target language, script, variant, and direction;
- domain, content type, document context, and input distribution;
- file format, parser or renderer, protected syntax, and translatability metadata;
- terminology database, glossary, style guide, and translation-memory versions;
- quality tier, risk, privacy, retention, residency, copyright, and permitted use;
- evaluation set, reviewers, evidence, limitations, and verification date.

Evaluate `A → B` and `B → A` separately. Do not transfer results across directions, languages, scripts, variants, domains, deployments, or quantizations without evidence.

## Acceptance gates

| Tier | Minimum gate |
| --- | --- |
| Exploration | Provisional output; manual review before reuse |
| Concept draft | Critical meaning and syntax preserved for discussion; not publishable |
| Working result | Required parsers pass and declared semantic, terminology, and format thresholds are met |
| Production quality | Validators and rendering checks pass plus required independent bilingual approval |
| Exceptional quality | Additional domain, style, accessibility, consistency, and editorial review |

Deterministic checks prove structural properties, not linguistic quality.

## Complete workflow

1. Reject candidates whose license, language pair, feature, format, or context support does not cover the work.
2. Reject routes that violate privacy, confidentiality, residency, or offline requirements.
3. Protect syntax and non-translatable regions.
4. Apply approved terminology and translation-memory policy.
5. Measure eligible candidates on a frozen representative suite.
6. Validate structure, rendering, semantics, terminology, and risk-specific requirements.
7. Compare correction, review, retry, escalation, latency, and total cost per accepted result.
8. Choose the least expensive assignment that consistently reaches the tier and define a separately validated fallback.

## Terminology and translation memory

Maintain approved, forbidden, and context-sensitive terms with domain, grammar, source, owner, and version. Test morphology and inflection rather than literal replacement alone.

Verify hosted glossary support for the exact pair, endpoint, and operation.

For translation memory, distinguish approved exact matches, fuzzy matches requiring review, unapproved machine output, stale or conflicting units, and matches whose surrounding context changes the correct target. Preserve provenance, reviewer, approval date, domain, product version, and supersession state.

Keep production memory separate from hidden evaluation references and prevent reference leakage into candidate runs.

## Software-localization integrity

Use format-aware parsers and validators for:

- named, positional, printf, and ICU placeholders;
- plural, gender, and select branches;
- HTML, XML, Markdown, links, images, code spans, and code fences;
- filenames, paths, commands, identifiers, API names, and configuration keys;
- escapes, accelerators, whitespace, newlines, and length limits;
- JSON, YAML, PO, resource bundles, XLIFF, schemas, and key sets;
- locale tags, directionality, numbers, dates, currencies, units, fonts, truncation, and rendering.

Use current CLDR locale data where applicable. Back translation, a second model, and the translating worker's own review are diagnostic signals, not proof.

## Language-pair evaluation

Stratify by pair, direction, script, variant, domain, content type, risk, context, ambiguity, historical failures, format, glossary state, memory state, and locale-specific behavior.

Freeze references, prompts, tools, thresholds, exclusions, and reviewer instructions before execution. Use an independent bilingual reviewer for material linguistic judgments.

### Ukrainian slice

Evaluate English-to-Ukrainian and Ukrainian-to-English separately. Test terminology, official names, omissions, additions, inflection, case, gender, agreement, plural behavior, register, address forms, word order, euphony, punctuation, typography, idiomatic phrasing, transliteration policy, and protected technical identifiers.

Use the current official Ukrainian Orthography and require a proficient native Ukrainian reviewer before a production-quality claim.

## Outcome metrics

Report eligible segment and document populations plus:

- semantic acceptance and critical-error rate;
- omission and unsupported-addition rate;
- approved-term accuracy and forbidden-term occurrences;
- placeholder, markup, parser, schema, key-set, and rendering pass rates;
- first-pass, corrected, escalated, and terminal acceptance;
- consistency, edit effort, reviewer time, latency, and cost per accepted result.

Use an explicit human error taxonomy such as a tailored MQM-style rubric. Automatic metrics and model judges may screen candidates only after calibration for the exact pair, direction, domain, and error cost.

## Decision record

```text
Assignment and version:
Languages, scripts, variants, and direction:
Domain, content, context, format, and protected syntax:
Quality tier and risk:
Model, endpoint, region, artifact, runtime, and hardware:
Terminology, glossary, style guide, and translation memory:
Privacy, retention, residency, license, and permitted use:
Evaluation set, validators, reviewer, rubric, and coverage:
Quality, structural, latency, effort, and cost outcomes:
Retry, stop, escalation, fallback, evidence, and verified date:
```

## Related pages

- [AI Model Selection and Team Design](../..)
- [Coding](../coding/)
- [Combined Workloads](../combined-workloads/)
- [Reliability Profiles](../reliability-profiles/)
- [Models](../../../../../../../software/sub/models/)
- [Benchmarks](../../../../../benchmarks/)
- [General repository disclaimer](../../../../../../../disclaimer/)

## Sources

- [Unicode CLDR](https://cldr.unicode.org/)
- [XLIFF 2.2](https://docs.oasis-open.org/xliff/xliff-core/v2.2/cs01/xliff-core-v2.2-cs01-part1.html)
- [W3C ITS 2.0](https://www.w3.org/TR/its20/)
- [MQM](https://themqm.org/)
- [DeepL supported languages](https://developers.deepl.com/docs/getting-started/supported-languages)
- [Google Cloud Translation](https://cloud.google.com/translate/docs)
- [Azure AI Translator](https://learn.microsoft.com/azure/ai-services/translator/)
- [Official Ukrainian Orthography](https://ulif.mon.gov.ua/system/files/pravopus-new.pdf)
