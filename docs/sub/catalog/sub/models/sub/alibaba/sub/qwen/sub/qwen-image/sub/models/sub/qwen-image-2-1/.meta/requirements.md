# Documentation Requirements

## Requirements

- Identify Qwen-Image-2.1 as Qwen Team's released open-weight unified image-generation and image-editing model published on 2026-09-20.
- Preserve native transparent-image generation/editing, multi-reference/local-edit workflows, the current visual-generation architecture, and first-party runtime examples only while current Qwen evidence supports them.
- Keep model weights and architecture separate from hosted Model Studio variants, Qwen Studio product behavior, Diffusers/ComfyUI/vLLM-Omni/SGLang integrations, and generated outputs.
- Treat parameter counts, memory/runtime guidance, supported reference-image counts, backend optimizations, precision/quantization, license terms, and performance claims as freshness-sensitive.
- Attribute quality, efficiency, typography, portrait/product-fidelity, and benchmark claims to Qwen Team or their cited evaluations.

## Decision and Operational Boundaries

- Qwen-Image-2.1 is the September 20, 2026 open-weight unified generation/editing release with a 7B visual-generation component.
- The weights use the Qwen Research License for non-commercial research/evaluation; commercial use needs a separate license.
- Native transparent-image workflows and 7B visual-component size must not be treated as a complete pipeline memory estimate or a hosted Pro API contract.
- Use the exact QwenImage21Pipeline/checkpoint compatibility and keep prompt-rewriter weights, runtime integrations, and generated assets distinct.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node represents the released Qwen-Image-2.1 trained model rather than the Qwen-Image series or a hosted API product.
- Runtime integrations are not duplicated as model identities.
- Mutable architecture/performance claims remain source-scoped.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
