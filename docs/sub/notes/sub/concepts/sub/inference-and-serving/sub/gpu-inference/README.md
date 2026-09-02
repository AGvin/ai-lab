# GPU Inference

Legacy residual retained for VRAM/workload sizing, kernel/fallback profiling, single-versus-multi-GPU benchmarking, sustained thermal/power evaluation, and practical deployment-fit guidance that are intentionally outside the canonical GPU Inference concept owner.

> **Migration note:** GPU-inference identity, model/deployment/quality-tier separation, architecture/precision/kernel/workload dependence, usable-memory versus weight-size boundaries, peak-spec versus realized-performance semantics, fallback/transfer behavior, multi-GPU/offloading distinctions, and non-universal GPU/CPU cost-speed-efficiency claims are already preserved in `docs/sub/concepts/sub/models/sub/inference/sub/execution/sub/gpu-inference/`. The remaining material below stays here until its exact learning, inference-engineering, runtime, performance-evaluation, capacity-planning, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## VRAM and workload residual

Measure peak and steady-state device memory with the exact model/artifact, precision/quantization, context length, batch size, concurrency, cache policy, graph/kernel workspaces, and runtime configuration used in production. Do not treat model weight bytes or advertised VRAM capacity as the full feasibility model.

Benchmark the accepted maximum context/concurrency combination and leave allocator/runtime headroom so a configuration that barely loads does not fail under real requests.

## Kernel and fallback residual

Use runtime/profiler/log evidence where practical to confirm the intended GPU kernels and execution providers are active for the hot operations. Observe CPU fallback, host-device transfers, synchronization, unsupported operators, dequantization/conversion, and utilization rather than attributing poor performance only to the GPU hardware.

Verify native support for the exact numerical representation and model operations. A lower-bit or mixed-precision artifact can be smaller while running slower if the runtime converts it repeatedly or lacks efficient kernels.

## Single- and multi-GPU residual

Establish a single-GPU baseline where feasible before comparing multi-GPU execution. Record the exact partition/parallelism strategy, device topology/interconnect, communication volume, load balance, memory placement, and context/batch shape with the result.

Additional GPUs can provide capacity or throughput while increasing synchronization and communication cost; evaluate realized scaling instead of assuming aggregate VRAM or peak compute combines linearly.

## Sustained-performance residual

Measure time to first output, prompt/prefill latency, decode throughput, end-to-end latency distribution, concurrency, memory, power, clocks, temperature, and throttling over a representative sustained run. Short burst benchmarks can hide thermal or power limits that materially change workstation/server behavior.

## Practical-fit residual

Evaluate accepted-result quality, latency/throughput, hardware/runtime compatibility, memory headroom, concurrency, energy/power, purchase/cloud cost, availability, reliability/operational requirements, and workload utilization together. A higher-spec GPU is not automatically the lowest-TCO or best-fit execution route.

These memory, profiling, multi-GPU, sustained-performance, and practical-fit practices remain migration source material until their exact learning, inference-engineering, runtime, performance-evaluation, capacity-planning, or decision-support owners are verified.
