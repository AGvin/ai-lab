# Documentation Requirements

## Identity and provenance

- Command A Vision is the July 2025 112B vision-language model for images, documents, charts and text responses.
- The public card explicitly credits Cohere and Cohere Labs. It combines a language component based on Command A with google/siglip2-so400m-patch16-512 through a multimodal adapter. Only the existing Command A canonical parent is materialized as a derived-from relation. [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Command A Vision model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-vision-07-2025?blobs=true).

## Operational decision boundaries

- The advertised context is 128K and the live API table lists 8K output. The downloadable card uses a 32K default configuration and explicitly describes configuring 128K; preserve this difference between supported capacity and packaged default. The card lists six core languages. [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The Cohere Chat service currently accepts at most 20 images or 20 MB total per request. Image tiling consumes context; the model card describes up to 12 image tiles plus a thumbnail and recommends images up to 2048×1536. These are separate service and preprocessing constraints. [Cohere Chat image-input contract](https://docs.cohere.com/v2/docs/image-inputs) [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025).
- This model accepts images and emits text; the dedicated documentation says tool use is unsupported. Do not project original A’s tool capabilities or A+’s serving features onto this version. [Command A Vision documentation](https://docs.cohere.com/docs/command-a-vision).
- Research weights state CC-BY-NC 4.0 and the acceptable-use policy. OCR, small text, charts and spatial interpretation require representative evaluation; the upstream encoder is a component, not proof that the complete model shares its license. [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
