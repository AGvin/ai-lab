# FLUX.1 Krea [dev]

FLUX.1 Krea [dev] is a separately released 12-billion-parameter, guidance-distilled rectified-flow model for text-to-image generation, jointly developed by Black Forest Labs and Krea. The [official checkpoint](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev) was released on July 31, 2025.

## Identity and provenance

[Krea's technical report](https://www.krea.ai/blog/flux-krea-open-source-release) identifies BFL-provided `flux-dev-raw` as the starting checkpoint. Krea describes supervised fine-tuning, including synthetic Krea-1 samples, followed by preference optimization. The Hub classifies the release as a FLUX.1-dev fine-tune; that registry tag does not establish that its starting weights equal the released FLUX.1-dev weights.

[BFL documents ecosystem compatibility](https://bfl.ai/blog/flux-1-krea-dev). Compatibility is not weight identity, and using Krea-1 samples does not itself establish weight inheritance from Krea-1. Neither the Krea application nor an API endpoint is this trained checkpoint.

## Use and limitations

- **Weights:** gated download under the FLUX dev Non-Commercial License. Model use, generated-output permissions and hosted API contracts are separate.
- **Quality:** aesthetics and realism are publisher claims. Evaluate prompt adherence and accepted-result quality on the intended assignment; no independent AI Lab benchmark is established.
- **Runtime:** compatible tooling does not guarantee GPU fit, memory use, throughput or inference settings. No local inference test has been performed.
- **Limitations:** the model may mismatch prompts, amplify bias and cannot provide reliable factual information.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `produced-by` | [Black Forest Labs](../../../../../../../../../../../producers/sub/b/sub/black-forest-labs/README.md) | `organization` |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |
| `produced-by` | [Krea](../../../../../../../../../../../producers/sub/k/sub/krea/README.md) | `organization` |

## Sources

- [Official model card and weights](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev)
- [Krea training report](https://www.krea.ai/blog/flux-krea-open-source-release)
- [BFL release](https://bfl.ai/blog/flux-1-krea-dev)
- [BFL model card and license](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-Krea-dev.md)
