# FLUX.1 Kontext [pro]

FLUX.1 Kontext [pro] is a distinct Black Forest Labs **hosted** image model introduced on May 29, 2025. It is a production-oriented hosted model for text-to-image generation and text-guided reference-image editing. [BFL release](https://bfl.ai/blog/flux-1-kontext).

## Identity and scope

The published BFL API offers `POST /v1/flux-kontext-pro` for this model. It supports text-based image generation and image-conditioned editing, rather than supplying downloadable weights. Unlike the open-weight Kontext [dev] checkpoint, [pro] is a separate proprietary hosted model identity. Do not infer its weight architecture, parameter count, training-parent lineage, downloadable rights, or a local serving path. [API documentation](https://api.bfl.ai/docs).

## Use and limitations

BFL positions [pro] for faster iteration and multi-turn reference-image editing; consistency and latency are producer claims, not independent measurements.

Current BFL documentation lists the earlier-generation Kontext [pro] and [max] variants as available but recommends FLUX.2 for new projects. The Kontext generation envelope is approximately 1 MP; inspect current API constraints, image-input formats, billing and usage conditions before integration. [BFL support guide](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext).

Hosted model use is governed by applicable API/service contracts. Neither weights nor non-commercial dev-model rights should be inferred from the hosted endpoint. We have not independently run inference, validated reproducible performance or measured provider quality claims.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [Original BFL Kontext announcement](https://bfl.ai/blog/flux-1-kontext)
- [Current Kontext model support and lifecycle](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext)
- [BFL API model endpoints](https://api.bfl.ai/docs)
