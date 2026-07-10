# GPU Offloading

<!--
ai_content:
  managed: true
  l10n: true
-->

GPU offloading places some or all model computation and weights on a GPU while the remaining work stays on the CPU or another device.

## Core idea

When a model does not fit entirely in VRAM, runtimes may place selected layers on the GPU and keep the rest in system memory. More GPU-resident layers usually improve speed, but transfers and synchronization can reduce the benefit when the split is poorly chosen.

## Practical use

- Run models larger than available VRAM.
- Balance model weights against KV-cache and batch memory.
- Use integrated GPUs or unified-memory systems efficiently.
- Compare full GPU, partial GPU, and CPU-only configurations.

## Design considerations

Reserve VRAM for context, runtime buffers, and concurrent requests. Monitor actual allocation rather than trusting a configured layer count. PCIe bandwidth, memory bandwidth, and CPU performance all influence partial-offload speed.

## Trade-offs and limitations

Partial offloading may be much slower than full GPU residency. Some layers or operations cannot be split efficiently. Unified-memory systems remove explicit transfer boundaries but still face bandwidth and capacity limits.

## Common mistakes

- Filling VRAM with weights and leaving no room for the KV cache.
- Assuming more offloaded layers always improve performance.
- Comparing systems without matching context and batch size.
- Ignoring thermal throttling and sustained power limits.

## Related concepts

- [Inference and Serving](../../)
- [GPU Inference](../gpu-inference/)
- [CPU Inference](../cpu-inference/)
- [KV Cache](../kv-cache/)
