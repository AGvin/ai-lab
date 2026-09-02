# Model Loading

Legacy residual retained for cold/warm startup benchmarking, peak/resident-memory measurement, cache/process behavior, and startup/recovery operations that are intentionally outside the canonical Model Loading concept owner.

> **Migration note:** Model-loading identity, download/conversion/compilation/warm-up/inference separation, loading-strategy variability, persisted-size versus peak/resident-memory distinctions, memory-mapping semantics, sharded-checkpoint versus parallelism boundaries, device-dispatch ownership, and successful-load versus practical-fit limits are already preserved in `docs/sub/concepts/sub/models/sub/inference/sub/execution/sub/model-loading/`. The remaining material below stays here until its exact learning, inference-engineering, deployment, performance-evaluation, or operations owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Startup-benchmark residual

Measure artifact acquisition/cache-hit state, cold load, warm/resident reuse, first-use compilation or kernel preparation, and first-request latency separately. A benchmark taken only after the model is fully resident and warmed does not represent scale-to-zero, restart, failover, or workstation workflows that reload models frequently.

Record storage medium, filesystem/cache state, artifact layout/sharding, runtime version, device placement, and host/device transfer conditions with startup measurements so later comparisons are reproducible.

## Memory-measurement residual

Observe peak host RAM, device memory, page cache, temporary conversion/compilation buffers, runtime workspaces, and steady-state resident memory rather than estimating capacity from artifact size alone. Include the headroom required by the operating system, caches, inference context, batching, and concurrent requests before declaring a deployment fit.

When memory mapping or lazy paging is used, evaluate page-fault/storage behavior under realistic memory pressure instead of assuming mapped weights have zero RAM cost or constant startup latency.

## Process and cache residual

Verify whether multiple workers/processes share file-backed pages, duplicate anonymous/device copies, or independently compile/cache runtime state. Containerization, worker counts, preload/fork behavior, persistent cache locations, and model-replica strategy can materially change total memory and cold-start behavior.

Treat cached downloads, converted artifacts, compiled graphs/kernels, and runtime caches as versioned operational state. Define invalidation rules so a model/runtime upgrade does not silently reuse incompatible cached output.

## Startup and recovery residual

Test the load path after a clean restart and under realistic failure conditions. Detect corrupt/incomplete artifacts, insufficient disk/RAM/VRAM, incompatible runtime state, and failed device transfers early enough to produce a clear service failure rather than partial readiness.

For services with readiness probes or traffic switching, mark the instance ready only after the execution path required for the workload is actually initialized to the agreed boundary; a process start or successful file open is not sufficient evidence.

These startup, memory, cache/process, and recovery practices remain migration source material until their exact learning, inference-engineering, deployment, performance-evaluation, or operations owners are verified.
