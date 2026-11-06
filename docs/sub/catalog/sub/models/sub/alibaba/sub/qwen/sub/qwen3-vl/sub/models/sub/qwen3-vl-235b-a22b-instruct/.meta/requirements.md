# Documentation Requirements

## Requirements

- Identify Qwen3-VL-235B-A22B-Instruct as the released MoE instruction model exposed by the current Qwen3-VL series and Alibaba Cloud Model Studio.
- Preserve text/image/video input and text output, visual understanding, OCR/spatial reasoning, and current tool/structured-output capabilities only while supported by first-party documentation.
- Keep total-parameter and active-parameter accounting distinct; do not interpret active parameters as checkpoint size, memory footprint, or universal compute requirement.
- Treat context limits, video limits, serving aliases/snapshots, regions, pricing, rate limits, fine-tuning, quantization, and runtime/backend support as freshness-sensitive.
- Keep the concrete model distinct from the Qwen3-VL series, dense Qwen3-VL siblings, and the Model Studio hosting service.
- Attribute benchmark and comparative performance claims to Qwen Team or the cited evaluator.

## Decision and Operational Boundaries

- Qwen3-VL-235B-A22B-Instruct has official Apache-2.0 open weights for text/image/video understanding and text generation.
- Keep native 256K context separate from extension to 1M and from hosted-region budgets; image/video preprocessing also consumes model context.
- Keep this Instruct checkpoint distinct from a Thinking sibling and from image/video generation or embedding models.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Visual agent capability does not authorize clicking, shell execution, or disclosure of image/document contents.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node is one concrete MoE model identity within Qwen3-VL.
- Active-parameter counts are not used as a hardware-fit shortcut.
- Hosted serving properties remain separate from intrinsic model identity.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
