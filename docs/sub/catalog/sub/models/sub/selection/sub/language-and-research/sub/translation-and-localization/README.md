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

## Localization integrity

For software-localization tasks, deterministic validation should cover applicable placeholders, plural/select branches, markup, links, code spans, identifiers, escapes, resource keys, schemas, locale tags, numbers/dates/currencies, directionality, length constraints, and rendering. Deterministic checks establish structural properties, not linguistic quality.

Production-quality linguistic claims require independent qualified bilingual review appropriate to the language pair and domain. Back translation or another model's agreement is supporting evidence, not proof.

## Acceptance tiers

Use explicit gates from exploratory output through concept draft, working result, production quality, and exceptional quality. The least expensive model is acceptable only when it consistently reaches the required gate after correction and review costs are included.

Link intrinsic model facts from [Model Reference](../../../../../reference/).
