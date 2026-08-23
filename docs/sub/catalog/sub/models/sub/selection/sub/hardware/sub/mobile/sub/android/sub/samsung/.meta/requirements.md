# Documentation Requirements

## Requirements

- Cover Samsung Exynos Android devices when Exynos NPU/GPU/CPU execution is the actual custom-model route.
- Identify exact Exynos generation/device, Android version, current Samsung AI toolchain/runtime, supported operators/data types/model conversion, and memory/thermal constraints before selection.
- Do not infer arbitrary NPU model support from Galaxy AI consumer features; consumer services and developer-deployable models are different contracts.
- If Samsung tooling delegates through LiteRT/another standardized runtime, record the exact delegate/backend and fallback behavior rather than treating “Exynos NPU” as sufficient detail.
- Require target-device measurement for latency, memory, sustained thermals/battery, and task quality.
- If current public developer support is insufficient for an exact model route, state `Unknown` rather than extrapolating from SoC TOPS.

## Validation

- Developer-deployable model evidence is separated from consumer feature marketing.
- Unsupported/publicly undocumented routes remain Unknown.
- Exact Exynos/runtime scope is visible.
