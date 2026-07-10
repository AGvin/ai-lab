# GPU Inference

<!--
ai_content:
  managed: true
  l10n: true
-->

GPU inference runs model operations on graphics processors designed for highly parallel matrix computation and high-bandwidth device memory.

## Core idea

GPUs can accelerate prompt processing and token generation when the model and runtime use optimized kernels. Available VRAM determines whether weights, the KV cache, batches, and temporary buffers fit without offloading.

## Practical use

- Interactive local language models.
- High-throughput model serving.
- Image, audio, and video generation.
- Embedding and reranking workloads at scale.
- Fine-tuning with supported low-rank methods.

## Design considerations

Evaluate VRAM capacity, memory bandwidth, supported numerical formats, software ecosystem, and power limits. Consumer and data-center GPUs may differ in memory size, reliability features, virtualization, and optimized precision support.

## Trade-offs and limitations

GPUs offer high speed but can be expensive, power-hungry, and constrained by VRAM. A model split across several GPUs may incur communication overhead. Runtime support varies by vendor and architecture.

## Common mistakes

- Selecting a GPU only by compute-core count.
- Ignoring VRAM needed for context and concurrency.
- Assuming every low-precision format is accelerated.
- Comparing peak specifications instead of measured model performance.

## Related concepts

- [Inference and Serving](../../)
- [CPU Inference](../cpu-inference/)
- [GPU Offloading](../gpu-offloading/)
- [Numerical Precision](../numerical-precision/)
