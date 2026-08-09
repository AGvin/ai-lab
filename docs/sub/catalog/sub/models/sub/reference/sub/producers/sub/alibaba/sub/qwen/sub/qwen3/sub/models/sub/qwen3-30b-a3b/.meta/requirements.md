# Documentation Requirements

## Requirements

- Identify Qwen3 30B-A3B as a concrete Mixture of Experts (MoE) model in the Qwen3 generation.
- Preserve concrete-model facts from the legacy Qwen3 30B-A3B page that describe the model itself.
- Preserve the distinction between total and active parameters and between model identity and downloadable artifacts.
- Keep hardware-fit, model-selection, deployment strategy, and workload-specific conclusions outside the canonical model profile unless a future architecture decision assigns them here.
- Keep chronological release differences on version nodes rather than flattening them into the base model page.

## Content Specification

- Use `Qwen3 30B-A3B` as the page title.
- Link the canonical Qwen3 family page.
- State that this is a mixture-of-experts causal language model.
- Preserve the documented 30.5B total parameter count, 3.3B active parameters per token, and 29.9B non-embedding parameter count.
- Preserve the documented 128 total experts and 8 active experts per token.
- Preserve the documented 48-layer architecture.
- Preserve the documented 32,768-token native context and official YaRN extension guidance to 131,072 tokens for the initial represented release.
- Preserve the Apache-2.0 license and pretraining-plus-post-training stage.
- Present thinking and non-thinking modes, multilingual work, reasoning, coding, instruction following, and tool-integrated agent capabilities as provider-described capabilities rather than AI Lab evaluation results.
- Preserve the official `Qwen/Qwen3-30B-A3B` model page as an identification and research reference.
- Preserve the official `Qwen/Qwen3-30B-A3B-GGUF` artifact repository and the legacy page's published size of approximately 18.6 GB for the `Q4_K_M` artifact used in the prior portfolio context.
- State clearly that active parameters are not the model's total storage or memory requirement and that published artifact size is not peak VRAM.
- Link the version index and keep version-specific behavior, naming, and context changes on the corresponding version pages.

## Excluded Residual Content

The following legacy content remains useful but is not owned by the canonical Qwen3 30B-A3B model page:

- the planning conclusion that a 24 GB GPU leaves limited nominal headroom for the recorded `Q4_K_M` artifact;
- recommendations for sequential loading, dual-GPU residency, or private-workload selection;
- comparisons against smaller local models or hosted routes;
- claims about measured accepted-result quality, throughput, production fit, frontier status, ecosystem maturity, or cost that require separate evidence;
- deployment guidance about exact runtime, batch size, context, concurrent services, and cache behavior beyond the model-level caveats needed to interpret artifact size.

Preserve these residuals for future decision-support, deployment/workflow, or evidence ownership until those domains are designed.

## Validation

- Total and active parameter counts are shown separately.
- The page does not imply that 3.3B active parameters make the model equivalent to a 3.3B dense model.
- The page does not equate published artifact size with VRAM requirements.
- Provider-described capabilities are not presented as independently benchmarked AI Lab results.
- Version-specific facts are not silently generalized to all Qwen3 30B-A3B releases.
- Internal links resolve to canonical nodes.
