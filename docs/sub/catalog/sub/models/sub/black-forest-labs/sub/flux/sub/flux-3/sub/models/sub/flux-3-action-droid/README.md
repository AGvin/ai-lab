# FLUX 3 Action DROID

**FLUX 3 Action DROID** is a separately published Black Forest Labs **DROID embodiment fine-tuned policy**. [Original source](https://huggingface.co/black-forest-labs/flux-3-action-droid) [BFL launch](https://huggingface.co/blog/black-forest-labs/flux-3-action).

## Learned identity and use

This model is fine-tuned from the FLUX 3 Action 7B adaptation base for the DROID robot data/observation/action convention. DROID camera/state/action preprocessing and a matching action head are required; adapting this policy is not evidence of safe use on a different physical robot.

Use only with the matching action/state normalization, observation layout, policy loader and any required shared video/text encoders. A correct model file alone does not supply a safe robot controller.

## Licensing, safety and limitations

The model weights are gated under the **FLUX Kommunity License**; the accompanying reference code uses Apache-2.0 and does not grant a blanket commercial model-weights license. For physical hardware, verify limits and interlocks for motion, force and workspace, use a separate emergency stop, and require human supervision. The 2026 provider benchmark is not an independently reproduced AI Lab result. No production readiness, local GPU fit or physical execution test is claimed.

The [Russia-linked provenance policy](../../../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) remains applicable if verifiable ownership or upstream technology evidence emerges; no unsupported specific Russian ownership allegation is made here.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX 3](../../../../README.md) | `model-series` |

## Sources

- [Official learned-model checkpoint](https://huggingface.co/black-forest-labs/flux-3-action-droid)
- [BFL Action model page](https://bfl.ai/models/flux-3-action)
- [Model usage and loading guide](https://github.com/black-forest-labs/flux-action/blob/main/docs/setup.md)
- [FLUX 3 Action publication](https://huggingface.co/blog/black-forest-labs/flux-3-action)
