# Documentation Requirements

## Requirements

- Cover existing AMD Instinct/ROCm server accelerator hosts.
- Identify exact Instinct GPU architecture/SKU/count/memory, ROCm/driver/runtime (e.g. vLLM or supported backend), interconnect/topology, model/artifact/precision, and current compatibility matrix.
- Keep consumer Radeon assumptions separate; server Instinct support must come from current ROCm/runtime documentation for the exact accelerator/model path.
- Distinguish single-GPU, multi-GPU, and multi-node execution and specify supported sharding/parallelism instead of summing memory.
- Account for KV/cache, batching/concurrency, communication overhead, quantization, scheduler, and prefill/decode behavior.
- Measure representative throughput/latency/memory/headroom and accepted-result quality; unsupported combinations remain Unknown.

## Validation

- Instinct and Radeon support boundaries remain separate.
- ROCm/runtime/model compatibility is pinned.
- Multi-GPU capacity claims include actual serving topology.
