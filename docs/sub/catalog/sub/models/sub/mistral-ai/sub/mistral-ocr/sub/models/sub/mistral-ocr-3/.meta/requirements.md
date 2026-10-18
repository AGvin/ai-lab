# Documentation Requirements

## Requirements

- Identify Mistral OCR 3 as a distinct released trained-model identity from Mistral AI.
- Render the standard entity-relations block from validated canonical metadata.
- Keep model-specific specifications, artifact representations and hosted access context distinct.

## Validation

- The entity ID matches the canonical path and reciprocal relations resolve.
- Claims stay at the documented release scope, and generated output is not treated as a correctness or security guarantee.

## Source-backed profile

- Required reader orientation: Mistral OCR 3 is Mistral AI’s December 18, 2025 document-extraction model, identified by `mistral-ocr-2512`.
- Preserve this model-scoped fact: Mistral still lists OCR 3 as GA for existing integrations and production workloads. It extracts interleaved text and images and supports structured annotations. [OCR 3 model card and continuing availability](https://docs.mistral.ai/models/ocr-3-25-12)

## Operational and interpretation boundaries

- Explain this boundary: OCR 4.1’s paragraph-block and block-confidence contract must not be assumed for this release. Check extracted text and annotations against source pages; model output is not an authoritative copy. [OCR 3 model card and continuing availability](https://docs.mistral.ai/models/ocr-3-25-12) [OCR output and confidence scores](https://docs.mistral.ai/studio/document-processing/basic_ocr)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
