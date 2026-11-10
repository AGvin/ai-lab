# Documentation Requirements

## Requirements

- Identify `Qwen/Qwen3-Coder-30B-A3B-Instruct` as a concrete model in the Qwen3-Coder series.
- Preserve current source-backed MoE architecture, 30.5B total / 3.3B active parameters, 48 layers, 32 query / 4 key-value heads, 128 total / 8 active experts, 262,144-token native context, YaRN extension guidance up to 1M tokens, non-thinking-only mode, pretraining/post-training stage, and Apache-2.0 license.
- Keep provider agentic-coding/browser/tool-use claims distinguishable from independent AI Lab evaluation.
- Preserve the semantic boundary that active parameters are not total storage/memory or dense-model equivalence.
- Note its role as the documented base model for reviewed derivatives without copying derivative modification facts into the base profile.
- Keep runtime, quantization, hardware fit, hosted state, and selection conclusions outside canonical model identity.

## Decision and Operational Boundaries

- Qwen3-Coder-30B-A3B-Instruct is an Apache-2.0, text-only, non-thinking coding model with 30.5B total and 3.3B active parameters.
- Keep the 262,144-token native context distinct from optional extensions and service quotas; preserve the exact checkpoint's non-thinking-only contract.
- Active parameter count does not establish model storage or peak serving memory.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.
- Retain derivative lineage separately; a downstream abliterated model's modifications or safety behavior are not properties of this original checkpoint.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The model remains distinct from Qwen3-Coder 480B-A35B Instruct and Qwen3-Coder-Next.
- 3.3B active parameters are not presented as total model scale or VRAM.
- Provider capability claims are not presented as independent benchmark evidence.
- Derivative refusal/alignment modifications are not attributed to the base model.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
