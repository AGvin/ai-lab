# Documentation Requirements

## Requirements

- Cover Android phones/tablets using MediaTek SoCs where NeuroPilot/Neuron or current vendor acceleration is the intended route.
- Identify exact Dimensity/SoC generation, Android version, NeuroPilot/runtime access level/version, supported operators/data types, and model conversion/export path.
- Keep mobile Dimensity guidance distinct from MediaTek Genio/Linux embedded products even when both use NeuroPilot branding.
- Record whether execution is NPU/GPU/CPU/heterogeneous and whether unsupported operations fall back, because fallback materially changes latency/power.
- For generative routes, require current vendor support for the exact architecture/quantization rather than inferring support from generic transformer capability.
- Measure sustained latency, memory, thermals, battery, and accepted-result quality on the target device.

## Validation

- SoC/toolkit scope is explicit.
- NeuroPilot marketing capability is not treated as exact model support.
- Mobile and embedded MediaTek product classes are not collapsed.
