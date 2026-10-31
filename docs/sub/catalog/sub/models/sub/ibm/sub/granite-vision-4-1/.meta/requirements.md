# Documentation Requirements

## Identity and provenance

- Identify Granite Vision 4.1 as IBM's April 2026 document-focused vision-language family represented by the 4B checkpoint.
- Preserve IBM producer provenance and the source-backed fine-tuning lineage from the canonical Granite 4.1 3B instruction-tuned checkpoint to Vision 4.1 4B; verify reciprocal model relations.
- Keep Docling, OCR pipelines, prompt/task wrappers, serving routes, quantizations and hosted services separate from the trained-model identity.

## Operational decision boundaries

- Preserve chart extraction, table extraction, semantic key-value extraction and general image-to-text support at exact model-card scope.
- Treat task tags and output formats as prompting/runtime contracts rather than separate model identities.
- The reviewed weights state Apache 2.0. Published benchmark comparisons, structured extraction accuracy and runtime integrations remain implementation- and data-sensitive.
- Do not treat image understanding as image generation or a guarantee that document extraction is lossless.

## Validation

- Family membership resolves exactly to Granite Vision 4.1 4B.
- Producer provenance resolves to IBM.
- The vision model's derived-from relation resolves to the exact canonical Granite 4.1 3B checkpoint, with its reciprocal has-derivative edge.
- This assessment grants no runtime, benchmark-reproduction, cache or final-render credit.
