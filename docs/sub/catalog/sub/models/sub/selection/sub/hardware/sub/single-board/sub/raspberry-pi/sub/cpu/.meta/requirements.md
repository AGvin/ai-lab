# Documentation Requirements

## Requirements

- Cover CPU-only Raspberry Pi inference without assuming an NPU/GPU add-on.
- Pin Pi generation, RAM, OS architecture, CPU runtime/backend, artifact/quantization, context/cache, storage, active cooling, and target latency.
- Favor compact text/speech/vision models with mature ARM CPU support; avoid describing an accelerator-specific export as CPU-fit merely because source weights exist.
- Measure RAM peak, prompt/task latency, sustained thermals/throttling, and accepted-result quality; model load alone is insufficient.
- Account for camera/audio preprocessing and other host-side work that shares CPU/RAM.
- Recommend hosted/accelerated escalation when CPU latency or modality requirements make local execution impractical.

## Validation

- No Hailo acceleration is assumed.
- ARM compatibility and practical latency are both verified.
- Sustained thermal behavior is not omitted for long-running use.
