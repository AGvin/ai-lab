# Supervised Fine-Tuning

Supervised Fine-Tuning, or SFT, trains a model on examples that pair an input or instruction with a desired output.

## Core idea

The model learns to assign higher probability to target responses supplied in the dataset. For chat models, examples usually include roles, instructions, context, and assistant answers formatted with the model's chat template.

## Practical use

- Convert a base model into an instruction-following model.
- Teach task-specific formats and terminology.
- Improve behavior on curated domain examples.
- Prepare a model before preference optimization.

## Dataset requirements

High-quality, diverse examples are more valuable than large volumes of repetitive text. Include realistic failures, edge cases, and desired uncertainty behavior. Remove secrets, accidental personal data, and incorrect synthetic answers.

## Trade-offs and limitations

SFT teaches imitation of examples, not independent factual verification. It can overfit style, memorize examples, or reduce performance outside the training distribution. The model may also learn undesirable patterns hidden in seemingly correct answers.

## Common mistakes

- Training on raw documents instead of instruction-response examples for an instruction task.
- Using generated answers without validation.
- Mixing incompatible chat templates.
- Evaluating on near-duplicates of training data.

## Related concepts

- [Training and Adaptation](../../)
- [Instruction Tuning](../instruction-tuning/)
- [Datasets](../datasets/)
- [Preference Optimization](../preference-optimization/)
