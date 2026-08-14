# Documentation Requirements

## Requirements

- Identify Qwen2.5-Coder 3B Instruct as a concrete instruction-tuned coding model in the Qwen2.5-Coder series.
- Preserve concrete-model facts that describe the model itself.
- Keep contextual scale classification, local-baseline recommendations, autonomous-coding suitability, hardware fit, and accepted-result conclusions outside the canonical model profile.

## Content Specification

- Use `Qwen2.5-Coder 3B Instruct` as the page title.
- Link the canonical Qwen2.5-Coder series.
- Describe the model as a coding-specialized instruction-tuned language model using a dense decoder-only Transformer architecture.
- Preserve 3.09B total parameters and 2.77B parameters excluding embeddings.
- Preserve 36 layers and distinguish configured/default context from extended context: the official shipped config sets `max_position_embeddings` to 32,768, while the official model card documents extension to 131,072 tokens with YaRN using factor 4 and `original_max_position_embeddings: 32768`.
- Preserve pretraining and post-training as the documented training stages.
- Preserve the Qwen Research License and text-input/text-output modality description from the official model card.
- Include the official `Qwen/Qwen2.5-Coder-3B-Instruct` model page.

## Excluded Residual Content

Preserve outside this canonical model profile:

- the contextual AI Lab `SLM` classification;
- recommendations for economical local coding baselines, bounded edits, test drafts, repetitive transformations, private/offline use, or constrained hardware;
- escalation guidance for repository-scale reasoning, architecture work, long tool sequences, high-risk changes, or repeated omissions;
- deployment assumptions about runtime, quantization, prompt templates, context, and hardware beyond the model-card-backed configured/extended context distinction;
- coding-quality, throughput, frontier-status, ecosystem-status, hardware-fit, and accepted-result-cost conclusions requiring separate evidence.

## Validation

- Contextual classification and recommendation language is not presented as intrinsic model identity.
- The model page does not claim autonomous-coding suitability from parameter count alone.
- Officially sourced model facts remain distinct from AI Lab evaluation conclusions.
- 131,072 tokens is not presented as the shipped/default/configured context; it is identified as an optional YaRN extension from the 32,768-token configured context.
- Internal links resolve to canonical nodes.
