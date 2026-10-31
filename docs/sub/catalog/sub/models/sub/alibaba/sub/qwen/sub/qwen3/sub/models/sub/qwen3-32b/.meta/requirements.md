# Documentation Requirements

## Requirements

- Identify Qwen3 32B as a concrete dense model in the Qwen3 series.
- Preserve current source-backed architecture, parameter, layer, attention, context, license, and training-stage facts.
- Keep provider capability claims distinguishable from independent AI Lab evaluation.
- Keep deployment, hardware, artifact, and task-selection conclusions outside the canonical model profile.

## Content Specification

- Use `Qwen3 32B` as the page title and link the Qwen3 series.
- Identify the exact `Qwen/Qwen3-32B` repository.
- Preserve 32.8B total and 31.2B non-embedding parameters, 64 layers, 64 query / 8 key-value attention heads, 32,768-token native context, YaRN extension guidance to 131,072 tokens, Apache-2.0 licensing, and pretraining-plus-post-training stage.
- Treat reasoning/coding/multilingual/tool-use statements as provider-described capabilities rather than workload acceptance evidence.

## Decision and Operational Boundaries

- Qwen3-32B is an Apache-2.0 dense text model with 32.8B total parameters and an initial hybrid-thinking interaction contract.
- Preserve the card's 32,768-token native context and separate 131,072-token YaRN extension; context scaling and memory requirements depend on the selected runtime.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- No facts are inferred from neighboring Qwen3 models when the Qwen3-32B card provides direct evidence.
- Provider capability claims are not presented as independent AI Lab benchmark results.
- The page contains no obsolete migration-placeholder or missing-source wording.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
