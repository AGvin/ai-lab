# Documentation Requirements

## Requirements

- Identify Qwen3.8-Flash-Next as a separately released Qwen3.8 foundation-model identity published on 2026-08-26 with its own first-party repository and weights.
- Preserve its own source-backed model facts rather than inheriting parameter or deployment claims from other Qwen3.8 siblings.
- Keep quantizations, provider routes, runtime packaging, benchmark state, and deployment recommendations outside intrinsic model identity unless separately materialized.

## Decision and Operational Boundaries

- Qwen3.8-Flash-Next has released multimodal weights, but Qwen explicitly describes it as an experimental preview of an architecture intended for Qwen4.
- Use the Qwen Community License 1.0 attached to these weights. Commercial MaaS or AI Work Assistant businesses require a separate license without the 2.4T checkpoint's USD 50 million revenue threshold; observe the limited internal-use exception and attribution conditions.
- Keep 262,144-token native context distinct from extension to 1,000,000 and from hosted Qwen3.8-Flash features.
- Retain this pre-existing preview node for accurate reference; do not treat released preview weights as a stable Qwen4 model release.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen3.8-Flash-Next remains a concrete model within the Qwen3.8 series rather than a serving alias or artifact.
- Sibling model facts are not copied by inference.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
