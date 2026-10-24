# Documentation Requirements

## Requirements

- Identify Qwen3 30B-A3B as a concrete Mixture of Experts (MoE) model in the Qwen3 series.
- Preserve concrete-model facts that describe the model itself.
- Preserve the distinction between total and active parameters and between model identity and downloadable artifacts.
- Keep hardware-fit, model-selection, deployment strategy, and workload-specific conclusions outside the canonical model profile.
- Keep chronological release differences on version nodes rather than flattening them into the base model page.

## Content Specification

- Use `Qwen3 30B-A3B` as the page title.
- Link the canonical Qwen3 series page.
- Preserve the MoE architecture, 30.5B total / 3.3B activated / 29.9B non-embedding parameters, 128 total / 8 active experts, and 48 layers.
- Preserve initial-release 32,768-token native context and YaRN extension guidance to 131,072 tokens only at the correct release scope.
- Preserve Apache-2.0 licensing and pretraining-plus-post-training stage.
- Present provider capability claims as provider-described capabilities rather than AI Lab evaluation results.
- Preserve the official model/GGUF references and retained artifact-size evidence where useful.
- State clearly that active parameters are not total storage or memory and published artifact size is not peak VRAM.
- Link version nodes and keep version-specific behavior, naming, and context changes there.

## Decision and Operational Boundaries

- Qwen3-30B-A3B is an Apache-2.0 MoE model with 30.5B total and 3.3B active parameters.
- Keep initial hybrid-thinking behavior and Instruct-2507 non-thinking behavior on their respective version owners; neither mode nor context is universal across the model's represented releases.
- Active parameters do not describe resident weights, KV cache, total RAM/VRAM, or equivalence to a dense 3B model.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Total and active parameter counts are shown separately.
- The page does not imply that 3.3B active parameters make the model equivalent to a 3.3B dense model.
- Version-specific facts are not silently generalized to all Qwen3 30B-A3B releases.
- Selection and deployment conclusions are not presented as intrinsic model facts.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
