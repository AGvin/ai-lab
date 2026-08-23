# Documentation Requirements

## Requirements

- Cover dedicated local/on-prem inference hosts and accelerator servers where service-style operation, large memory, concurrency, multi-accelerator execution, sharding, and sustained throughput materially affect feasible models.
- Route by accelerator ecosystem: `nvidia/`, `amd/`, `intel/`, `cpu/`.
- Treat single-device, multi-device, and multi-node topology as mandatory comparison dimensions inside applicable pages; do not infer practical capacity by summing memory.
- Require exact accelerator architecture/count/memory per device, interconnect/topology, runtime/backend, supported model/precision, batching/concurrency/KV-cache, prefill/decode behavior, throughput/latency target, and operational availability.
- Keep server purchasing and full deployment/failover architecture outside this journey; use existing server state as the model-selection constraint.

## Validation

- Direct children are the four selected server compute ecosystems.
- Datacenter accelerator support is not inferred from consumer-GPU support or vice versa.
- Aggregate VRAM is never presented as usable model capacity without a supported sharding/runtime topology.
