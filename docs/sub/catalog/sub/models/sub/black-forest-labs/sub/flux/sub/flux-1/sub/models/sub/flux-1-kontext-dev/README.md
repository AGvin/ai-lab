# FLUX.1 Kontext [dev]

Released 12B guidance-distilled rectified-flow model for text-instructed image editing. BFL released the open weights on June 26, 2025. This is distinct from hosted Kontext pro/max and from general FLUX.1-dev text-to-image weights. [Official checkpoint](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev).

## Identity and scope

Edits an input image from text instructions, including iterative changes. Character/reference preservation is a provider capability claim, not a guarantee. [First-party implementation](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-kontext-dev.md).

## Use and limitations

Review edit fidelity and unintended drift across successive edits. TensorRT BF16/FP8/FP4 distributions are runtime artifacts, not extra trained identities; API behavior does not establish local-checkpoint behavior.

Gated weights use the FLUX dev Non-Commercial License. Model-weight use, output permissions and hosted API contracts are separate; commercial model use requires appropriate rights. No local inference test or independent quality, memory or speed benchmark has been performed.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [Official model card and weights](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)
- [Reference implementation](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-kontext-dev.md)
- [BFL release and lifecycle information](https://bfl.ai/blog/flux-1-kontext-dev)
