# FLUX 3 Action

FLUX 3 Action here identifies Black Forest Labs' released 7B world-action adaptation base, published as black-forest-labs/flux-3-action-base. It jointly models future video and action chunks and requires embodiment-specific adaptation before use as a complete robot policy. [FLUX 3 Action technical product page](https://bfl.ai/models/flux-3-action) [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Action reference code](https://github.com/black-forest-labs/flux-action) [FLUX 3 Action DROID policy card](https://huggingface.co/black-forest-labs/flux-3-action-droid) [FLUX 3 Action SO-101 policy card](https://huggingface.co/black-forest-labs/flux-3-action-so101) [BFL Action launch listing](https://bfl.ai/blog).

## Identity and scope

This record identifies the official adaptation-base checkpoint. The official launch listing is dated 2026-09-23. DROID and SO-101 are separately fine-tuned policies. DROID also has guidance-distilled and step-distilled learned variants; FP8 packaging alone is an artifact distinction. [FLUX 3 Action technical product page](https://bfl.ai/models/flux-3-action) [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Action reference code](https://github.com/black-forest-labs/flux-action) [FLUX 3 Action DROID policy card](https://huggingface.co/black-forest-labs/flux-3-action-droid) [FLUX 3 Action SO-101 policy card](https://huggingface.co/black-forest-labs/flux-3-action-so101) [BFL Action launch listing](https://bfl.ai/blog).

The shared action trunk and supplied heads do not remove the need for embodiment-specific heads, processors and training. The separately supplied Qwen3-VL-4B-Instruct encoder retains its own Apache 2.0 terms and is not part of the 7B generator label. [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base).

## Use and limitations

Action weights use the FLUX Kommunity license; reference code uses Apache 2.0. The license's conditional commercial-output exception for qualifying users is not a blanket commercial model license. Review the current agreement and its aggregate-affiliate revenue test before relying on that exception. [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Action reference code](https://github.com/black-forest-labs/flux-action) [FLUX Kommunity License v1.0](https://huggingface.co/black-forest-labs/flux-3-image-klein-base/blob/main/LICENSE.md).

Do not transfer DROID success rates, action normalization or camera assumptions to this base checkpoint or another embodiment. Select the exact policy, saved processors and observation/action convention before recorded-data or simulation validation. [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Action DROID policy card](https://huggingface.co/black-forest-labs/flux-3-action-droid) [FLUX 3 Action SO-101 policy card](https://huggingface.co/black-forest-labs/flux-3-action-so101).

The model does not enforce joint, velocity, force or workspace limits. Application controllers and hardware stops remain necessary. This catalog review performs no inference or robot execution and establishes no physical deployment readiness. [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base).

Fine-tuning, BF16/FP8 inference and CPU-offload paths have different loaders and memory requirements. Pin the exact checkpoint, precision, code revision and encoder placement instead of using one policy's measured VRAM as a base-model guarantee. [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Action reference code](https://github.com/black-forest-labs/flux-action).

## Related trained policies

- [FLUX 3 Action DROID](../flux-3-action-droid/README.md) — DROID embodiment fine-tuned policy
- [FLUX 3 Action DROID guidance-distilled](../flux-3-action-droid-guidance-distilled/README.md) — guidance-distilled separately trained DROID student
- [FLUX 3 Action DROID step-distilled](../flux-3-action-droid-step-distilled/README.md) — single-step-distilled separately trained DROID student
- [FLUX 3 Action SO-101](../flux-3-action-so101/README.md) — SO-101 embodiment fine-tuned policy

These independently trained sibling policies have embodiment-specific action/state conventions, and FP8r precision packaging does not create extra trained models. [BFL release](https://huggingface.co/blog/black-forest-labs/flux-3-action).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX 3](../../../../README.md) | `model-series` |

## Sources

- [FLUX 3 Action technical product page](https://bfl.ai/models/flux-3-action)
- [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base)
- [FLUX 3 Action reference code](https://github.com/black-forest-labs/flux-action)
- [FLUX 3 Action DROID policy card](https://huggingface.co/black-forest-labs/flux-3-action-droid)
- [FLUX 3 Action SO-101 policy card](https://huggingface.co/black-forest-labs/flux-3-action-so101)
- [BFL Action launch listing](https://bfl.ai/blog)
- [FLUX Kommunity License v1.0](https://huggingface.co/black-forest-labs/flux-3-image-klein-base/blob/main/LICENSE.md)
