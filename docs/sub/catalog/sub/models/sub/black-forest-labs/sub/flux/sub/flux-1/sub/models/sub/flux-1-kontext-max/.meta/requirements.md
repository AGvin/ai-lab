# Documentation Requirements

## Identity and provenance

- Identify FLUX.1 Kontext [max] as a distinct released **BFL-hosted model**, not a local-weight form, precision preset or duplicate of Kontext [dev]. The original BFL release introduced two distinct hosted models [pro] and [max] on May 29, 2025. [BFL launch](https://bfl.ai/blog/flux-1-kontext).
- The current BFL support guide continues to list Kontext [pro] and [max] as available through API/Playground, while recommending newer FLUX.2 for new applications. Preserve previous-generation lifecycle and avoid claims of removed access. [Current provider guide](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext).
- The official API schema lists `POST /v1/flux-kontext-max` separately. Endpoint identity alone is not a proof of downloadable weights or a derived-from training relation. [API reference](https://api.bfl.ai/docs).

## Decision and operational boundaries

- BFL introduced [max] as experimental in May 2025 and promotes stronger prompt following, editing consistency and typography; current BFL guidance still lists [max] as available. No independently reproduced quality or stability guarantee. [Original release](https://bfl.ai/blog/flux-1-kontext).
- Both text-to-image generation and image-conditioned text-guided editing are supported. Current BFL help describes Kontext output at approximately fixed 1 MP; exact accepted image/input formats, policy checks, quotas and availability are provider/service-specific. [BFL guide](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext).
- Unlike [pro] and the open-weight Kontext [dev], [max] is a distinct BFL-hosted identity. A larger hosted tier does not establish an openly released checkpoint, parameter count, specific training parent or reproducible local runtime.
- Do not transfer FLUX.1 [dev] non-commercial weight-license provisions to proprietary API inference or imply that paying API fees licenses any local weights. Authentication, content rights, billing, retention and provider policies require contract-specific review.
- Do not publish guaranteed performance, VRAM fit, current per-image pricing or ranking without fresh provider evidence and independent tests.

## Validation

- Resolve one `member-of` link back to FLUX.1 and one reciprocal `has-member` edge.
- Show distinct [pro]/[max]/[dev] identities and the exact hosted route; do not infer training lineage or license from compatibility.
- No independently run image benchmark, cache/schema/CI or complete source-freshness credit.
