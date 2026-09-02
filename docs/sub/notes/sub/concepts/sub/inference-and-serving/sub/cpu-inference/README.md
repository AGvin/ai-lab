# CPU Inference

Legacy residual retained for thread/NUMA tuning, memory-bandwidth profiling, sustained benchmark, coexistence/capacity, and practical cost-fit evaluation that are intentionally outside the canonical CPU Inference concept owner.

> **Migration note:** CPU-inference identity, model/deployment/quality-tier separation, architecture/precision/kernel/memory/topology dependence, capacity-versus-performance boundaries, heterogeneous-placement semantics, and non-universal CPU/GPU cost/speed/efficiency claims are already preserved in `docs/sub/concepts/sub/models/sub/inference/sub/execution/sub/cpu-inference/`. The remaining material below stays here until its exact learning, inference-engineering, runtime, performance-evaluation, capacity-planning, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Thread and NUMA residual

Benchmark several thread counts and affinity policies instead of assuming one software thread per logical core is optimal. Observe physical-core utilization, SMT behavior, memory-controller/channel pressure, cache contention, and runtime scheduling under the actual model and batch/context shape.

On multi-socket or NUMA systems, test memory allocation and thread placement together. Remote-memory traffic can erase gains from additional cores, while pinning that helps one model/process can reduce flexibility for mixed workloads.

## Bandwidth and kernel residual

Use runtime/profiler evidence where practical to determine whether execution is limited by memory bandwidth, compute, cache behavior, synchronization, unsupported operators, or an unoptimized generic kernel path. Verify vector/matrix instruction support and the runtime build actually selected for the processor rather than inferring performance from CPU model/core count alone.

When quantized or reduced-precision execution is expected, confirm native/runtime-supported kernels for the exact representation. A compact artifact can consume less RAM while delivering little speed benefit if the hot path repeatedly converts or lacks optimized instructions.

## Sustained-benchmark residual

Measure prompt/prefill latency, decode throughput, end-to-end latency distribution, batch/concurrency behavior, resident/peak RAM, CPU utilization, power, clocks/temperature, and throttling over a representative run. Laptop or burst benchmarks should not be used as sustained server/workstation evidence without checking the steady-state power/thermal regime.

Compare several real workload shapes because embeddings, reranking, short generations, long-context prompts, and low-concurrency chat can exercise CPUs differently.

## Coexistence and cost-fit residual

Account for operating-system and application load, other services, memory pressure, latency interference, and reserved capacity before using all cores/RAM for inference. For shared hosts, benchmark the service-level impact on both inference and neighboring workloads.

Evaluate practical fit using accepted-result quality, latency/throughput, hardware already owned, energy/power, operational complexity, and opportunity cost together. Large RAM capacity can make a model loadable without making it the best production route.

These tuning, profiling, sustained-performance, coexistence, and cost-fit practices remain migration source material until their exact learning, inference-engineering, runtime, performance-evaluation, capacity-planning, or decision-support owners are verified.
