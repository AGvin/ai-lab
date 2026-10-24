# Documentation Requirements

## Requirements

- Identify Qwen3-VL-32B-Instruct as a released dense instruction model in the Qwen3-VL series.
- Preserve text/image/video input and text output plus current visual perception, OCR, spatial-reasoning, tool-use, and structured-output capabilities only while supported by first-party sources.
- Keep its dense architecture and concrete model boundary distinct from the larger MoE Qwen3-VL-235B-A22B-Instruct route.
- Treat context limits, serving aliases, regions, pricing, rate limits, fine-tuning, quantization, runtime support, and benchmark results as freshness-sensitive.
- Attribute comparative performance claims to Qwen Team or the cited evaluator.

## Decision and Operational Boundaries

- Qwen3-VL-32B-Instruct has official Apache-2.0 open weights for text/image/video understanding and text generation.
- Keep native 256K context separate from extension to 1M and from hosted-region budgets; image/video preprocessing also consumes model context.
- Keep this Instruct checkpoint distinct from a Thinking sibling and from image/video generation or embedding models.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Visual agent capability does not authorize clicking, shell execution, or disclosure of image/document contents.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains a concrete dense Qwen3-VL model rather than the series as a whole.
- Hosted API behavior is not generalized into permanent model architecture.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
