# Documentation Requirements

## Requirements

- Cover Snapdragon Android devices where Qualcomm QNN/AI Hub or current Android/LiteRT integration is the intended acceleration route.
- Identify exact Snapdragon/Hexagon generation, device/Android version, QNN/runtime version, supported export/precision, and memory/thermal envelope before selecting candidates.
- Use Qualcomm AI Hub device/model exports as provider-documented compatibility evidence, not as proof that every artifact or Snapdragon generation behaves identically.
- Separate NPU-accelerated models from GPU/CPU fallbacks and record any partitioning/unsupported-operator fallback that materially affects latency or power.
- For generative models, measure prompt/decode latency, context/cache memory, sustained thermals, and task acceptance quality; do not rank by NPU TOPS alone.
- Recheck supported devices/model exports when Qualcomm runtime/toolchain versions change.

## Validation

- Exact SoC/runtime/export identity is recorded.
- AI Hub presence is not converted into an AI Lab performance endorsement.
- Unsupported operators/fallback execution remain visible.
