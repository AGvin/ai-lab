# Choosing Translation and Localization Models and Workflows

Select an exact model, service, deployment, or smallest practical workflow for a defined language pair, direction, content type, quality tier, privacy boundary, and budget.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Guidance verified on 2026-07-25. Language support, features, prices, terms, and model behavior change; verify the complete assignment before adoption.

## Define the assignment

Separate general prose, technical documentation, software resources, UI strings, structured documents, high-volume batch work, high-risk material, and multilingual review.

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

## Candidate routes

- **Dedicated hosted translation:** evaluate exact DeepL API, Google Cloud Translation Advanced, or Azure AI Translator resources when current pair, glossary, document, batch, region, retention, and pricing support match.
- **General hosted models:** evaluate exact GPT-5.6, Claude Sonnet 5, Gemini 3.6 Flash, or another model when document context, terminology reasoning, rewriting, review, or mixed-content handling is required.
- **Local models:** evaluate exact Qwen3 or other downloadable artifacts when offline operation, privacy, or provider independence matters; name artifact, quantization, runtime, context, hardware, and language direction.
- **Hybrid workflow:** deterministic preprocessing and memory retrieval, one primary route, deterministic checks, independently validated review for failures, and qualified human approval at required coverage.

Retry only transient failures likely to improve under the same assignment. Escalate repeated semantic, terminology, pair, context, or capability failures to a different assignment. A fallback must pass the same data, format, quality, and risk gates.

Do not describe output as certified, professionally translated, or human-reviewed unless that process occurred and evidence is retained.

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
