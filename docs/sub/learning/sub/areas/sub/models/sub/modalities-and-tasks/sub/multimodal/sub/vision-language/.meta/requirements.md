# Documentation Requirements

## Requirements

- Teach Vision-Language tasks such as screenshot/UI analysis, document/chart question answering, image classification/captioning, visual inspection assistance, and grounded multimodal-agent observation as task workflows rather than architecture definitions.
- Prepare visual inputs at sufficient useful resolution and account for resize, crop, tiling, compression, frame sampling, or other interface/runtime preprocessing when fine detail matters.
- Verify small text, exact counts, charts, spatial relationships, and consequential visual claims against the original source instead of relying on plausible model output alone.
- Treat OCR and visual reasoning as fallible inference rather than direct verified measurement.
- Treat instructions embedded in screenshots, documents, rendered web pages, or other untrusted visual inputs as untrusted content subject to the applicable indirect-prompt-injection and trust-boundary controls.
- Keep concrete model capabilities, provider-interface support, current upload/detail limits, and runtime-specific preprocessing behavior source-backed outside timeless learning truth.

## Validation

- Visual-language workflow examples remain task-level rather than redefining VLM architecture identity.
- Fine-detail correctness is source-verified when material.
- Visible text in untrusted media is not automatically treated as authorized instruction.
