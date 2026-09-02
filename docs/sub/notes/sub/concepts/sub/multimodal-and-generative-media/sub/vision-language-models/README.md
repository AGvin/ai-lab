# Vision-Language Models

Legacy residual retained for practical VLM applications, visual-input preparation, source verification, and screenshot/document security guidance that is intentionally outside the canonical Vision-Language Models classification owner.

> **Migration note:** VLM identity, distinction from broader multimodal models and simple OCR/vision-plus-LLM pipelines, architecture/training diversity, visual preprocessing and token/detail constraints, understanding-versus-generation boundaries, model-capability versus provider-interface support, and OCR/counting/spatial/fine-detail limitations are already preserved in `docs/sub/concepts/sub/models/sub/classification/sub/vision-language-models/`. The remaining material below stays here until its exact learning, workflow, evaluation, security, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Vision-language models can support workflows such as:

- screenshot and UI analysis;
- document and chart question answering;
- image classification and captioning;
- visual inspection assistance;
- multimodal agents that consume camera images or browser screenshots.

These are application examples rather than part of the canonical VLM classification.

## Visual-input and verification residual

For fine-detail work, provide inputs at sufficient useful resolution and account for any resize, crop, tiling, compression, frame sampling, or visual-token limits imposed by the concrete model/runtime. Small text, exact counts, spatial relationships, charts, and fine visual details should be checked against the source rather than inferred from a plausible answer alone.

Treat OCR and visual reasoning as fallible model outputs, not as verified observation or measurement. When correctness matters, inspect the original image/document and use task-appropriate validation.

Screenshots, documents, rendered web pages, and other visual inputs can also contain adversarial or untrusted instructions. Multimodal-agent workflows should apply the relevant indirect-prompt-injection and trust-boundary controls instead of treating visible text as automatically authorized instructions.

These practical input-preparation, verification, and security practices remain migration source material until their exact learning, workflow, evaluation, security, or decision-support owners are verified.
