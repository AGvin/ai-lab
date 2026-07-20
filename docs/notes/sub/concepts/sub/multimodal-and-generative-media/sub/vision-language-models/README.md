# Vision-Language Models

Vision-language models process visual information together with natural-language instructions or questions.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Images are converted into visual features or tokens and combined with a language model. The system can describe scenes, answer questions, read screenshots, interpret diagrams, compare images, or extract structured information. The model does not necessarily process every pixel at original resolution; preprocessing and visual-token budgets determine available detail.

## Practical use

- Screenshot and UI analysis.
- Document and chart question answering.
- Image classification and captioning.
- Visual inspection assistance.
- Multimodal agents that use cameras or browser screenshots.

## Trade-offs and limitations

Small text, exact counts, spatial relations, and fine visual details can be unreliable. OCR quality, image resizing, cropping, and compression affect results. A plausible description is not a precise measurement or verified observation.

## Common mistakes

- Assuming the model reads all visible text perfectly.
- Using one low-resolution image for detailed inspection.
- Treating visual inference as evidence without checking the source image.
- Ignoring prompt injection embedded in screenshots or documents.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Multimodal Models](../../../foundations-and-architecture/sub/multimodal-models/)
- [Multimodal Context](../multimodal-context/)
- [Indirect Prompt Injection](../../../safety-privacy-and-reliability/sub/indirect-prompt-injection/)
