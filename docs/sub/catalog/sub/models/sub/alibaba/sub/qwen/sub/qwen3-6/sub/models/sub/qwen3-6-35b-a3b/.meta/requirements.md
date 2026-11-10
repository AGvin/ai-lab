# Documentation Requirements

## Requirements

- Identify Qwen3.6-35B-A3B using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-6/models/qwen3-6-35b-a3b`.
- Preserve canonical membership in `catalog/models/alibaba/qwen/qwen3-6` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Qwen3.6-35B-A3B is a released Apache-2.0 35B total/3B active MoE vision-language checkpoint for text, image, and video understanding with text output.
- Preserve 262,144-token native context and the separately documented extension to 1,010,000; thinking is on by default and can be disabled through the appropriate API/template setting.
- History-preservation and runtime-specific reasoning controls are configuration options; do not copy hosted behavior into every local runtime.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
