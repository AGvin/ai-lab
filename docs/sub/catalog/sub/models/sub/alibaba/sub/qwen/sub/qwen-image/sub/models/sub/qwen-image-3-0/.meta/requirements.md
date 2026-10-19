# Documentation Requirements

## Requirements

- Identify Qwen-Image-3.0 as the released standard Qwen image-generation/editing model identity `qwen-image-3.0`.
- Preserve the current unified text-to-image and image-editing boundary, dense-layout/text-rendering behavior, multilingual font support, output controls, and multi-output behavior only while first-party Model Studio documentation supports them.
- Keep Qwen-Image-3.0 distinct from Qwen-Image-3.0-Pro, older Qwen-Image generations, Model Studio as the hosting service, and snapshot/region-specific serving aliases.
- Treat input/output limits, image sizes, reference-image behavior, pricing, quotas, regional availability, API protocol support, snapshot aliases, and provider quality/speed comparisons as freshness-sensitive serving facts.
- Attribute generation quality, text rendering, semantic adherence, and speed/cost positioning to Alibaba/Qwen first-party material rather than independent AI Lab ranking.

## Decision and Operational Boundaries

- qwen-image-3.0 is a separately named hosted image generation/editing model; it is not a runtime option on another catalog model.
- The current editing contract supports one to three reference images; follow the exact API rather than adjacent-model marketing summaries.
- The OpenAI-compatible route uses synchronous /images/generations with its image extension; it does not implement /images/edits, multipart masks, streaming, or asynchronous calls. DashScope supplies the asynchronous route.
- Do not infer open weights or a checkpoint license from the service model name; validate returned asset persistence and service retention separately.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete standard 3.0 model identity rather than the Qwen-Image series or Model Studio service.
- Serving aliases/snapshots do not become duplicate peer model identities by default.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
