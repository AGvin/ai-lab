# Documentation Requirements

## Requirements

- Cover Apple-Silicon Macs where unified memory and Apple-native/Metal-backed runtimes define the local model route.
- Identify exact M-series chip, installed unified memory, macOS version, intended runtime/backend (for example MLX/Core ML/Metal-backed), exact artifact/quantization, and concurrent application load.
- Treat unified memory as shared system memory, not dedicated VRAM; reserve headroom for macOS, applications, context/KV cache, multimodal encoders, runtime allocations, and display workloads.
- Compare prompt processing, decode/generation, context headroom, memory pressure/swap, modality support, and accepted-result quality under realistic concurrent load.
- Do not assume a model fitting in unified memory has useful latency or sustained responsiveness; measure.
- Link the `user-scenarios/professionals/mac-developer-or-creator/` route when professional context, hybrid data handling, or creator workflow matters more than hardware fit alone.
- Keep Mac purchase/memory-upgrade advice outside this page; expose a different/hybrid route when existing hardware is insufficient.

## Validation

- Unified memory is not labeled VRAM or treated as fully available to the model.
- Runtime/artifact/OS conditions are pinned for fit claims.
- Hardware-fit and professional-scenario ownership remain separate.
