# Documentation Requirements

## Identity and provenance

- FLUX.2 [klein] 4B is Black Forest Labs' separately published 4-billion-parameter 4-step distilled flow-transformer model for image generation and editing. Its weights use Apache 2.0.
- The official FLUX.2 [klein] 4B model card identifies this checkpoint. The 4B figure describes the image generator; it does not include every auxiliary component loaded for inference. [FLUX.2-klein-4B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B).
- The official model table marks both step and guidance distillation. Use the documented four-step workflow; base weights at the same scale are separate learned objects. [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2) [FLUX.2-klein-4B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B).
- The public release date is 2026-01-15, as stated in the launch announcement. [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence).

## Operational decision boundaries

- The weight license is Apache 2.0. Keep any separately supplied text encoder, code, modifications and hosted-service terms visible; a permissive model license does not validate output accuracy. [FLUX.2-klein-4B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) [FLUX.2 Klein 4B Apache License](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md).
- Pin the four-step loader, precision, resolution, encoder placement and offload. Published VRAM and speed figures apply to their specific configuration; they do not certify every GPU or prove local execution here. [FLUX.2-klein-4B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).
- Review text rendering, instruction compliance, reference preservation and bias on intended prompts. Keep any remote text encoding or prompt rewriting visible to the workflow owner. The model produces images rather than verified factual answers. [FLUX.2-klein-4B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
