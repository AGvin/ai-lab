# Documentation Requirements

## Requirements

- Cover phones/tablets where mobile OS policy, SoC accelerators, battery/thermal limits, app packaging, and platform model APIs constrain local model selection.
- Route Apple devices to `apple/` and Android devices to `android/`; do not classify laptops here merely because they use ARM SoCs.
- Require exact device/SoC, OS version, supported platform/runtime APIs, model format/export, memory/storage budget, and sustained thermal behavior before recommending a local route.
- Distinguish system-provided models/APIs from app-bundled custom models and third-party local runtimes.
- Compare local value against hosted/hybrid fallback when mobile context, memory, battery, or model quality make local execution unsuitable.

## Validation

- Direct children are only `apple/` and `android/`.
- Mobile support is not inferred from desktop support for the same vendor/architecture.
- Consumer AI feature availability is not treated as proof that arbitrary custom models can use the same accelerator.
