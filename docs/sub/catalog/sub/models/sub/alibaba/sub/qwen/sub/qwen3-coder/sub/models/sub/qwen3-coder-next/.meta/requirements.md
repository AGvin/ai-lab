# Documentation Requirements

## Requirements

- Identify Qwen3-Coder-Next as a concrete open-weight coding-agent model in the Qwen3-Coder series.
- Preserve intrinsic model facts from the current official profile.
- Keep runtime deployment instructions, hardware fit, contextual classifications, and workload-quality conclusions outside the canonical model profile.

## Content Specification

- Use `Qwen3-Coder-Next` as the page title.
- Link the canonical Qwen3-Coder series.
- Describe the model as a causal language model using hybrid Gated DeltaNet, gated attention, and Mixture of Experts architecture.
- Preserve 80B total parameters, 3B active parameters, 262,144-token native context, Apache-2.0 licensing, and non-thinking-only mode.
- Preserve the official model page and technical report.
- State that 3B active parameters do not represent total storage, RAM, VRAM, or dense-model equivalence.
- Present coding-agent, long-horizon coding, complex tool-use, and execution-recovery suitability as provider-described intent rather than independently validated AI Lab quality.

## Decision and Operational Boundaries

- Qwen3-Coder-Next is an Apache-2.0, text-only, non-thinking coding model with 80B total and 3B active parameters.
- Keep the 262,144-token native context distinct from optional extensions and service quotas; preserve the exact checkpoint's non-thinking-only contract.
- Active parameter count does not establish model storage or peak serving memory.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- 80B total and 3B active parameter counts remain distinct.
- The page does not treat the model as equivalent to a 3B dense model.
- Provider intent is not presented as benchmarked AI Lab evidence.
- Runtime and hardware guidance is not presented as intrinsic model identity.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
