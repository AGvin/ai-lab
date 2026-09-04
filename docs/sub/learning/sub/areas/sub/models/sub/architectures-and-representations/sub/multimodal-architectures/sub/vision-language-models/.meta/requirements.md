# Documentation Requirements

## Requirements

- Teach Vision-Language Models as multimodal architectures that jointly process visual and linguistic information, distinct from simple OCR pipelines or loosely coupled vision-plus-LLM systems.
- Explain architecture/training diversity and common visual preprocessing/token/detail constraints without freezing one model family's design as universal.
- Distinguish visual understanding from image generation and keep concrete task workflows with `modalities-and-tasks/multimodal/vision-language`.
- Explain that resize, crop, tiling, compression, frame sampling, and visual-token limits can remove fine evidence before reasoning begins.
- Treat OCR, counting, spatial relations, charts, and fine-detail answers as fallible model outputs that require source verification when correctness matters.
- Keep exact model capabilities, provider-interface support, current image limits, and runtime compatibility source-backed with catalog/evidence owners.

## Validation

- VLM identity is not reduced to OCR plus text generation.
- Fine-detail answers are not treated as verified observation solely because they are plausible.
- Interface support is not inferred from architecture capability alone.
