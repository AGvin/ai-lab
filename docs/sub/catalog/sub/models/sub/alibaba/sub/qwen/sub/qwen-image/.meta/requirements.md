# Documentation Requirements

## Requirements

- Identify Qwen-Image as the image-generation and image-editing model series within the broader Qwen family.
- Preserve the current series boundary across unified text-to-image generation and image editing without treating Alibaba Cloud Model Studio serving APIs, Qwen Studio image features, or generated artifacts as trained-model identities.
- Materialize released concrete Qwen-Image models only when their first-party identity and lifecycle are independently established.
- Preserve current Qwen-Image-3.0 and Qwen-Image-3.0-Pro as concrete hosted model identities alongside earlier independently materialized Qwen-Image releases; do not treat date snapshots or serving aliases as peer trained models.
- Keep architecture details, supported input counts, transparency/editing controls, inference backends, quantization, pricing, rate limits, regional availability, and provider routing freshness-sensitive.
- Preserve Qwen Team production provenance and the parent Qwen relation.
- Attribute quality, efficiency, typography, realism, and benchmark claims to Qwen Team or the cited evaluator rather than converting them into independent AI Lab rankings.

## Decision and Operational Boundaries

- Qwen-Image covers image-generation and image-editing models, including open 2.1 checkpoints and named hosted variants.
- Keep Qwen-Image-2.1 and its Turbo weights under the Qwen Research License; commercial use requires a separate license and is not made permissive by marketing terminology.
- Do not carry 2.1 reference-image counts, transparency, or inference-step settings into 3.0; follow the exact model and protocol.
- The OpenAI-compatible image route has a narrower contract than the full OpenAI Images API; verify synchronous/async behavior, output URL handling, and supported editing fields.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen-Image remains a model series within Qwen rather than an image API or end-user image product.
- Concrete open-weight and hosted model variants remain separate only where first-party sources expose independently identifiable model identities.
- Producer and parent relations resolve bidirectionally.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
