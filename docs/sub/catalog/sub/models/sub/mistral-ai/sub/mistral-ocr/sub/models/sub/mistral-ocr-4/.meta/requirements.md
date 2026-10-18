# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Mistral OCR 4 as the June 2026 focused document-intelligence/OCR model release.
- Preserve first-party facts such as structured document outputs, language coverage, self-hostability, and confidence/bounding-box features only at this release scope.
- Treat benchmark comparisons, throughput, price, deployment packaging, and API availability as freshness-sensitive.

## Validation

- Membership resolves to Mistral OCR.

## Source-backed profile

- Required reader orientation: Mistral OCR 4 is the OCR 4.0 document-extraction release introduced on June 23, 2026.
- Preserve this model-scoped fact: The exact hosted identifier is `mistral-ocr-4-0`; the moving `mistral-ocr-4` alias is not this fixed release. It introduced paragraph boxes and structural block labels. [OCR 4.0 model card and deprecation](https://docs.mistral.ai/models/ocr-4-0)
- Preserve this model-scoped fact: The hosted `mistral-ocr-4-0` release is retired according to Mistral’s September 30, 2026 retirement schedule. It is retained here as a historical identity; the named replacement is OCR 4.1. [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational and interpretation boundaries

- Explain this boundary: Do not assign OCR 4.1’s block-level confidence extension to this older release. Structured extraction is model output and should be checked against the original document when accuracy matters. [OCR 4.0 model card and deprecation](https://docs.mistral.ai/models/ocr-4-0) [OCR request and confidence-granularity contract](https://docs.mistral.ai/api/endpoint/ocr)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
