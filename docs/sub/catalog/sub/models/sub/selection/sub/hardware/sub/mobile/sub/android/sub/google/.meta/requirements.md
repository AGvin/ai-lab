# Documentation Requirements

## Requirements

- Cover Google Tensor/Pixel-class Android devices where Android platform-provided on-device generative AI or supported custom local execution is material.
- Identify exact Pixel/device, Tensor generation, Android/API level, AICore/Gemini Nano availability, and applicable app API before route selection.
- Treat platform-provided Gemini Nano as a managed system-model route whose model version/availability may change with OS/device support; do not represent it as an app-owned artifact.
- Keep arbitrary custom-model deployment separate and require a supported LiteRT/vendor execution path for the exact model/export.
- Account for context/task limits, memory, battery, thermals, rate/availability constraints, and hosted fallback when the system model is not appropriate.
- Recheck Android supported-device/API documentation when OS releases change.

## Validation

- System-model and custom-model routes remain distinct.
- Pixel feature availability is not generalized to all Android devices.
- Mutable system-model behavior is date/version bounded.
