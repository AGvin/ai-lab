# Documentation Requirements

## Requirements

- Cover personal/workstation PCs where NVIDIA GeForce/RTX/RTX PRO-class CUDA compute is the intended local inference accelerator.
- Identify exact GPU SKU/architecture, VRAM, driver/CUDA/runtime backend, artifact/precision/quantization, context/cache, auxiliary models, and display/application/game VRAM occupancy.
- Distinguish CUDA-compatible runtime support from TensorRT/TensorRT for RTX support for the exact model/operators; provider-documented compatibility is not automatic task fit.
- Measure peak VRAM rather than using weight-file size; include KV/cache, temporary buffers, multimodal components, offload, batch/concurrency, and fragmentation/headroom.
- Measure prompt/decode latency, sustained thermals/power, and accepted-result quality under realistic desktop contention.
- Do not recommend another GPU until the existing card has been measured and a real capability/resource gap is demonstrated.
- Link gamer/local-GPU scenarios when user context is the primary question; this page remains hardware-first.

## Validation

- Nominal VRAM/load success does not equal practical fit.
- RTX datacenter/server assumptions are not imported without evidence.
- Buying advice stays outside model-selection ownership.
