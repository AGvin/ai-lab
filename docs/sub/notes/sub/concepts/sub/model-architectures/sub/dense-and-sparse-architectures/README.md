# Dense and Sparse Architectures

Legacy residual retained for model-documentation and deployment-selection guidance that is intentionally outside the canonical architecture concept owner.

> **Migration note:** Dense/sparse definitions, conditional activation, total-versus-active parameter semantics, memory-residency caveats, routing/dispatch overhead, adjacent-technique boundaries, and the associated conceptual mistakes are already preserved in `docs/sub/concepts/sub/models/sub/architectures/sub/dense-and-sparse-architectures/`. The remaining material below stays here until its exact model-reference, hardware-fit, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Deployment and selection residual

For local inference, dense models are often simpler to estimate and place on one device. Sparse models can still work well locally when the runtime supports their routing/expert layout and the complete weight set can be stored or otherwise placed appropriately. Active parameter count alone is not a local-hardware requirement and must not be treated as proof that a sparse model fits the same device as a dense model with a similar active count.

For multi-device serving, expert placement, inter-device communication, load imbalance, batch size, and interconnect performance can materially change realized latency and throughput. A lower active-parameter count therefore does not by itself establish a hardware-fit or serving-performance conclusion.

These deployment interpretations remain migration source material until their exact existing hardware/model-selection owner is verified.

## Model-documentation residual

When dense/sparse architecture materially affects model comparison or selection, the legacy documentation used the following compact fields:

```text
Architecture: Dense | Sparse — MoE | Other sparse | Unknown
Total parameters: <value or Unknown>
Active parameters: <value, Not applicable, or Unknown>
Routing: <top-k or other reliable detail when relevant>
```

Do not estimate active parameters by dividing total parameters by the number of experts unless authoritative architecture documentation explicitly supports that calculation.

These field recommendations are intentionally not part of the canonical architecture concept. Keep them here until the applicable model-reference or model-selection contract explicitly owns their representation.
