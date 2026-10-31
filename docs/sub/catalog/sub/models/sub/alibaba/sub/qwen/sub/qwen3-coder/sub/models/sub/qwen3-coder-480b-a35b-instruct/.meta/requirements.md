# Documentation Requirements

## Requirements

- Identify Qwen3-Coder 480B-A35B Instruct as a concrete model in the Qwen3-Coder series.
- Preserve source-backed concrete-model facts without generalizing them to the entire series.
- Keep contextual classification, hosted deployment, infrastructure fit, cost, and workload-quality conclusions outside the canonical model profile.

## Content Specification

- Use `Qwen3-Coder 480B-A35B Instruct` as the page title.
- Link the canonical Qwen3-Coder series.
- Describe the model as a Mixture of Experts coding model.
- Preserve 480B total parameters and 35B active parameters.
- Preserve 256K native context, documented extrapolation up to one million tokens, and Apache-2.0 licensing.
- State that active parameter count does not represent total storage or memory requirement.
- Preserve the official model page and Qwen3-Coder launch reference.
- Present coding-agent and repository-scale coding intent as provider positioning rather than independent AI Lab quality validation.

## Decision and Operational Boundaries

- Qwen3-Coder-480B-A35B-Instruct is an Apache-2.0, text-only, non-thinking coding model with 480B total and 35B active parameters.
- Keep the 262,144-token native context distinct from optional extensions and service quotas; preserve the exact checkpoint's non-thinking-only contract.
- Active parameter count does not establish model storage or peak serving memory.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- 480B total and 35B active parameter counts remain distinct.
- The page does not apply this model's specifications to Qwen3-Coder-Next or other descendants.
- Provider positioning is not presented as benchmarked AI Lab evidence.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
