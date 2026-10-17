# Documentation Requirements

## Requirements

- Identify Qwen3-VL-235B-A22B-Instruct as the released MoE instruction model exposed by the current Qwen3-VL series and Alibaba Cloud Model Studio.
- Preserve text/image/video input and text output, visual understanding, OCR/spatial reasoning, and current tool/structured-output capabilities only while supported by first-party documentation.
- Keep total-parameter and active-parameter accounting distinct; do not interpret active parameters as checkpoint size, memory footprint, or universal compute requirement.
- Treat context limits, video limits, serving aliases/snapshots, regions, pricing, rate limits, fine-tuning, quantization, and runtime/backend support as freshness-sensitive.
- Keep the concrete model distinct from the Qwen3-VL series, dense Qwen3-VL siblings, and the Model Studio hosting service.
- Attribute benchmark and comparative performance claims to Qwen Team or the cited evaluator.

## Validation

- The node is one concrete MoE model identity within Qwen3-VL.
- Active-parameter counts are not used as a hardware-fit shortcut.
- Hosted serving properties remain separate from intrinsic model identity.
