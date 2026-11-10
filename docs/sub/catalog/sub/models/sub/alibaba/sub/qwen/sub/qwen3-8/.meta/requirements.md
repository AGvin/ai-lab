# Documentation Requirements

## Requirements

- Identify Qwen3.8 as a model series within Qwen based on first-party Qwen release repositories.
- Link every represented Qwen3.8 identity, including open checkpoints and the independently documented hosted Max and Flash models.
- Preserve coding, professional-work, research, and long-horizon agentic positioning only as current Qwen Team claims.
- Keep the independently documented hosted `qwen3.8-max` identity distinct from the open Qwen3.8-2.4T-A95B checkpoint; descriptive phrases such as `Qwen-Max-class` alone do not establish a new identity.

## Decision and Operational Boundaries

- Qwen3.8 includes separately released open checkpoints and independently named hosted Max and Flash models.
- Do not infer a common license: 27B is Apache-2.0, the 2.4T-A95B checkpoint uses a separate Qwen3.8-Max license, and Flash-Next uses Qwen Community License 1.0.
- Separate the text-only, thinking-only 2.4T-A95B weights from the multimodal hosted Max service; distinguish native checkpoint context from extended or hosted limits.
- Keep Flash-Next as a released experimental architecture preview and avoid presenting it as a stable Qwen4 release.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen3.8 remains a series within Qwen and has symmetric production provenance to Qwen Team.
- Concrete parameter/accounting facts remain with concrete models and distinguish total from active parameters where applicable.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
