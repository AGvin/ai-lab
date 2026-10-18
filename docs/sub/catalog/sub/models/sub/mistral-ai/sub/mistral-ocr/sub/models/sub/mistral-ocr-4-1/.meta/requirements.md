# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Mistral OCR 4.1 as the current GA OCR release and successor to OCR 4.0 for new integrations.
- Preserve paragraph-level bounding boxes, structural block labels, block-level confidence scores, and other capabilities only at exact first-party release scope.
- Treat pricing, throughput, API aliases, deployment packaging, feature support, and lifecycle state as freshness-sensitive.

## Validation

- Membership resolves to Mistral OCR.
- The 4.1 identity remains distinct from the alias `mistral-ocr-4`, which may move between compatible releases.

## Source-backed profile

- Required reader orientation: Mistral OCR 4.1 is Mistral AI’s document-extraction release introduced on July 16, 2026 and made generally available on August 31, 2026.
- Preserve this model-scoped fact: Its exact API identifier is `mistral-ocr-4-1`. It extracts paragraph-level bounding boxes, structural block labels and block-level confidence scores. [OCR 4.1 model card](https://docs.mistral.ai/models/ocr-4-1) [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational and interpretation boundaries

- Explain this boundary: Confidence output is opt-in: `confidence_scores_granularity` selects page, block or word scores and otherwise defaults to no scores. A score does not certify the extracted text. [OCR request and confidence-granularity contract](https://docs.mistral.ai/api/endpoint/ocr)
- Explain this boundary: OCR output and structured annotations require validation against the source document. API file handling, pricing and commercial deployment packaging are service properties. [OCR output and confidence scores](https://docs.mistral.ai/studio/document-processing/basic_ocr)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
