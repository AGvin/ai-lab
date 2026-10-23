# Documentation Requirements

## Requirements

- Identify Qwen3.8-27B as the concrete 27B-parameter Qwen3.8 model released on 2026-08-14.
- Preserve official model identity and source-backed capabilities without generalizing properties from the much larger Qwen3.8-2.4T-A95B sibling.
- Keep exact artifacts, quantizations, provider routes, benchmark state, and deployment recommendations outside intrinsic model identity unless separately materialized.

- Preserve reciprocal `has-derivative` relations to Cloudflare Clef and to Perplexity's PPLX 27B and PPLX Decider V1, V1.1, and V1.2 checkpoints when their first-party sources explicitly identify Qwen3.8-27B as the base. Do not transfer derivative-specific decision heads, local-agent tuning, output contracts, hosted limits, or licenses to this parent model.

## Decision and Operational Boundaries

- Qwen3.8-27B is the released 27B dense vision-language checkpoint, accepting image/video/text input and generating text under Apache-2.0.
- Its native context is 262,144 tokens; the card distinguishes extension to 1,000,000 tokens from native support and separately discusses hosted features.
- Thinking is on by default and can be disabled; reasoning-depth and history-preservation support must match the runtime.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen3.8-27B remains a distinct concrete model within the Qwen3.8 series.
- Sibling model parameter or deployment facts are not copied here by inference.
- Every materialized `has-derivative` edge is reciprocal and does not reassign producer ownership from the derivative model.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
