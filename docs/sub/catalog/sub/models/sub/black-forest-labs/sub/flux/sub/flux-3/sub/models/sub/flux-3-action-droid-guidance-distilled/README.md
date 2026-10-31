# FLUX 3 Action DROID guidance-distilled

**FLUX 3 Action DROID guidance-distilled** is a separately published Black Forest Labs **guidance-distilled separately trained DROID student**. [Original source](https://huggingface.co/black-forest-labs/flux-3-action-droid/tree/main/variants/gd) [BFL launch](https://huggingface.co/blog/black-forest-labs/flux-3-action).

## Learned identity and use

This model is initialized from the fine-tuned DROID policy, trained under a frozen teacher, and released in the `variants/gd` BF16 directory. This learned student differs from root DROID weights. `variants/gd-fp8r` is a precision packaging of the same student, not a new model.

Use only with the matching action/state normalization, observation layout, policy loader and any required shared video/text encoders. A correct model file alone does not supply a safe robot controller.

## Licensing, safety and limitations

The model weights are gated under the **FLUX Kommunity License**; the accompanying reference code uses Apache-2.0 and does not grant a blanket commercial model-weights license. For physical hardware, verify limits and interlocks for motion, force and workspace, use a separate emergency stop, and require human supervision. The 2026 provider benchmark is not an independently reproduced AI Lab result. No production readiness, local GPU fit or physical execution test is claimed.

The [Russia-linked provenance policy](../../../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) remains applicable if verifiable ownership or upstream technology evidence emerges; no unsupported specific Russian ownership allegation is made here.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX 3](../../../../README.md) | `model-series` |

## Sources

- [Official learned-model checkpoint](https://huggingface.co/black-forest-labs/flux-3-action-droid/tree/main/variants/gd)
- [BFL Action model page](https://bfl.ai/models/flux-3-action)
- [Model usage and loading guide](https://github.com/black-forest-labs/flux-action/blob/main/docs/setup.md)
- [FLUX 3 Action publication](https://huggingface.co/blog/black-forest-labs/flux-3-action)
