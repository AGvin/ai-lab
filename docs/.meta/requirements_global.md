# Global Documentation Requirements

These requirements apply to the entire documentation tree unless a more specific requirement explicitly overrides them.

## Search discoverability

Write documentation so that search engines can understand and index it effectively without reducing factual accuracy, readability, technical precision, or usefulness to readers. Use clear terminology, descriptive headings, and natural wording. Do not use keyword stuffing, repetitive phrasing, or content created primarily to manipulate search ranking.

## Localized external references

When an authoritative resource provides multiple localized versions, prefer the version that matches the locale of the generated document. For example, use an English (United States) resource for `en_US` and a Ukrainian resource for `uk_UA` when those official variants exist and are equivalent. When no matching official localization exists, use the closest authoritative version and do not substitute a lower-quality unofficial translation solely to match the locale.

## Incremental updates by default

Preserve existing valid documentation and update only the content affected by the requested change. Do not regenerate an entire document merely because a local section changed. Perform full-document regeneration only when it is explicitly required or when an incremental update cannot produce a coherent and correct result.

## Stable document structure

Preserve valid headings, anchors, links, ordering, and surrounding authored content whenever they are outside the requested scope. Avoid unnecessary rewrites and structural churn that create noisy diffs, break inbound references, or obscure the substantive change.

## Informative, non-clickbait headings

Use precise, descriptive headings that accurately represent the section or document content. Do not use sensational, manipulative, exaggerated, misleading, curiosity-gap, or tabloid-style wording designed primarily to attract clicks. Search optimization must never justify clickbait language or claims stronger than the supporting evidence.
