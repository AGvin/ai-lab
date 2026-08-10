# Z-Image

Z-Image is the full-capacity undistilled foundation model in the Z-Image image-generation family, published as `Tongyi-MAI/Z-Image`.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model family

- [Z-Image](../../../..)

## Canonical profile

- Model repository: `Tongyi-MAI/Z-Image`
- Parameters: 6B
- Architecture: Scalable Single-Stream Diffusion Transformer (S3-DiT)
- Input: text prompts
- Output: images
- Training/distillation boundary: full-capacity undistilled foundation model
- License: Apache-2.0
- Public checkpoint release: January 27, 2026

The official model card distinguishes the base Z-Image model from the speed-oriented distilled Z-Image-Turbo variant. The variants are separate trained identities and must not be represented as runtime modes or versions of one model.

## Evidence boundary

Tongyi-MAI publishes qualitative prompt-adherence, diversity, and aesthetic claims for Z-Image. AI Lab media-creation selection must validate those properties on the intended task before using them as recommendation evidence.

Diffusers integration, hosted inference providers, quantized artifacts, workflow-engine support, memory fit, generation latency, and accepted-result cost are runtime/artifact/service/selection concerns rather than intrinsic model identity.

## Official resources

- [Z-Image model card](https://huggingface.co/Tongyi-MAI/Z-Image)
- [Z-Image repository](https://github.com/Tongyi-MAI/Z-Image)
