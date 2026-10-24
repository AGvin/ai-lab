# Documentation Requirements

## Identity and provenance

- FLUX.1-schnell is Black Forest Labs' 12-billion-parameter rectified-flow transformer for text-to-image generation. Latent adversarial diffusion distillation enables the documented 1–4-step workflow; its weights are released under Apache 2.0.
- The official checkpoint is black-forest-labs/FLUX.1-schnell: a 12B image generator with a distilled 1–4-step workflow. Partner API endpoints and quantized distributions do not create additional learned identities by themselves. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Operational decision boundaries

- The official card provides a BF16 Diffusers example with CPU offload. Fit and speed depend on precision, resolution, offload and the other loaded components; no local execution or universal minimum VRAM is established here. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).
- Use it for image synthesis, with review of rendered text, prompt compliance and bias. BFL warns that it is not a source of factual information; the permissive weight license does not certify generated content as correct. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
