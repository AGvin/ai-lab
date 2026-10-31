# Qwen3.5-9B

Qwen3.5-9B is Qwen Team's released post-trained dense vision-language checkpoint derived from Qwen3.5-9B-Base. It is the exact upstream checkpoint used by BFL's separately fine-tuned FLUX 3 Image Klein Prompt Upsampler.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [Qwen3.5](../../../../README.md) | `model-series` |
| `derived-from` | [Qwen3.5-9B-Base](../qwen3-5-9b-base/README.md) | `model` |
| `has-derivative` | [FLUX 3 Image Klein Prompt Upsampler](../../../../../../../../../black-forest-labs/sub/flux-3-image-klein-prompt-upsampler/README.md) | `model` |

## Architecture and modalities

The [exact configuration](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/config.json) identifies Qwen3_5ForConditionalGeneration / qwen3_5, a 32-layer language stack, hidden size 4096 and FFN intermediate size 12288, with groups of three linear-attention layers followed by one full-attention layer and a separate vision encoder. This is the dense 9B member; a generic series sparse-MoE highlight does not establish MoE experts for this configuration. The model supports text/image/video input and text output. The 9B label describes language-model scale; it is not an active-parameter MoE or a peak-memory estimate.

## Training and operating boundary

The [official card and metadata](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/README.md) distinguish post-training from the separately released pretrained Base. Thinking/non-thinking settings are modes of this checkpoint. Qwen3-VL-4B-Instruct is another architecture and component, not this model or the Prompt Upsampler's parent. Use the matching processor/chat template and pin the exact weight/runtime revision; native or extended context claims do not prove feasible memory or all-runtime support.

## License and limitations

Weights use Apache-2.0. Benchmark/capability statements on the [publisher card](https://huggingface.co/Qwen/Qwen3.5-9B) are publisher evidence, not reproduced AI Lab measurements. A downloadable checkpoint does not define hosted API privacy, lifecycle or retention. Model-generated commands/tool arguments do not authorize execution; the application owns tool permissions, validation and isolation. No inference or independent beneficial-owner audit was performed.

## Official resources

- [Qwen3.5-9B original model card](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Qwen3.5-9B configuration](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/config.json)
- [Qwen3.5-9B card and lineage metadata](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/README.md)
- [Qwen3.5-9B-Base original model card](https://huggingface.co/Qwen/Qwen3.5-9B-Base)
- [flux-3-image-klein-pup original model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup)
