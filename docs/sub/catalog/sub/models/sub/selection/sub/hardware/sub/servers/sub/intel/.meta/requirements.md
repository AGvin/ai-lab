# Documentation Requirements

## Requirements

- Cover existing Intel server AI compute where Gaudi or another Intel accelerator is the intended model-serving route; keep general Xeon CPU-only execution in sibling `cpu/`.
- Identify exact accelerator/SKU/count/memory, driver/software stack, current vLLM/Optimum/Intel-supported runtime, model/artifact/precision, interconnect/topology, and compatibility matrix.
- Distinguish Gaudi accelerator routes from Intel GPU/NPU PC routes and from CPU inference.
- Specify single-device/multi-device/multi-node topology and supported parallelism; do not treat aggregate HBM as automatically usable by one model.
- Account for KV/cache, batching/concurrency, communication overhead, compiler/runtime constraints, and service latency/throughput targets.
- Mark combinations Unknown when current Intel/runtime support does not verify them.

## Validation

- Exact accelerator/runtime/model support is current.
- Gaudi, Xeon CPU, and PC NPU/iGPU routes are not conflated.
- Multi-accelerator fit is topology-scoped.
