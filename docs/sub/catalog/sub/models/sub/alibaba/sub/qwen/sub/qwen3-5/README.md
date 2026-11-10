# Qwen3.5

Qwen3.5 is a Qwen Team model series within the Qwen family. This bounded catalog branch represents the separately released 9B and 35B-A3B pretrained and post-trained vision-language checkpoints; it is not a complete inventory of every Qwen3.5 scale or deployment route.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [Qwen](../../README.md) | `model-family` |
| `has-member` | [Qwen3.5-9B-Base](sub/models/sub/qwen3-5-9b-base/README.md) | `model` |
| `has-member` | [Qwen3.5-9B](sub/models/sub/qwen3-5-9b/README.md) | `model` |
| `has-member` | [Qwen3.5 35B-A3B Base](sub/models/sub/qwen3-5-35b-a3b-base/) | `model` |
| `has-member` | [Qwen3.5 35B-A3B](sub/models/sub/qwen3-5-35b-a3b/) | `model` |

## Identity and scope

The exact [Base card](https://huggingface.co/Qwen/Qwen3.5-9B-Base) identifies a pretrained-only checkpoint; the [post-trained card](https://huggingface.co/Qwen/Qwen3.5-9B) and its metadata identify the separate adapted checkpoint. Preserve their training-stage and learned-weight distinction. Thinking modes, quantized packages and hosted model routes are not automatic additional learned-model identities.

## Series boundaries

The 35B-A3B pretrained Base and post-trained checkpoints are separately materialized alongside 9B. The post-trained 35B-A3B is the immediate source of the Huihui modification; no stage or dense/MoE capability is transferred between siblings.

Follow the exact member for architecture, modality, license, context configuration and runtime support. Do not project a generic family MoE highlight onto the dense 9B member or transfer post-trained instruction-following claims to Base. The represented members use Apache-2.0; this bounded review does not establish one license or capability contract for every series member.

## Downstream lineage

BFL's [Prompt Upsampler](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup) fine-tunes the post-trained 9B checkpoint, not the pretrained Base directly. A downstream application using a model does not make the application's image generator its training parent. No inference, benchmark reproduction or complete Qwen3.5 sibling sweep is claimed.

## Official resources

- [Qwen3.5-9B-Base original model card](https://huggingface.co/Qwen/Qwen3.5-9B-Base)
- [Qwen3.5-9B original model card](https://huggingface.co/Qwen/Qwen3.5-9B)
