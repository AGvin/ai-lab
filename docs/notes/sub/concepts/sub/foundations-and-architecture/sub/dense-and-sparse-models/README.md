# Dense and Sparse Models

Dense models activate most model parameters for each input, while sparse models activate only selected parameters or components.

## Core idea

A dense transformer runs every feed-forward block for every token. A sparse architecture such as Mixture of Experts may route each token through a small subset of experts. This allows a high total parameter count without using every parameter for each token.

## Practical implications

- Total parameters describe storage requirements.
- Active parameters better approximate per-token computation.
- Expert routing adds communication and load-balancing requirements.
- Sparse models may require specialized runtime support.

## Trade-offs and limitations

Sparse models can provide more capacity at similar compute, but they are difficult to train and serve efficiently. All expert weights may still need to be stored in memory. Uneven routing can overload some experts while leaving others idle.

## Common mistakes

- Comparing total sparse-model parameters directly with dense active parameters.
- Assuming a large MoE model fits like a dense model with the same active count.
- Ignoring multi-device communication overhead.
- Treating sparsity as equivalent to quantization or pruning.

## Related concepts

- [Foundations and Architecture](../../)
- [Mixture of Experts](../mixture-of-experts/)
- [Quantization](../../../inference-and-serving/sub/quantization/)
- [Pruning](../../../training-and-adaptation/sub/pruning/)
