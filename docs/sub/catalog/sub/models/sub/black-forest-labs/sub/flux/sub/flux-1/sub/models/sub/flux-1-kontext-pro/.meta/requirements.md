# Documentation Requirements

## Identity and provenance

- Identify FLUX.1 Kontext [pro] as a distinct released **BFL-hosted model**, not a local-weight form, precision preset or duplicate of Kontext [dev]. The original BFL release introduced two distinct hosted models [pro] and [max] on May 29, 2025. [BFL launch](https://bfl.ai/blog/flux-1-kontext).
- The current BFL support guide continues to list Kontext [pro] and [max] as available through API/Playground, while recommending newer FLUX.2 for new applications. Preserve previous-generation lifecycle and avoid claims of removed access. [Current provider guide](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext).
- The official API schema lists `POST /v1/flux-kontext-pro` separately. Endpoint identity alone is not a proof of downloadable weights or a derived-from training relation. [API reference](https://api.bfl.ai/docs).

## Decision and operational boundaries

- BFL positions [pro] for faster iteration and multi-turn reference-image editing; consistency and latency are producer claims, not independent measurements. [Original release](https://bfl.ai/blog/flux-1-kontext).
- Both text-to-image generation and image-conditioned text-guided editing are supported. Current BFL help describes Kontext output at approximately fixed 1 MP; exact accepted image/input formats, policy checks, quotas and availability are provider/service-specific. [BFL guide](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext).
- Unlike the open-weight Kontext [dev] checkpoint, [pro] is a separate proprietary hosted model identity. Do not infer its weight architecture, parameter count, training-parent lineage, downloadable rights, or a local serving path.
- Do not transfer FLUX.1 [dev] non-commercial weight-license provisions to proprietary API inference or imply that paying API fees licenses any local weights. Authentication, content rights, billing, retention and provider policies require contract-specific review.
- Do not publish guaranteed performance, VRAM fit, current per-image pricing or ranking without fresh provider evidence and independent tests.

## Validation

- Resolve one `member-of` link back to FLUX.1 and one reciprocal `has-member` edge.
- Show distinct [pro]/[max]/[dev] identities and the exact hosted route; do not infer training lineage or license from compatibility.
- No independently run image benchmark, cache/schema/CI or complete source-freshness credit.
