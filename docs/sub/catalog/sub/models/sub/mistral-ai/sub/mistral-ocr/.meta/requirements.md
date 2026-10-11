# Documentation Requirements

## Requirements

- Identify Mistral OCR as Mistral AI's document-parsing/OCR model family.
- Link Mistral OCR 4.1 as the latest GA release and retain Mistral OCR 4.0 as a separately released predecessor that remains available for existing integrations unless first-party lifecycle state changes.
- Keep Document AI application/service behavior, API pricing, no-code workflows, and self-hosting packaging separate from intrinsic model identity.
- Treat supported languages, output schema, bounding boxes, block classification, confidence behavior, benchmarks, pricing, aliases, and deployment/lifecycle state as freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.
- The model family is not conflated with the broader hosted Document AI product surface.
- `mistral-ocr-latest` / `mistral-ocr-4` alias movement does not erase the separate 4.0 and 4.1 trained/released identities.
