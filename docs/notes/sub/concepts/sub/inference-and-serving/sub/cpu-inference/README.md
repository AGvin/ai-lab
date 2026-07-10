# CPU Inference

<!--
ai_content:
  managed: true
  l10n: true
-->

CPU inference runs most model computation on general-purpose processor cores and system memory.

## Core idea

Large language-model inference is often limited by memory bandwidth rather than only arithmetic throughput. CPUs can run quantized models efficiently enough for development, low-volume services, embeddings, or devices without suitable GPUs. Vector instruction support and memory-channel bandwidth strongly affect performance.

## Practical use

- Run local models on hardware without a discrete GPU.
- Serve low-concurrency workloads with large system RAM.
- Execute small embedding, classification, or reranking models.
- Use CPU layers alongside partial GPU offloading.

## Design considerations

Match thread count to physical cores and runtime behavior. Excessive threads can create contention. Use fast memory, appropriate NUMA placement on multi-socket systems, and optimized kernels for the processor architecture.

## Trade-offs and limitations

CPU inference usually has lower generation throughput than a capable GPU, but system RAM can hold larger models at lower cost. High utilization may affect other workloads and increase power consumption.

## Common mistakes

- Assuming more threads always improve speed.
- Comparing laptop burst performance with sustained server operation.
- Ignoring memory bandwidth and NUMA topology.
- Using an unoptimized generic build without vector extensions.

## Related concepts

- [Inference and Serving](../../)
- [GPU Inference](../gpu-inference/)
- [GPU Offloading](../gpu-offloading/)
- [Quantization](../quantization/)
