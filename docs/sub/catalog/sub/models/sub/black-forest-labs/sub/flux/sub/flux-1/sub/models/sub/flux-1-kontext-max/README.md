# FLUX.1 Kontext [max]

FLUX.1 Kontext [max] is a distinct Black Forest Labs **hosted** image model introduced on May 29, 2025. It is a separately released premium hosted in-context image generation and editing model. [BFL release](https://bfl.ai/blog/flux-1-kontext).

## Identity and scope

The published BFL API offers `POST /v1/flux-kontext-max` for this model. It supports text-based image generation and image-conditioned editing, rather than supplying downloadable weights. Unlike [pro] and the open-weight Kontext [dev], [max] is a distinct BFL-hosted identity. A larger hosted tier does not establish an openly released checkpoint, parameter count, specific training parent or reproducible local runtime. [API documentation](https://api.bfl.ai/docs).

## Use and limitations

BFL introduced [max] as experimental in May 2025 and promotes stronger prompt following, editing consistency and typography; current BFL guidance still lists [max] as available. No independently reproduced quality or stability guarantee.

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
