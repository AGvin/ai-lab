# Command A Vision

Command A Vision is the July 2025 112B vision-language model for images, documents, charts and text responses.

## Identity and provenance

The public card explicitly credits Cohere and Cohere Labs. It combines a language component based on Command A with google/siglip2-so400m-patch16-512 through a multimodal adapter. Only the existing Command A canonical parent is materialized as a derived-from relation. [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Command A Vision model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-vision-07-2025?blobs=true).

## Decision and operating boundaries

- The advertised context is 128K and the live API table lists 8K output. The downloadable card uses a 32K default configuration and explicitly describes configuring 128K; preserve this difference between supported capacity and packaged default. The card lists six core languages. [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The Cohere Chat service currently accepts at most 20 images or 20 MB total per request. Image tiling consumes context; the model card describes up to 12 image tiles plus a thumbnail and recommends images up to 2048×1536. These are separate service and preprocessing constraints. [Cohere Chat image-input contract](https://docs.cohere.com/v2/docs/image-inputs) [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025).
- This model accepts images and emits text; the dedicated documentation says tool use is unsupported. Do not project original A’s tool capabilities or A+’s serving features onto this version. [Command A Vision documentation](https://docs.cohere.com/docs/command-a-vision).
- Research weights state CC-BY-NC 4.0 and the acceptable-use policy. OCR, small text, charts and spatial interpretation require representative evaluation; the upstream encoder is a component, not proof that the complete model shares its license. [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Catalog relations

- [Cohere Labs](../../../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Command A](../../../../) — series or family.
- [Command A](../command-a-03-2025/) — derived from.

## Official resources

- [Additional official model documentation](https://docs.cohere.com/v1/docs/command-a-vision).
- [Command A Vision release](https://docs.cohere.com/v1/changelog/2025-07-31-command-a-vision).
- [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025).
- [Command A Vision model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-vision-07-2025?blobs=true).
- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Cohere Chat image-input contract](https://docs.cohere.com/v2/docs/image-inputs).
- [Command A Vision documentation](https://docs.cohere.com/docs/command-a-vision).
- [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
