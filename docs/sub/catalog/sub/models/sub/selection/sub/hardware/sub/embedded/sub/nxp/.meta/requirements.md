# Documentation Requirements

## Requirements

- Cover NXP MCU/embedded targets using the current eIQ ecosystem/runtime for the exact i.MX RT or other applicable platform.
- Identify target SoC/core/accelerator, SRAM/external memory/flash, eIQ/tool/runtime version, supported model format/operators/data types, quantization, and real-time/power constraints.
- Separate CPU/DSP/NPU execution routes and record fallback/partitioning that affects determinism or latency.
- Prefer model-zoo/tool-supported examples as compatibility evidence while requiring target-application accuracy/latency/memory measurement after conversion.
- Include sensor/preprocess/postprocess/firmware resource costs when they materially consume the same memory/compute budget.
- Keep Linux-capable application processors in a more appropriate hardware class when the deployment no longer behaves like deeply constrained MCU inference.

## Validation

- Exact target/toolchain is pinned.
- eIQ ecosystem branding does not collapse materially different device classes.
- Real-time/power and post-conversion quality are part of fit.
