# Pruning

Pruning removes model weights, neurons, attention heads, layers, or other structures judged unnecessary for a target objective.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Unstructured pruning sets individual weights to zero, while structured pruning removes larger units that hardware and runtimes can exploit more easily. Pruned models are often fine-tuned afterward to recover quality.

## Practical use

- Reduce model size or computation.
- Study which components contribute to a task.
- Create hardware-friendly smaller architectures.
- Combine with quantization or distillation.

## Trade-offs and limitations

Sparse weights do not guarantee speedup unless the runtime and hardware support the sparsity pattern. Aggressive pruning can damage general capabilities or create task-specific brittleness. Retraining and evaluation may cost more than selecting an existing smaller model.

## Common mistakes

- Reporting zero weights as practical acceleration.
- Pruning without measuring quality on diverse tasks.
- Assuming every layer contributes equally.
- Ignoring runtime support for structured or unstructured sparsity.

## Related concepts

- [Training and Adaptation](../../)
- [Dense and Sparse Models](../../../foundations-and-architecture/sub/dense-and-sparse-models/)
- [Distillation](../distillation/)
- [Quantization](../../../inference-and-serving/sub/quantization/)
