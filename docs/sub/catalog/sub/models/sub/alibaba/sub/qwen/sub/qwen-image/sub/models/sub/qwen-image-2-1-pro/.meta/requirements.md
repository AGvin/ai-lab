# Documentation Requirements

## Requirements

- Identify Qwen-Image-2.1-Pro as the released Alibaba Cloud Model Studio model identity `qwen-image-2.1-pro`, released for international service on 2026-10-02.
- Preserve its current text-to-image and image-editing boundary, including transparent-image workflows and multi-reference editing, only while first-party Model Studio documentation supports those capabilities.
- Keep Qwen-Image-2.1-Pro distinct from the open-weight Qwen-Image-2.1 checkpoint and from the Alibaba Cloud Model Studio service that hosts it.
- Treat model routing, regions, prices, quotas, output-size controls, reference limits, prompt rewriting, endpoint behavior, and lifecycle aliases/snapshots as serving facts rather than intrinsic permanent architecture.
- Attribute quality, efficiency, realism, typography, and product-fidelity claims to Alibaba/Qwen first-party material rather than independent AI Lab measurement.

## Decision and Operational Boundaries

- qwen-image-2.1-pro is a separately named hosted image generation/editing model; it is not a runtime option on another catalog model.
- The current editing contract supports up to ten reference images with prompt-driven transparency; follow the exact API rather than adjacent-model marketing summaries.
- The OpenAI-compatible route uses synchronous /images/generations with its image extension; it does not implement /images/edits, multipart masks, streaming, or asynchronous calls. DashScope supplies the asynchronous route.
- Do not infer open weights or a checkpoint license from the service model name; validate returned asset persistence and service retention separately.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete hosted model identity, not the hosting service or the open-weight Qwen-Image-2.1 checkpoint.
- Serving properties are freshness-sensitive and not generalized to the full Qwen-Image series.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
