# Documentation Requirements

## Requirements

- Identify Mistral OCR as Mistral AI's document-parsing/OCR model family.
- Render the standard entity-relations block and preserve exact lifecycle differences between represented releases, including retired OCR 4.0 and continuing GA OCR 3.
- Keep Document AI application/service behavior, API pricing, no-code workflows, and self-hosting packaging separate from intrinsic model identity.
- Treat supported languages, output schema, bounding boxes, block classification, confidence behavior, benchmarks, pricing, aliases, and deployment/lifecycle state as freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.
- The model family is not conflated with the broader hosted Document AI product surface.
- `mistral-ocr-latest` / `mistral-ocr-4` alias movement does not erase the separate 4.0 and 4.1 trained/released identities.

## Source-backed profile

- Required reader orientation: Mistral OCR is Mistral AI’s document-extraction model family.
- Preserve this model-scoped fact: The family retains OCR 3 for its documented ongoing GA availability, OCR 4.0 as a retired hosted release, and OCR 4.1 as the current GA successor. [OCR 3 model card and continuing availability](https://docs.mistral.ai/models/ocr-3-25-12) [OCR 4.1 model card](https://docs.mistral.ai/models/ocr-4-1) [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational and interpretation boundaries

- Explain this boundary: OCR release identity, moving API aliases and the wider Document AI service are different concerns. Bounding boxes, labels and confidence granularity must be verified for the exact model version. [OCR request and confidence-granularity contract](https://docs.mistral.ai/api/endpoint/ocr)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
