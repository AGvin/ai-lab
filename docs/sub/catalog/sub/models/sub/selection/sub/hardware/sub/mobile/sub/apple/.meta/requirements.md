# Documentation Requirements

## Requirements

- Cover iPhone/iPad-class Apple devices where OS/device eligibility, app memory, battery/thermals, and Apple on-device model APIs constrain the model route.
- Identify exact device generation, OS version, available system model/API, app deployment method, and local storage/memory budget before recommending a route.
- Distinguish the Apple Foundation Models framework/system-provided on-device model from app-bundled/custom Core ML/Core AI models and third-party runtimes; they have different identity, update, compatibility, and task boundaries.
- Treat CPU/GPU/Neural Engine execution as model/runtime-specific; do not assume every model can use every compute unit.
- Account for context window, multimodal auxiliary assets, app memory pressure, battery, thermals, package/download size, and sustained use.
- When a task needs more reasoning/context or unsupported modalities than the on-device route provides, present an explicit hosted/hybrid fallback with data-boundary implications.
- Recheck Apple supported-device/OS/API requirements and model changes before presenting system-model behavior as current.

## Validation

- Consumer Apple Intelligence availability is not equated with arbitrary custom-model deployment support.
- System-provided and custom-model routes remain distinct.
- Device support and practical task quality are both required; neither implies the other.
