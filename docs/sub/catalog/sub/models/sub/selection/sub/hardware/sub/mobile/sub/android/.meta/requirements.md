# Documentation Requirements

## Requirements

- Present Android as an entry/router, not one homogeneous accelerator target.
- Identify device model, SoC/vendor, Android/API level, available platform-provided AI features, LiteRT/vendor delegate or SDK path, and supported model/export before selection.
- Route custom on-device acceleration by SoC ecosystem: `qualcomm/`, `mediatek/`, `google/`, `samsung/`.
- Distinguish platform-provided models such as supported Gemini Nano/AICore routes from arbitrary app-deployed custom models.
- Require memory, storage, battery/thermal, sustained-load, model-format/operator, quantization, and app packaging constraints to be explicit.
- Use CPU/GPU fallback only when the intended runtime/model actually supports it and performance is measured; NPU presence does not guarantee usable acceleration.
- Recheck device/OS/vendor runtime support because Android support is unusually fragmented and mutable.

## Validation

- Recommendations are SoC/runtime scoped rather than “Android supports X”.
- Consumer feature support is not used as proof of custom-model NPU support.
- Direct children correspond to the four selected mobile SoC ecosystems.
