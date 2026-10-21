# Z-Image

Z-Image is a 6B-parameter image-generation model family published by Tongyi-MAI. The official project describes a Scalable Single-Stream Diffusion Transformer (S3-DiT) architecture and multiple distinct trained variants rather than one executable model identity.

## Translations

- English

## Producer

- [Tongyi-MAI](../../../../../producers/sub/t/sub/tongyi-mai/)

## Family variants

The official repository currently describes Z-Image, Z-Image-Turbo, Z-Image-Omni-Base, and Z-Image-Edit as distinct variants with different training or task roles. The reviewed base Z-Image model and its distilled Z-Image-Turbo derivative are materialized here. Z-Image-Omni-Base and Z-Image-Edit remain upstream variants outside the materialized catalog until independently reviewed and required by scope.

## Models

- [`Z-Image`](./sub/models/sub/z-image/) — the full-capacity undistilled foundation model behind the Z-Image family.
- [`Z-Image-Turbo`](./sub/models/sub/z-image-turbo/) — the separately trained distilled derivative.

## Scope boundary

This page owns Z-Image family identity, publisher relation, shared architecture context, and model navigation. Exact model training state and license belong to concrete model pages. Diffusers/ComfyUI integration, hosted inference, quantization, hardware fit, security/privacy workflow, rankings, and recommendations belong to artifact/software/service/deployment, selection, policy, or evidence owners.

## Official resources

- [Z-Image repository](https://github.com/Tongyi-MAI/Z-Image)
- [Z-Image on Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image)
