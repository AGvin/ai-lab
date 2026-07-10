# Overfitting

<!--
ai_content:
  managed: true
  l10n: true
-->

Overfitting occurs when a model learns training examples or noise too specifically and performs worse on new, representative data.

## Core idea

Training loss can continue to improve while validation performance stops improving or declines. In language-model adaptation, overfitting may appear as memorized phrases, repetitive style, reduced general ability, or brittle behavior outside the training format.

## Causes

- Too little or highly repetitive data.
- Excessive training steps or learning rate.
- Data leakage between training and evaluation.
- A model with much more capacity than the task requires.
- Evaluation sets that are too similar to training data.

## Mitigation

Use held-out validation and test sets, early stopping, regularization, data augmentation, and stronger deduplication. Compare against the unchanged base model and evaluate both target and general capabilities.

## Common mistakes

- Using training loss as the only success metric.
- Testing with paraphrases of training examples.
- Assuming PEFT methods cannot overfit.
- Continuing training because loss still decreases.

## Related concepts

- [Training and Adaptation](../../)
- [Fine-Tuning](../fine-tuning/)
- [Datasets](../datasets/)
- [Evals](../../../evaluation-and-operations/sub/evals/)
