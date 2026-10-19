# Documentation Requirements

## Requirements

- Identify Qwen-Image-2.1-Turbo as the released speed/cost-oriented member of the Qwen-Image 2.1 generation.
- Preserve current unified image generation/editing and transparency support only while first-party Alibaba/Qwen documentation supports those capabilities for this exact model ID.
- Keep Turbo distinct from Qwen-Image-2.1 and Qwen-Image-2.1-Pro rather than treating it as a generic serving mode.
- Treat pricing, latency, output limits, reference-image limits, regions, quotas, snapshot aliases, and provider quality/speed comparisons as freshness-sensitive.
- Attribute balance/quality/cost positioning to Alibaba/Qwen rather than independent AI Lab ranking.

## Decision and Operational Boundaries

- Qwen-Image-2.1-Turbo is both an independently released accelerated checkpoint and a named hosted variant; the October 9, 2026 checkpoint uses eight denoising steps.
- The open checkpoint is Qwen Research licensed; a hosted API listing is not a permissive commercial license to its weights.
- Keep the checkpoint's 7B visual component and Diffusers pipeline distinct from whole-pipeline memory and hosted quotas.
- The current hosted 2.1 Turbo editing contract allows up to ten references and prompt-driven transparency; do not inherit 3.0 protocol limits or negative-prompt support.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete Turbo model identity rather than a service tier.
- Provider comparisons remain model- and configuration-scoped.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
