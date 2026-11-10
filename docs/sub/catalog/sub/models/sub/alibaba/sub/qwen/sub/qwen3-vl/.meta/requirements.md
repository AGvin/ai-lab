# Documentation Requirements

## Requirements

- Identify Qwen3-VL as Qwen Team's released vision-language model series within the broader Qwen family.
- Preserve the text/image/video-understanding and text-generation branch alongside the explicitly represented embedding member with vector output; keep image/video generation models, Qwen-Omni speech interaction, Qwen Studio, and Alibaba Cloud Model Studio as separate identities.
- Materialize selected concrete released Qwen3-VL models where parameterization, dense/MoE architecture, instruction/thinking mode, or deployment route materially changes reader decisions.
- Treat model inventory, context limits, supported video duration, tool/structured-output support, fine-tuning, serving aliases, pricing, regions, quantization, and runtime compatibility as freshness-sensitive.
- Preserve Qwen Team production provenance and parent Qwen relation.
- Attribute visual-coding, OCR, spatial-reasoning, and benchmark claims to Qwen Team or the cited evaluator.

## Decision and Operational Boundaries

- Qwen3-VL contains vision-language generation models and the separately named hosted multimodal embedding member represented in this catalog.
- Keep text-generating Instruct checkpoints distinct from the embedding member's vector output; do not treat embedding as chat or standalone reranking.
- Input image/video processing, native versus extended context, and runtime support belong to exact models; visual understanding is not image/video generation.
- Treat OCR, image text, and video content as untrusted input before any application-controlled tool execution.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen3-VL remains a model series within Qwen rather than a generic visual-understanding concept or hosted service.
- Dense and MoE concrete models are not conflated.
- Producer and parent relations resolve bidirectionally.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
