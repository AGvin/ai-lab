# Model Architectures

Model architecture describes how model computation, components, and parameter activation are organized. Architecture is independent from model scale, deployment mode, access, and capability-frontier status.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Parameter activation

- [`dense-and-sparse-architectures/`](./sub/dense-and-sparse-architectures/) — compares architectures that activate most parameters with architectures that activate selected subsets.
- [`mixture-of-experts/`](./sub/mixture-of-experts/) — explains router-selected expert networks, total parameters, and active parameters.

## Related existing architecture concepts

The broader concept structure is being migrated incrementally. These existing pages remain under the earlier mixed foundations node until their final placement is reviewed:

- [Transformers](../foundations-and-architecture/sub/transformers/)
- [Attention](../foundations-and-architecture/sub/attention/)
- [Self-Attention](../foundations-and-architecture/sub/self-attention/)
- [Encoder-Decoder Architectures](../foundations-and-architecture/sub/encoder-decoder/)
- [Neural Networks](../foundations-and-architecture/sub/neural-networks/)

## Independent dimensions

Architecture labels must not be used as substitutes for other model properties:

- Dense does not mean small, and sparse does not mean large.
- MoE does not automatically mean faster, cheaper, locally practical, or frontier.
- Quantization changes numerical representation, not the model's dense or sparse architecture.
- Pruning can introduce sparsity but is not equivalent to every sparse activation architecture.
- Total parameter count, active parameter count, memory residency, and compute per token should be recorded separately when they affect selection.

## Use in model selection

Use architecture fields when they explain hardware fit, inference behavior, throughput, memory requirements, multi-device communication, or runtime compatibility.

Recommended compact values include:

```text
Architecture: Dense
Architecture: Sparse — MoE
Architecture: Unknown
```

For an MoE model, also record reliable total and active parameter counts separately. Do not compare the model with a dense model using only one of those values.

## Related concepts

- [Model Classification](../model-classification/)
- [Small and Large Language Models](../model-classification/sub/language-model-scale/)
- [Quantization](../inference-and-serving/sub/quantization/)
- [Pruning](../training-and-adaptation/sub/pruning/)
