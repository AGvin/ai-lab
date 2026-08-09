# Documentation Requirements

## Requirements

- Identify Qwen3 14B as a concrete dense model in the Qwen3 generation.
- Preserve concrete-model facts from the legacy Qwen3 14B page that describe the model itself.
- Preserve official artifact identity and published size when useful for distinguishing the documented release from its downloadable representation.
- Keep model-selection, hardware-fit, orchestration suitability, and workload-specific conclusions outside the canonical model profile unless a future architecture decision assigns them here.

## Content Specification

- Use `Qwen3 14B` as the page title.
- Link the canonical Qwen3 family page.
- State that this is a dense causal language model.
- Preserve the documented 14.8B total parameter count and 13.2B non-embedding parameter count.
- Preserve the documented 40-layer architecture.
- Preserve the documented 32,768-token native context and official YaRN extension guidance to 131,072 tokens.
- Preserve the Apache-2.0 license and pretraining-plus-post-training stage.
- Present thinking and non-thinking modes, multilingual instruction following, translation, reasoning, coding, and tool-integrated agent capabilities as provider-described capabilities rather than AI Lab evaluation results.
- Preserve the official `Qwen/Qwen3-14B` model page as an identification and research reference.
- Preserve the official `Qwen/Qwen3-14B-GGUF` artifact repository and the legacy page's published size of approximately 9 GB for the `Q4_K_M` artifact used in the prior portfolio context.
- State clearly that published artifact size is not peak VRAM or total runtime memory.

## Excluded Residual Content

The following legacy content remains useful but is not owned by the canonical Qwen3 14B model page:

- recommendations for 16–24 GB VRAM systems;
- resident-local-generalist and hybrid-system recommendations;
- orchestration, routing, coding-assistance, automation, and escalation suitability conclusions;
- comparative planning inference that Qwen3 14B offers more 24 GB headroom than the Qwen3 30B-A3B `Q4_K_M` artifact;
- deployment-fit, reliability, frontier-status, ecosystem-status, and accepted-result-cost conclusions that require separate dated evidence.

Preserve these residuals for future decision-support, deployment/workflow, or evidence ownership until those domains are designed.

## Validation

- The page does not treat the GGUF artifact as a separate base-model identity.
- The page does not equate published file size with VRAM requirements.
- Provider-described capabilities are not presented as independently benchmarked AI Lab results.
- Hardware, orchestration, and hybrid-routing recommendations are not presented as intrinsic model facts.
- Internal links resolve to canonical nodes.
