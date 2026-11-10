# Aya Vision

Aya Vision is the multilingual vision-language series released on 4 March 2025. Its represented 8B and 32B model identities accept text and images and produce text. [Source 1](https://cohere.com/blog/aya-vision) · [Source 2](https://huggingface.co/CohereLabs/aya-vision-8b) · [Source 3](https://huggingface.co/CohereLabs/aya-vision-32b)

## Release, modalities and lineage

Cohere released Aya Vision on 4 March 2025. The represented models use a language component, SigLIP2 vision encoder and multimodal adapter to produce text from text and images. The 8B card links Command R7B 12-2024; the 32B card identifies Aya Expanse 32B. Both specific cards document 23 languages and a 16K context. [Release](https://cohere.com/blog/aya-vision) · [8B architecture](https://huggingface.co/CohereLabs/aya-vision-8b) · [32B architecture](https://huggingface.co/CohereLabs/aya-vision-32b)

## Access and visual evaluation

Official weight downloads have model-card access and noncommercial-license conditions. Current Cohere documentation lists the 32B route as live and retires the 8B route on 4 April 2026. For local image tasks, use the matching processor and multimodal chat template, and evaluate OCR, captions and image-grounded answers on the languages and image quality that matter to the application. [Provider status](https://docs.cohere.com/docs/models) · [Retirement notice](https://docs.cohere.com/docs/deprecations) · [Current processor workflow](https://huggingface.co/docs/transformers/model_doc/aya_vision)

## Represented members

| Model or series | Scope from its concrete record |
| --- | --- |
| [Aya Vision 32B](sub/models/sub/aya-vision-32b/README.md) | 32B-class text/image model; 23 languages; 16K context; language parent Aya Expanse 32B; live 32B Chat route. |
| [Aya Vision 8B](sub/models/sub/aya-vision-8b/README.md) | 8B-class text/image model; 23 languages; 16K context; language parent Command R7B 12-2024; 8B Chat route retired 4 April 2026. |

## Relations

- Members: [Aya Vision 32B](sub/models/sub/aya-vision-32b/README.md), [Aya Vision 8B](sub/models/sub/aya-vision-8b/README.md)
- Member of: [Aya](../../README.md)

## Official resources

- <https://cohere.com/blog/aya-vision>
- <https://huggingface.co/CohereLabs/aya-vision-8b>
- <https://huggingface.co/CohereLabs/aya-vision-32b>
- <https://docs.cohere.com/docs/aya-vision>
- <https://docs.cohere.com/docs/models>
- <https://docs.cohere.com/docs/deprecations>
- <https://huggingface.co/docs/transformers/model_doc/aya_vision>
