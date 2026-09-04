# Global Documentation Requirements

These requirements apply to the entire documentation tree unless a more specific requirement explicitly overrides them.

## Search discoverability

Write documentation so that search engines can understand and index it effectively without reducing factual accuracy, readability, technical precision, or usefulness to readers. Use clear terminology, descriptive headings, and natural wording. Do not use keyword stuffing, repetitive phrasing, or content created primarily to manipulate search ranking.

## Localized external references

When an authoritative resource provides multiple localized versions, prefer the version that matches the locale of the generated document. For example, use an English (United States) resource for `en_US` and a Ukrainian resource for `uk_UA` when those official variants exist and are equivalent. When no matching official localization exists, use the closest authoritative version and do not substitute a lower-quality unofficial translation solely to match the locale.

## Adaptive render scope

When updating an existing rendered document, analyze the current document against the current canonical inputs and determine what is already valid, what is stale or missing, and what reader-facing scope is actually affected.

By default, make the smallest coherent semantic change that produces a correct, coherent, well-formed complete document. Preserve valid unaffected content. Expand the scope from an item or block to a section, several dependent sections, or the whole document whenever canonical changes, dependencies, structure, or document quality require it.

A full-document scope does not by itself require rewriting every valid sentence. However, the repository owner may explicitly request a full-document refresh; in that case ordinary renderer-authored wording and structure may be regenerated without the default preservation preference, while canonical authored content and all current requirements and rendering constraints remain authoritative.

## Stable document structure

Preserve valid headings, anchors, links, ordering, and surrounding renderer-authored content when they remain outside the coherent affected scope. Broaden or rebuild structure when required for correctness, coherence, or an explicit full-document refresh. Avoid unnecessary structural churn that creates noisy diffs, breaks inbound references, or obscures the substantive change.

## Informative, non-clickbait writing

Write headings, summaries, and introductory text so they accurately represent the document or section content. Avoid sensational, manipulative, exaggerated, misleading, curiosity-gap, or tabloid-style wording intended primarily to attract attention or increase click-through rates. Search optimization must never take precedence over factual accuracy, technical precision, evidence strength, or reader trust. Do not make claims stronger than the supporting evidence.
