# Documentation Requirements

## Requirements

- Use the reader-facing title `Dense and Sparse Architectures`.
- Scope `dense` and `sparse` here to parameterized computation and activation: dense computation broadly reuses the same relevant parameterized subnetwork for each input, while sparse or conditional computation selects only a subset of available parameterized components for a particular input or token.
- Make clear that this activation-oriented meaning of sparsity is not a synonym for every other use of `sparse`, including sparse tensors, zero-valued weights, or pruning-induced weight sparsity.
- Present Mixture of Experts as an important sparse/conditional-computation architecture but not as a synonym for the whole sparse category.
- Distinguish total parameters from parameters active on a particular computation path. Treat the former as total learned capacity/storage state and the latter as one contributor to per-input arithmetic work; neither metric alone determines end-to-end memory use, latency, throughput, or quality.
- Explain that inactive parameters may still need storage or placement and that actual residency depends on the runtime, device placement, offloading, expert layout, and serving strategy.
- Explain that sparse activation can reduce arithmetic work relative to activating all available components, while routing, dispatch, load balancing, irregular memory access, synchronization, and inter-device communication can materially change realized performance.
- Keep quantization, pruning, distillation, language-model scale, frontier status, and deployment mode as separate dimensions or techniques even when they interact operationally with dense or sparse architectures.
- Keep concrete runtime compatibility, hardware-fit conclusions, model-selection fields, and benchmark outcomes with their applicable catalog, evidence, or decision owners.
- Use the canonical entity references as research inputs when rendering comparative claims about conditional computation or sparse activation.

## Validation

- The page does not use `sparse` as an unqualified synonym for MoE, pruning, quantization, or small model size.
- The page does not assume total parameter count equals per-token computation for sparse architectures.
- The page does not treat active parameter count as a complete storage, RAM, VRAM, latency, throughput, or quality requirement.
- The page does not promise proportional speed or cost reductions from lower active parameter counts.
- Dense and sparse architecture labels remain conceptually independent from scale, frontier position, deployment, and model-selection suitability.
- The legacy operational/model-selection field recommendations are not duplicated into this canonical concept owner.
