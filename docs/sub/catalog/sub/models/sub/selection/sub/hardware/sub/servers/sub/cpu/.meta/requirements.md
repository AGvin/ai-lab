# Documentation Requirements

## Requirements

- Cover dedicated CPU-server inference where no accelerator is the intended execution path.
- Identify CPU ISA/generation, sockets/NUMA topology, cores/threads, RAM capacity/bandwidth/channels, runtime/backend, exact artifact/quantization, context/cache, concurrency, and service latency target.
- Prefer CPU-optimized/quantized models and runtimes with current architecture support; distinguish RAM capacity from memory bandwidth/compute-limited performance.
- Pin NUMA/threading/batch/concurrency conditions for measurements; a model fitting in system RAM does not imply useful serving throughput.
- Account for KV/cache growth, preprocessing, scheduler/service overhead, and power/TCO when comparing local CPU serving with accelerator or hosted alternatives.
- Escalate when accepted-result latency/throughput/energy economics justify another existing compute route; do not turn this into accelerator purchasing advice.

## Validation

- Capacity and performance are measured separately.
- NUMA/socket/runtime conditions are explicit for material claims.
- Hosted/accelerated fallback remains a valid outcome.
