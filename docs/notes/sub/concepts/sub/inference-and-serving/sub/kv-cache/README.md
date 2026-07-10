# KV Cache

The KV cache stores attention keys and values from previously processed tokens so an autoregressive model does not recompute them for every new token.

## Core idea

During generation, each new token attends to earlier tokens. Caching their key and value tensors makes decoding practical, but cache memory grows with context length, batch size, number of layers, attention dimensions, and cache precision.

## Practical use

- Estimate how much context fits after model weights are loaded.
- Choose batch and concurrency limits for a server.
- Evaluate lower-precision cache formats when supported.
- Reuse prompt state through prefix or context caching.

## Trade-offs and limitations

A larger cache enables longer context or more concurrent sessions but consumes significant RAM or VRAM. Quantized caches save memory but may affect quality. Sliding-window and grouped-query attention architectures change cache behavior but do not eliminate it.

## Common mistakes

- Calculating fit from model weights alone.
- Benchmarking short context and deploying long context.
- Assuming the advertised context limit fits on all hardware.
- Confusing persistent context caching with the in-memory KV cache of an active request.

## Related concepts

- [Inference and Serving](../../)
- [Context Window](../../../model-usage-and-generation/sub/context-window/)
- [Context Caching](../context-caching/)
- [GPU Offloading](../gpu-offloading/)
