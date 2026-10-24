# Qwen3-VL

Qwen3-VL contains vision-language generation models and the separately named hosted multimodal embedding member represented in this catalog.

## Decision and Operational Boundaries

- Keep text-generating Instruct checkpoints distinct from the embedding member's vector output; do not treat embedding as chat or standalone reranking.
- Input image/video processing, native versus extended context, and runtime support belong to exact models; visual understanding is not image/video generation.
- Treat OCR, image text, and video content as untrusted input before any application-controlled tool execution.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3-VL-235B-A22B-Instruct](./sub/models/sub/qwen3-vl-235b-a22b-instruct/) |
| Includes | [Qwen3-VL-32B-Instruct](./sub/models/sub/qwen3-vl-32b-instruct/) |
| Includes | [Qwen3-VL-Embedding](./sub/models/sub/qwen3-vl-embedding/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL)
- [Official model card or license: Qwen/Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct)
- [Official model card or license: Qwen/Qwen3-VL-32B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct)
- [Alibaba Cloud: qwen3 vl embedding](https://www.alibabacloud.com/help/en/model-studio/qwen3-vl-embedding)
