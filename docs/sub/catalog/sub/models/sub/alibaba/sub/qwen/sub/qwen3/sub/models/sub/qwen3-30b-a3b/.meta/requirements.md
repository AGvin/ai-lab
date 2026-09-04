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

## Validation

- Total and active parameter counts are shown separately.
- The page does not imply that 3.3B active parameters make the model equivalent to a 3.3B dense model.
- Version-specific facts are not silently generalized to all Qwen3 30B-A3B releases.
- Selection and deployment conclusions are not presented as intrinsic model facts.
