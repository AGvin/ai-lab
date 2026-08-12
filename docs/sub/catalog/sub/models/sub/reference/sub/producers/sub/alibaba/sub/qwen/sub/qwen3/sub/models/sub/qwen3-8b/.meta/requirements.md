# Documentation Requirements

## Requirements

- Identify Qwen3 8B as a concrete dense model in the Qwen3 series.
- Preserve concrete-model facts that describe the model itself.
- Preserve official artifact identity and published size when useful for distinguishing the documented model from a downloadable representation.
- Keep model-selection, hardware-fit, agent-role suitability, and workload-specific conclusions outside the canonical model profile.

## Content Specification

- Use `Qwen3 8B` as the page title.
- Link the canonical Qwen3 series page.
- State that this is a dense causal language model.
- Preserve 8.2B total parameters and 6.95B non-embedding parameters.
- Preserve 36 layers, 32,768-token native context, YaRN extension guidance to 131,072 tokens, Apache-2.0 licensing, and pretraining-plus-post-training stage.
- Present provider capability claims as provider-described capabilities rather than AI Lab evaluation results.
- Preserve the official model and GGUF references and the documented `Q4_K_M` file size where retained.
- State clearly that published artifact size is not peak VRAM or total runtime memory.

## Validation

- The page does not treat the GGUF artifact as a separate base-model identity.
- The page does not equate published file size with VRAM requirements.
- Provider-described capabilities are not presented as independently benchmarked AI Lab results.
- Hardware and role recommendations are not presented as intrinsic model facts.
