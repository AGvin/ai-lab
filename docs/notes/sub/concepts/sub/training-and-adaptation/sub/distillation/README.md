# Distillation

<!--
ai_content:
  managed: true
  l10n: true
-->

Distillation trains a smaller or simpler student model to reproduce useful behavior from a stronger teacher model.

## Core idea

The teacher may provide probability distributions, generated answers, reasoning examples, labels, or synthetic tasks. The student learns from these signals and may retain part of the teacher's capability at lower inference cost.

## Practical use

- Create smaller models for local or edge deployment.
- Transfer task behavior from an expensive model.
- Generate training labels where human annotation is limited.
- Specialize a compact model for a narrow workflow.

## Trade-offs and limitations

The student also inherits teacher errors and biases. Distillation cannot preserve every capability when model capacity is reduced. Generated training data may violate provider terms or model licenses, so provenance and usage rights matter.

## Common mistakes

- Evaluating only on teacher-generated examples.
- Treating the teacher as ground truth.
- Ignoring data contamination and licensing.
- Expecting a much smaller student to match every teacher capability.

## Related concepts

- [Training and Adaptation](../../)
- [Synthetic Data](../synthetic-data/)
- [Model Selection](../../../evaluation-and-operations/sub/model-selection/)
- [Quantization](../../../inference-and-serving/sub/quantization/)
