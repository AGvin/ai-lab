# Mistral OCR 4.1

Mistral OCR 4.1 is Mistral AI’s document-extraction release introduced on July 16, 2026 and made generally available on August 31, 2026.

## Translations

- English

## Relations

- Family: [Mistral OCR](../../../../)

## Model profile

Its exact API identifier is `mistral-ocr-4-1`. It extracts paragraph-level bounding boxes, structural block labels and block-level confidence scores. [OCR 4.1 model card](https://docs.mistral.ai/models/ocr-4-1) [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational boundaries

Confidence output is opt-in: `confidence_scores_granularity` selects page, block or word scores and otherwise defaults to no scores. A score does not certify the extracted text. [OCR request and confidence-granularity contract](https://docs.mistral.ai/api/endpoint/ocr)

OCR output and structured annotations require validation against the source document. API file handling, pricing and commercial deployment packaging are service properties. [OCR output and confidence scores](https://docs.mistral.ai/studio/document-processing/basic_ocr)

## Official resources

- [OCR 4.1 model card](https://docs.mistral.ai/models/ocr-4-1)
- [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)
- [OCR request and confidence-granularity contract](https://docs.mistral.ai/api/endpoint/ocr)
- [OCR output and confidence scores](https://docs.mistral.ai/studio/document-processing/basic_ocr)
