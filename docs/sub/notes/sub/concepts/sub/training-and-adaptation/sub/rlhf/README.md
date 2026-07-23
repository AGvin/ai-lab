# RLHF

Reinforcement Learning from Human Feedback, or RLHF, uses human preference data to train a model toward behavior judged more desirable.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Typical pipeline

1. Supervised fine-tuning creates an instruction-following model.
2. Humans compare or rank candidate responses.
3. A reward model learns to predict those preferences.
4. Reinforcement learning updates the language model to increase predicted reward.

## Core idea

RLHF optimizes model behavior through a learned reward signal rather than direct target-token imitation alone. It has been widely used to improve helpfulness and safety behavior in assistant models.

## Trade-offs and limitations

Reward models are imperfect proxies. The policy may exploit weaknesses in the reward model, become overly cautious, or learn preferred style without improved truthfulness. RLHF is operationally complex and requires careful control of training stability.

## Common mistakes

- Assuming human preference equals factual correctness.
- Using vague annotation criteria.
- Failing to monitor reward hacking and regressions.
- Treating RLHF as necessary for small domain adaptations.

## Related concepts

- [Training and Adaptation](../../)
- [Preference Optimization](../preference-optimization/)
- [DPO](../dpo/)
- [Model Alignment](../../../safety-privacy-and-reliability/sub/model-alignment/)
