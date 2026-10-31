# Documentation Requirements

## Requirements

- Identify ShieldGemma 2 as Google's released open safety-classifier model for evaluating text/image content against defined safety policies.
- Preserve the current 4B image-safety model boundary and tuneable/open-model positioning only while supported by current first-party documentation.
- Keep ShieldGemma 2 distinct from ShieldGemma 1, general-purpose Gemma models, moderation APIs, safety policies, guardrail frameworks, and complete application-safety systems.
- Treat policy taxonomy, input modalities, artifacts, licenses, fine-tuning, runtime support, threshold/calibration guidance, benchmark results, and known limitations as freshness-sensitive.
- Do not imply that a favorable ShieldGemma classification guarantees policy compliance, application safety, regulatory compliance, or protection outside the evaluated policy/domain.

## Validation

- The node remains a concrete classifier model rather than a generic safety framework.
- Safety claims remain scoped to defined policies, model revision, calibration, and evaluated data.

## Verified identity and provenance

Gemma 3 4B instruction-checkpoint-derived image-safety classifier; ShieldGemma 2 returns policy-specific safety scores rather than general conversational answers.

## Source-scoped operating boundaries

- The model evaluates natural and synthetic images against sexually explicit, dangerous, and violent content policies. Outputs include Yes/No probabilities for the supplied policy, enabling threshold calibration rather than providing a universal binary safety certificate. [Policy and output definition](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2).
- Evaluate false positives and false negatives for the actual image domain and policy. A classifier score does not cover untested harm categories, bypasses, application permissions, or legal compliance. [Model evaluation and limitations](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2).

## Source evidence

- <https://ai.google.dev/gemma/docs/shieldgemma/model_card_2>
- <https://deepmind.google/models/gemma/shieldgemma-2/>
