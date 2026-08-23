# Documentation Requirements

## Requirements

- Cover NVIDIA Jetson developer/module systems as an integrated embedded CUDA platform, not a miniature desktop GPU.
- Identify exact Jetson module/family, installed system memory, JetPack/Jetson Linux generation, CUDA/TensorRT/TensorRT-LLM or other backend, power mode, and sustained thermal envelope.
- Check exact JetPack support for the device; current Orin and Thor software generations may differ materially and must not be assumed interchangeable.
- Treat shared system memory, CPU/GPU/media-engine use, context/cache, multimodal encoders, and other services as part of practical model headroom.
- Measure prompt/decode or task throughput/latency under selected power mode and sustained load; TOPS/AI performance labels alone are insufficient.
- Keep Orin/Thor as one ecosystem page until actual content/reader navigation justifies separate children; use compatibility tables/sections first.
- Link robotics/physical-AI decision guides when task intent rather than hardware fit becomes primary.

## Validation

- JetPack/device generation is pinned.
- Shared-memory/power-mode constraints are explicit.
- Desktop RTX assumptions are not imported automatically.
