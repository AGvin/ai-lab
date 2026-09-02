# GPU Offloading

Legacy residual retained for placement-sweep benchmarking, VRAM headroom planning, transfer/fallback observability, and sustained thermal/performance evaluation that are intentionally outside the canonical GPU Offloading concept owner.

> **Migration note:** GPU-offloading identity, direction ambiguity, partial-versus-full residency and multi-GPU separation, target-state variability, non-monotonic performance, weight-versus-workload-memory capacity, interconnect/unified-memory boundaries, and loading/quantization distinctions are already preserved in `docs/sub/concepts/sub/models/sub/inference/sub/execution/sub/gpu-offloading/`. The remaining material below stays here until its exact learning, inference-engineering, runtime, performance-evaluation, capacity-planning, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Placement-sweep residual

Benchmark CPU-only, full-GPU where feasible, and several partial-placement configurations under the same model/artifact, context, batch, concurrency, and generation settings. More GPU-resident layers or tensors can improve performance, but the optimum depends on transfer frequency, fallback operations, cache placement, CPU capability, memory bandwidth, and runtime scheduling.

Record the actual placement map rather than only a nominal layer count when the runtime can split modules, operations, caches, or tensors differently.

## VRAM-headroom residual

Reserve device memory for KV/cache state, activations, runtime workspaces, kernels/graphs, temporary buffers, outputs, batching, and concurrent requests before maximizing weight residency. Measure peak allocation under the real workload instead of filling VRAM during model load and discovering runtime OOM or allocator pressure later.

For variable context or concurrency, benchmark the memory curve at the accepted maximum rather than only a small single-request prompt.

## Transfer and fallback residual

Use runtime/profiler/log evidence where available to observe host-device transfers, synchronization stalls, CPU fallback, page migration, cache movement, and device utilization. A configuration can appear GPU-heavy while bottlenecking on PCIe/interconnect traffic or unsupported operators.

On unified-memory systems, measure actual bandwidth, residency, pressure, and contention instead of assuming the absence of explicit copies removes placement constraints.

## Sustained-performance residual

Measure time-to-first output, prompt/prefill latency, decode throughput, end-to-end latency, power, clocks, temperature, and throttling over a long-enough run to represent the intended service or workstation workload. Short benchmarks can overstate configurations that cannot sustain their initial clocks or power envelope.

Compare accepted-result quality together with latency/memory/cost when offloading is paired with quantization or another representation change; placement and representation are separate variables and should not be conflated in the conclusion.

These placement, headroom, transfer, and sustained-performance practices remain migration source material until their exact learning, inference-engineering, runtime, performance-evaluation, capacity-planning, or decision-support owners are verified.
