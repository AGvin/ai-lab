# FLUX1.1 [pro]

FLUX1.1 [pro] is a separately released Black Forest Labs **hosted** text-to-image model introduced on October 2, 2024. It is distinct from FLUX.1 [pro] and the open-weight FLUX.1 [dev] and [schnell] checkpoints. [BFL launch](https://bfl.ai/blog/24-10-02-flux).

## Identity and scope

BFL serves this model through POST /v1/flux-pro-1.1. The model is cataloged within the FLUX.1 suite, but this navigation grouping does not assert weight inheritance or a particular training parent. No downloadable FLUX1.1 [pro] checkpoint, parameter count or local-deployment right is established here. [Official API](https://api.bfl.ai/docs).

## Use and limitations

BFL's November 2024 release added **Ultra** for higher-resolution generation (up to 4 MP) and **Raw** for a more candid photographic aesthetic. BFL calls these **modes of FLUX1.1 [pro]**; the separate Ultra endpoint is not proof of a separately trained model. [Ultra and Raw modes](https://bfl.ai/blog/24-11-06-ultra).

BFL described improved text-to-image speed and prompt adherence at release; those comparative claims are provider assertions, not independent benchmarks. For new integrations, compare the current FLUX.2 and FLUX 3 offerings rather than presuming this previous-generation endpoint is optimal. [Current model catalog](https://bfl.ai/models/).

Hosted inference is subject to the current API/service contract. Confirm quotas, generation options, output rights, billing, retention and policy restrictions directly. We have not independently run inference or measured quality, latency or hardware fit.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [Original FLUX1.1 [pro] launch](https://bfl.ai/blog/24-10-02-flux)
- [FLUX1.1 [pro] model profile](https://bfl.ai/models/flux-pro)
- [Ultra/Raw modes announcement](https://bfl.ai/blog/24-11-06-ultra)
- [Current API routes](https://api.bfl.ai/docs)
