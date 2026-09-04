# Documentation Requirements

## Requirements

- Teach offloading as deliberately placing model weights, layers, tensors, caches, operations, or other runtime state across CPU/host memory, GPU/accelerator memory, multiple devices, or storage-backed/unified-memory mechanisms when full preferred-device residency is unavailable or suboptimal; use the canonical GPU Offloading concept for stable identity/boundaries.
- Define the intended placement state explicitly rather than using `offload` as an ambiguous direction. Record which parts execute/reside on which device/memory domain and distinguish partial placement from full GPU residency and from true multi-GPU parallelism.
- Benchmark CPU-only, full preferred-device execution where feasible, and several partial-placement configurations under the same model/artifact, context, batch, concurrency, and generation/task settings. More accelerator residency does not guarantee monotonic speedup.
- Record the actual placement map when the runtime can split modules, operations, tensors, or caches differently from a nominal layer-count setting.
- Reserve accelerator/device memory for KV/cache state, activations/intermediates, runtime workspaces, graphs/kernels, temporary buffers, outputs, batching/concurrency, and allocator headroom before maximizing weight residency. Measure peak memory at the accepted context/concurrency envelope.
- Use runtime/profiler/log evidence where available to observe host-device transfers, synchronization stalls, CPU fallback, page migration, cache movement, device utilization, and unsupported operations. A configuration that appears accelerator-heavy can still bottleneck on transfers or fallback.
- On unified-memory systems, measure actual residency, bandwidth, pressure, page migration, and contention rather than assuming the lack of explicit copy calls eliminates placement constraints.
- Explain that the best placement depends on CPU capability, accelerator capability, memory bandwidth/capacity, interconnect, transfer frequency, cache placement, runtime scheduling, workload shape, and concurrent activity.
- Measure representative time to first output, prompt/prefill latency, decode/task throughput, end-to-end latency, memory, power/clocks/temperature, and throttling over sustained execution when they matter to the intended workload.
- Keep placement and numerical representation as separate variables. If offloading is combined with quantization or another artifact change, compare accepted-result quality, memory, and performance in a way that does not attribute both effects to placement alone.
- Keep concrete runtime placement syntax, current compatibility, benchmark measurements, hardware topology results, and recommendations with catalog/evidence/decision owners.

## Validation

- Offloading direction/target state is explicit rather than ambiguous.
- More accelerator-resident weights/layers are not assumed to improve performance monotonically.
- Runtime headroom includes workload state rather than only weight residency.
- Transfers, fallback, and unified-memory pressure remain observable performance concerns.
- Offloading and quantization are not conflated as one optimization variable.
