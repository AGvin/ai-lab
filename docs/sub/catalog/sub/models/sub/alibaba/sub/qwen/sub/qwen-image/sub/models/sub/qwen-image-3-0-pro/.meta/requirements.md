# Documentation Requirements

## Requirements

- Identify Qwen-Image-3.0-Pro as the released higher-quality Qwen image-generation/editing model identity `qwen-image-3.0-pro`.
- Preserve current complex-layout, multilingual small-text, image-generation/editing, multi-output, and higher-quality positioning only while current first-party Model Studio documentation supports those facts.
- Keep Qwen-Image-3.0-Pro distinct from Qwen-Image-3.0, older Qwen-Image generations, Model Studio as host, and version/date snapshots.
- Treat image-size/reference limits, API behavior, pricing, quotas, regions, latency/speed trade-offs, provider comparisons, and lifecycle aliases as freshness-sensitive.
- Attribute quality and productivity comparisons to Alibaba/Qwen rather than independent AI Lab measurement.

## Decision and Operational Boundaries

- qwen-image-3.0-pro is a separately named hosted image generation/editing model; it is not a runtime option on another catalog model.
- The current editing contract supports one to three reference images; follow the exact API rather than adjacent-model marketing summaries.
- The OpenAI-compatible route uses synchronous /images/generations with its image extension; it does not implement /images/edits, multipart masks, streaming, or asynchronous calls. DashScope supplies the asynchronous route.
- Do not infer open weights or a checkpoint license from the service model name; validate returned asset persistence and service retention separately.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete Pro model identity rather than a billing tier or generic quality mode.
- Standard/Pro claims remain model-specific and provider-attributed.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
