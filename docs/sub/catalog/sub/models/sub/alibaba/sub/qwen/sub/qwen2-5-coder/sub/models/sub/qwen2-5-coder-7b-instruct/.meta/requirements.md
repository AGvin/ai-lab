# Documentation Requirements

## Requirements

- Identify Qwen2.5-Coder 7B Instruct as a concrete instruction-tuned coding model in the Qwen2.5-Coder series.
- Preserve concrete-model facts that describe the model itself.
- Keep contextual scale classification, local/self-hosted suitability, autonomous-coding claims, hardware fit, and accepted-result conclusions outside the canonical model profile.

## Content Specification

- Use `Qwen2.5-Coder 7B Instruct` as the page title.
- Link the canonical Qwen2.5-Coder series.
- Describe the model as a coding-specialized instruction-tuned language model using a dense decoder-only Transformer architecture.
- Preserve 7.61B total parameters and 6.53B parameters excluding embeddings.
- Preserve 28 layers and a 131,072-token context length.
- Preserve pretraining and post-training as the documented training stages.
- Preserve the Apache-2.0 license and text-input/text-output modality description from the official model card.
- Include the official `Qwen/Qwen2.5-Coder-7B-Instruct` model page.

## Excluded Residual Content

Preserve outside this canonical model profile:

- the contextual AI Lab `SLM` classification and the description of this model as a stronger compact local route;
- recommendations for bounded multi-file edits, debugging, tests, documentation, or local/self-hosted coding assistance;
- claims that stronger quality justifies additional memory or latency;
- warnings and validation guidance around autonomous repository work, instruction retention, tool use, regressions, framework-specific behavior, and final-diff quality;
- coding-quality, throughput, frontier-status, ecosystem-status, hardware-fit, and accepted-result-cost conclusions requiring separate evidence.

## Validation

- Contextual classification and recommendation language is not presented as intrinsic model identity.
- The page does not infer autonomous repository-work reliability from model size or provider benchmarks.
- Officially sourced model facts remain distinct from AI Lab evaluation conclusions.
- Internal links resolve to canonical nodes.
