# FLUX 3 Action SO-101

**FLUX 3 Action SO-101** is a separately published Black Forest Labs **SO-101 embodiment fine-tuned policy**. [Original source](https://huggingface.co/black-forest-labs/flux-3-action-so101) [BFL launch](https://huggingface.co/blog/black-forest-labs/flux-3-action).

## Learned identity and use

This model is fine-tuned separately from the FLUX 3 Action adaptation base for the SO-101 observation and robot action interface, released as a gated LeRobot model. SO-101 action/state normalization, camera layout, hardware interfaces and safety bounds are distinct from DROID. Never assume DROID performance transfers to SO-101.

Use only with the matching action/state normalization, observation layout, policy loader and any required shared video/text encoders. A correct model file alone does not supply a safe robot controller.

## Licensing, safety and limitations

The model weights are gated under the **FLUX Kommunity License**; the accompanying reference code uses Apache-2.0 and does not grant a blanket commercial model-weights license. For physical hardware, verify limits and interlocks for motion, force and workspace, use a separate emergency stop, and require human supervision. The 2026 provider benchmark is not an independently reproduced AI Lab result. No production readiness, local GPU fit or physical execution test is claimed.

The [Russia-linked provenance policy](../../../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) remains applicable if verifiable ownership or upstream technology evidence emerges; no unsupported specific Russian ownership allegation is made here.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX 3](../../../../README.md) | `model-series` |

## Sources

- [Official learned-model checkpoint](https://huggingface.co/black-forest-labs/flux-3-action-so101)
- [BFL Action model page](https://bfl.ai/models/flux-3-action)
- [Model usage and loading guide](https://github.com/black-forest-labs/flux-action/blob/main/docs/setup.md)
- [FLUX 3 Action publication](https://huggingface.co/blog/black-forest-labs/flux-3-action)
