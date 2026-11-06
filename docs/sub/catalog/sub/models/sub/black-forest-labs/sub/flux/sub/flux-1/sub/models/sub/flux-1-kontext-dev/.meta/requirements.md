# Documentation Requirements

## Identity and provenance

- Identify the exact `black-forest-labs/FLUX.1-Kontext-dev` checkpoint, independently published by BFL within FLUX.1. [Official registry](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev).
- Released 12B guidance-distilled rectified-flow model for text-instructed image editing. BFL released the open weights on June 26, 2025. This is distinct from hosted Kontext pro/max and from general FLUX.1-dev text-to-image weights. [First-party documentation](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-kontext-dev.md) [BFL release](https://bfl.ai/blog/flux-1-kontext-dev).
- Render the standard current-entity relation block; preserve a single model identity rather than duplicating precision/runtime distributions.

## Operational decision boundaries

- Edits an input image from text instructions, including iterative changes. Character/reference preservation is a provider capability claim, not a guarantee. [Reference documentation](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-kontext-dev.md).
- Review edit fidelity and unintended drift across successive edits. TensorRT BF16/FP8/FP4 distributions are runtime artifacts, not extra trained identities; API behavior does not establish local-checkpoint behavior. [Model card](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev).
- Separate gated non-commercial model-weight permissions, outputs and hosted-service terms; do not inherit schnell's Apache 2.0 license.
- Do not assert VRAM fit, quality ranking or measured speed without workload-specific tests.

## Validation

- Resolve series membership with one exact inverse and resolving reader navigation.
- Preserve dev versus pro/other checkpoint distinctions; no inferred direct learned-parent edge from compatible code.
- No runtime, benchmark, full catalog validation or exhaustive upstream-coverage claim.
