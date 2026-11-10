# FLUX.1-dev

FLUX.1-dev is Black Forest Labs' released 12-billion-parameter, guidance-distilled rectified-flow transformer for text-to-image generation. The official checkpoint is [`black-forest-labs/FLUX.1-dev`](https://huggingface.co/black-forest-labs/FLUX.1-dev), distinct from FLUX.1-schnell.

## Identity and scope

The model has its own pretrained/distilled weights and uses a text prompt to synthesize images. The publisher provides a gated weight release and reference inference code. Neither a hosted API endpoint nor a different weight format establishes a separate trained FLUX.1-dev model.

## Use and limitations

- **Weight license:** [FLUX dev Non-Commercial License](https://bfl.ai/legal/non-commercial-license-terms), not the Apache 2.0 terms applied to schnell. Commercial usage requires appropriate separate rights; do not conflate weight-use rights, outputs and hosted API terms.
- **Operational fit:** memory, speed, resolution, precision and inference steps depend on the selected framework and loaded supporting components. No local runtime or benchmarking has been performed for AI Lab.
- **Safety and fidelity:** the producer warns of prompt mismatches, bias and inability to provide factual information. Provider output-quality rankings are not independent AI Lab findings.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [FLUX.1-dev weights and model card](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- [Black Forest Labs official model card](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md)
- [FLUX dev Non-Commercial License](https://bfl.ai/legal/non-commercial-license-terms)
