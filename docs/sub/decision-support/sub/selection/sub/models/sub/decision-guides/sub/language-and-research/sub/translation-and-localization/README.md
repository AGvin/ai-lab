# Translation and Localization Model Selection

Choose models for translation and localization by the exact language pair and direction, content type, terminology, structural constraints, privacy boundary, quality tier, and correction cost.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Scope

This page owns model-specific translation/localization selection. Dedicated translation services, complete localization platforms, parsers, rendering tools, and broader workflow choices remain outside model selection even when they participate in the final solution.

Evaluate each direction separately. Do not transfer results across languages, scripts, regional variants, domains, model versions, artifacts, quantizations, or deployment routes without evidence.

## Assignment definition

Record the exact model/version/artifact together with source and target language, direction, domain, content type, document context, protected syntax, output format, terminology/glossary/style-guide version, privacy constraints, quality tier, evaluation set, and verification date.

Measure semantic acceptance, critical errors, omissions, unsupported additions, terminology accuracy, structural-validator pass rates, consistency, edit effort, reviewer time, latency, retries, and cost per accepted result.

## Candidate evaluation set

These candidates preserve useful **model** hypotheses from the legacy mixed translation/model/service guide after current first-party identity/capability revalidation. They are not a language-pair ranking, and the dedicated translation services from the legacy page are intentionally outside this model-only subtree.

| Candidate | Evaluate for | Evidence state | Main boundary |
| --- | --- | --- | --- |
| [Gemma 4 E2B Instruct](../../../../../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e2b-instruct/) | Lowest-footprint private/local multimodal draft experiments involving text plus image/document or bounded short-audio context | Provider-documented multilingual multimodal model; legacy AI Lab candidate hypothesis | Compact size and modality support do not establish translation quality; evaluate each direction, terminology set, document type, and exact runtime separately |
| [Phi-4 Mini Instruct](../../../../../../../reference/sub/producers/sub/microsoft/sub/phi/sub/phi-4/sub/models/sub/phi-4-mini-instruct/) | Compact multilingual text-first draft and terminology-aware experiments under constrained local resources | Provider-documented multilingual text/coding model including Ukrainian; legacy AI Lab candidate hypothesis | Not translation-specialized; tool/function-calling availability is surface/runtime-dependent and irrelevant unless the assignment actually requires it |
| [Gemma 4 E4B Instruct](../../../../../../../reference/sub/producers/sub/google/sub/gemma/sub/gemma-4/sub/models/sub/e4b-instruct/) | Stronger compact local mixed-content translation experiments where image, document, UI, or short-audio context may matter | Provider-documented multilingual multimodal model; legacy AI Lab candidate hypothesis | Stored/runtime footprint exceeds the effective-parameter label and pair-specific quality remains unverified |
| [Qwen3 8B](../../../../../../../reference/sub/producers/sub/alibaba/sub/qwen/sub/qwen3/sub/models/sub/qwen3-8b/) | Reproducible text-first local baseline for private preprocessing, draft translation, summarization, and technical-content experiments | Provider-documented multilingual instruction model; legacy AI Lab candidate hypothesis | More local capacity does not prove better translation or lower accepted-result cost; exact artifact/direction must be measured |
| [GPT-5.6 Terra](../../../../../../../reference/sub/producers/sub/openai/sub/gpt/sub/gpt-5-6/sub/models/sub/terra/) | Hosted context-heavy technical documents, terminology reasoning, rewriting, or review when a general reasoning model is appropriate | Current provider positioning for balanced professional reasoning/language work; AI Lab pair-specific quality unverified here | Hosted data path and mutable service properties must be rechecked; use bilingual evaluation rather than provider positioning to determine quality |
| [Claude Sonnet 5](../../../../../../../reference/sub/producers/sub/anthropic/sub/claude/sub/sonnet/sub/models/sub/sonnet-5/) | Long technical documents, instruction-heavy rewriting/review, and context-rich multilingual workflows | Current provider-documented knowledge-work/reasoning strengths; AI Lab pair-specific quality unverified here | Provider claims and long context do not establish terminology fidelity or direction-specific translation quality |
| [Gemini 3.6 Flash](../../../../../../../reference/sub/producers/sub/google/sub/gemini/sub/models/sub/gemini-3-6-flash/) | Hosted mixed text/image/PDF/audio inputs and high-frequency multimodal translation or localization experiments | Current provider-documented multimodal and long-context capabilities; AI Lab pair-specific quality unverified here | Exact input surface, data terms, output consistency, and direction-specific linguistic quality require current evaluation |

Candidate membership means only that the model is worth a bounded experiment for the stated hypothesis. Recheck current hosted availability, model IDs/aliases, modalities, limits, and prices when they materially affect the decision; do not preserve those mutable values as a durable rank.

## Localization integrity

For software-localization tasks, deterministic validation should cover applicable placeholders, plural/select branches, markup, links, code spans, identifiers, escapes, resource keys, schemas, locale tags, numbers/dates/currencies, directionality, length constraints, and rendering. Deterministic checks establish structural properties, not linguistic quality.

Production-quality linguistic claims require independent qualified bilingual review appropriate to the language pair and domain. Back translation or another model's agreement is supporting evidence, not proof.

## Acceptance tiers

Use explicit gates from exploratory output through concept draft, working result, production quality, and exceptional quality. The least expensive model is acceptable only when it consistently reaches the required gate after correction and review costs are included.

Link intrinsic model facts from [Model Reference](../../../../../../../reference/).
