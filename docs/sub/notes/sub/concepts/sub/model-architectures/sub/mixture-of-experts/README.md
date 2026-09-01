# Mixture of Experts

Legacy residual retained for MoE deployment interpretation and model-documentation guidance that is intentionally outside the canonical architecture concept owner.

> **Migration note:** MoE definition, expert/router roles, routing-policy variability, conditional capacity, total-versus-active parameter semantics, storage/placement caveats, load balancing, communication overhead, and related conceptual mistakes are already preserved in `docs/sub/concepts/sub/models/sub/architectures/sub/dense-and-sparse-architectures/sub/mixture-of-experts/`. The remaining material below stays here until its exact model-reference, hardware-fit, runtime-support, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Deployment and runtime residual

Efficient MoE inference depends on runtime support for routing, expert dispatch, batching, memory placement, and output combination. A runtime that can load an MoE model may still execute it inefficiently.

For multi-device deployment, experts may be distributed across GPUs or nodes. Token dispatch can introduce communication overhead, synchronization cost, and uneven device utilization; interconnect bandwidth and expert placement can therefore materially affect hardware fit.

For local inference, all required weights still need viable storage or placement and the runtime must implement the architecture efficiently. Active parameter count alone is not a RAM/VRAM requirement. CPU offloading or split placement may make a model loadable while still producing poor latency.

Batch size and routing balance can also change realized performance. Large batches may improve expert utilization, while small interactive batches can expose routing overhead and uneven routing can overload popular experts.

These deployment/runtime interpretations remain migration source material until their exact existing catalog, hardware-selection, or runtime-support owner is verified.

## Model-documentation residual

When MoE architecture materially affects comparison or selection, the legacy documentation recorded reliable fields separately:

```text
Architecture: Sparse — MoE
Total parameters: <value or Unknown>
Active parameters: <value or Unknown>
Experts: <count or Unknown>
Experts selected per token: <value or Unknown>
Shared experts: <value or Not documented>
Runtime notes: <relevant support or placement constraints>
```

Do not derive undocumented values from naming conventions or divide total parameters by expert count without an authoritative architecture description.

These field recommendations are intentionally not part of the canonical MoE concept. Keep them here until the applicable model-reference or model-selection contract explicitly owns their representation.
