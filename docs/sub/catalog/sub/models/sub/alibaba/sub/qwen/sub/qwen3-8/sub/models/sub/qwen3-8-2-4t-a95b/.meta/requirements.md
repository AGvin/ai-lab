# Documentation Requirements

## Requirements

- Identify Qwen3.8-2.4T-A95B as the concrete Qwen3.8 model released on 2026-08-12.
- Preserve the official distinction between approximately 2.4T total parameters and 95B active parameters without inferring unpublished expert-routing details.
- Keep exact artifacts, quantizations, provider routes, benchmark state, and deployment recommendations outside intrinsic model identity unless separately materialized.

## Decision and Operational Boundaries

- Qwen3.8-2.4T-A95B is the released text-only, thinking-only checkpoint with 2.4T total and 95B active parameters.
- Use its Qwen3.8-Max license rather than the repository's Apache badge. Commercial MaaS/AI Work Assistant businesses above USD 50 million aggregate revenue during any consecutive 12 months require a separate license; the limited internal-use exception does not permit third-party access.
- The license also requires prominent model attribution above its specified user/revenue thresholds; consult the exact license before distribution or commercial deployment.
- Keep native 262,144-token context and documented extension to 1,010,000 separate from the hosted Max service's multimodal, non-thinking, and built-in-tool features.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Parameter totals and active parameters remain distinct facts.
- The model is not renamed to `Qwen3.8 Max` solely from comparative or class-positioning language.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
