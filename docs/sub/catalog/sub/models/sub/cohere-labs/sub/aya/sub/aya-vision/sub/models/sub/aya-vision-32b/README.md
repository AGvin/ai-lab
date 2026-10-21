# Aya Vision 32B

Aya Vision 32B is Cohere Labs' nominal 32B-class multilingual vision-language model, released on 4 March 2025. The card documents text/image input, text output, 23 languages and a 16K context. [Source 1](https://huggingface.co/CohereLabs/aya-vision-32b) · [Source 2](https://cohere.com/blog/aya-vision)

## Identity and trained components

Its language component is explicitly Aya Expanse 32B. The model pairs that language component with the exact `google/siglip2-so400m-patch14-384` vision encoder through a multimodal adapter. Its output is text, including captions, OCR results and answers grounded in images. The published 32B label identifies the release class rather than an exact count of all multimodal tensors. [Specific architecture and model card](https://huggingface.co/CohereLabs/aya-vision-32b) · [Language-model parent](https://huggingface.co/CohereLabs/aya-expanse-32b) · [Release date](https://cohere.com/blog/aya-vision)

## Weights and hosted route

The current c4ai-aya-vision-32b Chat route is live with 16K context and a 4K maximum output. The official repository is `CohereLabs/aya-vision-32b`. Its file access is gated by displayed conditions, and the card lists CC-BY-NC-4.0 with Cohere Labs acceptable-use terms. Current hosted limits and weight-distribution conditions are separate scopes. [Weight identity and terms](https://huggingface.co/CohereLabs/aya-vision-32b) · [Current provider table](https://docs.cohere.com/docs/models) · [Retirement history](https://docs.cohere.com/docs/deprecations)

## Image processing and evaluation

Use AutoProcessor and a compatible AutoModelForImageTextToText implementation with the model's multimodal chat template. The specific card describes up to 12 image tiles plus a thumbnail, using 169 visual tokens per tile and up to 2,197 image tokens. Let the matching processor map aspect ratios and supported resolutions, and account for image tokens when planning the context. Pin the revision, processor, runtime and precision; test OCR, small text, captions and grounded answers on representative images and languages. [Image mapping](https://huggingface.co/CohereLabs/aya-vision-32b) · [Current runtime interface](https://huggingface.co/docs/transformers/model_doc/aya_vision)

## Relations

- Derived from: [Aya Expanse 32B](../../../../../aya-expanse/sub/models/sub/aya-expanse-32b/README.md)
- Member of: [Aya Vision](../../../../README.md)

## Official resources

- <https://huggingface.co/CohereLabs/aya-vision-32b>
- <https://cohere.com/blog/aya-vision>
- <https://huggingface.co/CohereLabs/aya-expanse-32b>
- <https://huggingface.co/google/siglip2-so400m-patch14-384>
- <https://docs.cohere.com/docs/aya-vision>
- <https://docs.cohere.com/docs/models>
- <https://docs.cohere.com/docs/deprecations>
- <https://huggingface.co/docs/transformers/model_doc/aya_vision>
