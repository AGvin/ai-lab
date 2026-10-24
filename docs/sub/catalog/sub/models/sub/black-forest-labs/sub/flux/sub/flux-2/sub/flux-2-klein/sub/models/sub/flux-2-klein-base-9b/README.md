# FLUX.2 [klein] Base 9B

FLUX.2 [klein] Base 9B is Black Forest Labs' separately published 9-billion-parameter undistilled base flow-transformer model for image generation and editing. Its weights use FLUX Non-Commercial. [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B).

## Identity and scope

The official FLUX.2 [klein] Base 9B model card identifies this checkpoint. The 9B figure describes the image generator; it does not include every auxiliary component loaded for inference. [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B).

This is the undistilled checkpoint intended for customization and fine-tuning; the same-scale distilled model is a separate learned object. A LoRA or fine-tune must be evaluated on its own provenance rather than treated as a precision-only build. [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

The 9B image generator uses a separate 8B Qwen3 text embedder. Generator scale and combined pipeline memory are different quantities. [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B).

The public release date is 2026-01-15, as stated in the launch announcement. [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence).

## Use and limitations

The FLUX Non-Commercial license limits model and derivative operation to its permitted noncommercial scope unless separately licensed. Its conditional permission for commercial outputs does not authorize commercial weight operation. [FLUX Non-Commercial License v2.1](https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL) [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B).

Base inference and fine-tuning have different step and memory demands from the four-step distilled workflow. Pin precision, resolution, guidance, encoder placement and offload; do not copy a distilled-model latency result to the base model. [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

Review text rendering, instruction compliance, reference preservation and bias on intended prompts. Keep any remote text encoding or prompt rewriting visible to the workflow owner. The model produces images rather than verified factual answers. [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.2 [klein]](../../../../README.md) | `model-series` |

## Sources

- [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B)
- [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2)
- [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)
- [FLUX Non-Commercial License v2.1](https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL)
