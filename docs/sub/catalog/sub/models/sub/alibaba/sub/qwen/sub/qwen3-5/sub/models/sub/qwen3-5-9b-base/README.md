# Qwen3.5-9B-Base

Qwen3.5-9B-Base is Qwen Team's separately released pretrained-only 9B-scale vision-language checkpoint. It is the upstream learned model for the post-trained Qwen3.5-9B and is intended for adaptation and research rather than direct conversation.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [Qwen3.5](../../../../README.md) | `model-series` |
| `has-derivative` | [Qwen3.5-9B](../qwen3-5-9b/README.md) | `model` |

## Training-stage boundary

The [exact Base introduction](https://huggingface.co/Qwen/Qwen3.5-9B-Base) explicitly identifies pretrained-only weights. A copied overview later says “Pre-training & Post-training”; retain the exact introduction's pretrained-only boundary rather than promoting that inconsistent overview label to a Base fact. Chat/control tokens and generic registry chat snippets do not establish a conversation-tuned model.

## License and use

The released checkpoint is Apache-2.0. The [published repository](https://huggingface.co/Qwen/Qwen3.5-9B-Base/tree/main) contains independently downloadable model and processor artifacts. Pin the model/processor revision and a compatible multimodal runtime, and validate the intended adaptation or inference behavior; artifact size and a 9B name are not peak-memory estimates.

## Limitations

Do not inherit the post-trained model's benchmark results, reasoning settings or tool-use behavior. Download availability does not guarantee perpetual runtime support or a matching hosted API. This profile establishes no independent runtime, benchmark or beneficial-ownership verification.

## Official resources

- [Qwen3.5-9B-Base original model card](https://huggingface.co/Qwen/Qwen3.5-9B-Base)
- [Qwen3.5-9B-Base weight and processor files](https://huggingface.co/Qwen/Qwen3.5-9B-Base/tree/main)
- [Qwen3.5-9B original model card](https://huggingface.co/Qwen/Qwen3.5-9B)
