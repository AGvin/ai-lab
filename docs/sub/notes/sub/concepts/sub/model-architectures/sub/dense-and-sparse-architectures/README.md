# Dense and Sparse Architectures

Dense and sparse architectures differ in how much of a model's parameterized computation is activated for each token or input.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Dense architectures

A dense model activates most of its core parameterized blocks for each token. In a conventional dense transformer, every token passes through the same sequence of attention and feed-forward layers.

For a dense model, total parameter count and active parameter count are usually close enough that one parameter figure is often used as a practical approximation. This does not mean every stored value contributes equally to every operation.

## Sparse architectures

A sparse architecture activates only selected parameters, components, connections, or blocks for a given token or operation.

Mixture of Experts is the most common model-selection example: a router sends each token through a subset of available expert networks. Other forms of sparsity can exist, so sparse and MoE are not exact synonyms.

## Total and active parameters

| Measure | Meaning | Primary operational relevance |
| --- | --- | --- |
| Total parameters | All parameters stored by the complete model | Artifact size, storage, model loading, and memory residency |
| Active parameters | Parameters used for a token or operation under the activation path | Approximate compute per token and some latency or throughput behavior |

For a dense model, the two counts are often similar. For a sparse model, total parameters can be much larger than active parameters.

Neither figure alone fully predicts performance. Runtime implementation, memory bandwidth, context length, batching, quantization, cache behavior, routing overhead, and device communication can dominate real inference results.

## Practical implications

### Memory

Inactive parameters still normally need to be stored and made available. A sparse model with a small active count does not necessarily fit into the memory required by a dense model of that active size.

### Computation

Activating fewer parameters can reduce arithmetic work per token, but routing, expert dispatch, synchronization, and irregular memory access add overhead.

### Local inference

Dense models are often simpler to estimate and run on one device. Sparse models may work well locally when the runtime has efficient support and all weights fit in RAM or VRAM, but active parameter count alone is not a local-hardware requirement.

### Multi-device serving

Sparse models can require expert placement across devices. Communication and load imbalance can reduce the theoretical compute advantage, especially with small batches or slow interconnects.

## Relationship to adjacent techniques

- **Quantization** reduces numerical precision. It can be applied to dense or sparse models and does not change the activation architecture.
- **Pruning** removes or masks weights or structures. It can produce sparsity, but not every pruned model uses dynamic sparse activation.
- **Distillation** trains a model to imitate another model and does not determine dense or sparse architecture.
- **SLM and LLM** describe relative scale, not activation architecture.
- **Frontier** describes a current capability position, not architecture.

## Use in model documentation

When architecture affects selection, record:

```text
Architecture: Dense | Sparse — MoE | Other sparse | Unknown
Total parameters: <value or Unknown>
Active parameters: <value, Not applicable, or Unknown>
Routing: <top-k or other reliable detail when relevant>
```

Do not estimate active parameters by dividing total parameters by the number of experts unless the architecture documentation explicitly supports that calculation.

## Common mistakes

- Comparing an MoE model's total parameters directly with a dense model's active parameters.
- Assuming inactive experts require no memory.
- Treating every sparse architecture as MoE.
- Treating quantization and sparsity as the same mechanism.
- Assuming fewer active parameters always produce proportionally lower latency.
- Ignoring routing and cross-device communication overhead.

## Related concepts

- [Model Architectures](../../)
- [Mixture of Experts](../mixture-of-experts/)
- [Small and Large Language Models](../../../model-classification/sub/language-model-scale/)
- [Quantization](../../../inference-and-serving/sub/quantization/)
- [Pruning](../../../training-and-adaptation/sub/pruning/)
- [Model Loading](../../../inference-and-serving/sub/model-loading/)
