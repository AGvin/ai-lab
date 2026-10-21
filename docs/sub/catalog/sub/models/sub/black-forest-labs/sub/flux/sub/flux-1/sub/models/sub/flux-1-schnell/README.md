# FLUX.1-schnell

FLUX.1-schnell is Black Forest Labs' 12-billion-parameter rectified-flow transformer for text-to-image generation. Latent adversarial diffusion distillation enables the documented 1–4-step workflow; its weights are released under Apache 2.0. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Identity and scope

The official checkpoint is black-forest-labs/FLUX.1-schnell: a 12B image generator with a distilled 1–4-step workflow. Partner API endpoints and quantized distributions do not create additional learned identities by themselves. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Use and limitations

The official card provides a BF16 Diffusers example with CPU offload. Fit and speed depend on precision, resolution, offload and the other loaded components; no local execution or universal minimum VRAM is established here. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

Use it for image synthesis, with review of rendered text, prompt compliance and bias. BFL warns that it is not a source of factual information; the permissive weight license does not certify generated content as correct. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
