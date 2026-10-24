# ShieldGemma 2

Gemma 3 4B instruction-checkpoint-derived image-safety classifier; ShieldGemma 2 returns policy-specific safety scores rather than general conversational answers.

## Relations

- Member of: [Gemma](../../)

## Source-scoped operating boundaries

- The model evaluates natural and synthetic images against sexually explicit, dangerous, and violent content policies. Outputs include Yes/No probabilities for the supplied policy, enabling threshold calibration rather than providing a universal binary safety certificate. [Policy and output definition](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2).
- Evaluate false positives and false negatives for the actual image domain and policy. A classifier score does not cover untested harm categories, bypasses, application permissions, or legal compliance. [Model evaluation and limitations](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2).

## Official resources

- <https://deepmind.google/models/gemma/shieldgemma-2/>
- <https://ai.google.dev/gemma/docs/releases>
- <https://ai.google.dev/gemma/docs/shieldgemma/model_card_2>
