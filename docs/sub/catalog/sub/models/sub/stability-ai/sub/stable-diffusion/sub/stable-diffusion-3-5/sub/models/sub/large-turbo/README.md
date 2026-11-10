# Stable Diffusion 3.5 Large Turbo

Stable Diffusion 3.5 Large Turbo is the distilled, speed-oriented Large Turbo model in Stability AI’s 3.5 series. Stability describes adversarial diffusion distillation and a four-step generation setup. It is a distinct trained variant, not merely a runtime flag applied to Large.

## Inference trade-off

The official model card gives the intended step and guidance configuration. Fewer generation steps can reduce work, but observed latency and image quality still depend on the runtime, hardware, resolution and prompt. A benchmark for Large or an optimized runtime build is not automatically a result for the released Turbo model. Keep the exact checkpoint and conversion lineage with any deployment comparison.

## Access and license

The official model distribution identifies the Stability AI Community license and requires acceptance of access conditions. Confirm the agreement’s commercial eligibility and any Enterprise requirement. API or partner hosting adds service-specific terms and processing boundaries; downloadable weights do not include every hosted entitlement.

## Relations

- Member of: [Stable Diffusion 3.5](../../../../)

## Official resources

- [Series release](https://stability.ai/news/introducing-stable-diffusion-3-5)
- [Official documentation](https://stability.ai/core-models)
- [Official Large Turbo model card](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-turbo)
- [License program](https://stability.ai/license)
