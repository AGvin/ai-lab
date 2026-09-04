# FLUX.1-schnell

FLUX.1-schnell is a Black Forest Labs text-to-image model in the FLUX.1 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical profile

- Model repository: `black-forest-labs/FLUX.1-schnell`
- Parameters: 12B
- Architecture: rectified-flow transformer
- Input: text descriptions
- Output: images
- Training/distillation: latent adversarial diffusion distillation
- Generation regime: designed for high-quality generation in 1–4 steps
- License: Apache 2.0

The model card also records limitations including imperfect prompt matching, statistical bias amplification, and unsuitability for factual-information tasks. These are model limitations, not a ranking against other image generators.

## Evidence boundary

The official card publishes quality and prompt-following claims. AI Lab media-creation selection must validate those claims against the required image task, runtime, precision, dimensions, candidate budget, and accepted-result criteria before making a recommendation.

Third-party APIs, ComfyUI support, Diffusers integration, GPU memory fit, and quantizations are access/runtime/artifact concerns and must not be collapsed into intrinsic model identity.

## Official resources

- [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
