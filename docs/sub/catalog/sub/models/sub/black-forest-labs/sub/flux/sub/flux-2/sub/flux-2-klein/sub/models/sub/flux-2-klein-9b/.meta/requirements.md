# Documentation Requirements

## Identity and provenance

- FLUX.2 [klein] 9B is Black Forest Labs' separately published 9-billion-parameter 4-step distilled flow-transformer model for image generation and editing. Its weights use FLUX Non-Commercial.
- The official FLUX.2 [klein] 9B model card identifies this checkpoint. The 9B figure describes the image generator; it does not include every auxiliary component loaded for inference. [FLUX.2-klein-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B).
- The official model table marks both step and guidance distillation. Use the documented four-step workflow; base weights at the same scale are separate learned objects. [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2) [FLUX.2-klein-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B).
- The 9B image generator uses a separate 8B Qwen3 text embedder. Generator scale and combined pipeline memory are different quantities. [FLUX.2-klein-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B).
- The public release date is 2026-01-15, as stated in the launch announcement. [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence).

## Operational decision boundaries

- The FLUX Non-Commercial license limits model and derivative operation to its permitted noncommercial scope unless separately licensed. Its conditional permission for commercial outputs does not authorize commercial weight operation. [FLUX Non-Commercial License v2.1](https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL) [FLUX.2-klein-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B).
- Pin the four-step loader, precision, resolution, encoder placement and offload. Published VRAM and speed figures apply to their specific configuration; they do not certify every GPU or prove local execution here. [FLUX.2-klein-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).
- BFL separately publishes a 9B-KV distribution whose reference-image key/value cache is reused after the first denoising step. Select its documented checkpoint and cache-enabled loader explicitly. The reviewed sources do not establish whether its learned parameters differ from ordinary 9B; it is not accepted here as another model, an alias, or a proven derivative. [FLUX.2-klein-9b-kv model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv) [FLUX.2 Klein KV cache implementation](https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_klein_kv_cache.md) [FLUX.2 model loader configuration](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/util.py).
- Review text rendering, instruction compliance, reference preservation and bias on intended prompts. Keep any remote text encoding or prompt rewriting visible to the workflow owner. The model produces images rather than verified factual answers. [FLUX.2-klein-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
