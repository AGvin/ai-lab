# Documentation Requirements

## Requirements

- Cover general-purpose computers where no useful supported GPU/NPU accelerator is available for the intended model/workload.
- Identify CPU architecture/instruction support, core/thread topology, RAM capacity/bandwidth, OS/runtime, exact artifact/quantization, context/cache, and intended latency before selection.
- Prefer compact/quantized models with mature CPU runtimes; separate “can execute” from interactive/useful performance.
- Measure prompt processing, generation/task latency, memory bandwidth pressure, RAM peak, context headroom, and concurrency rather than inferring from model size.
- For multimodal/generative media workloads, account for preprocessors/encoders/decoders that may dominate CPU time or memory.
- Present hosted/hybrid escalation when the accepted-result latency/quality economics are poor; do not force local merely because enough RAM exists.

## Validation

- CPU route is used only when a relevant supported accelerator route is not the intended path.
- RAM capacity alone does not establish useful performance.
- Hosted fallback remains a legitimate outcome.
