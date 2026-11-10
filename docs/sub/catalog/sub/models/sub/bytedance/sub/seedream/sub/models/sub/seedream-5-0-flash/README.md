# Seedream 5.0 Flash

Seedream 5.0 Flash is ByteDance Seed's separately announced September 2026 hosted image-generation and editing model. BytePlus and Volcengine use different service IDs for the same named model. Exact training lineage, architecture and downloadable weights have not been independently established. [BytePlus release](https://docs.byteplus.com/en/docs/modelark/model-release-announcement) [Volcengine release](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh).

## Identity and scope

BytePlus identifies `dola-seedream-5-0-flash-260915`, while Volcengine identifies `doubao-seedream-5-0-flash-260915`. These distinguish provider API routes, not additional catalog model identities. Flash is not assumed to be derived from Pro simply because their features overlap. [BytePlus release](https://docs.byteplus.com/en/docs/modelark/model-release-announcement) [Volcengine release](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh).

## Use and limitations

The reviewed provider contract supports text-to-image, reference-image editing, precise editing with markers, multilingual generation and layer decomposition (one base image and up to sixteen independent layers). It lists 1K, 1.5K and 2K tiers, PNG/JPEG outputs and standard prompt optimization. Flash does not inherit Pro's additional fast prompt optimization mode. [BytePlus Pro/Flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro).

For the BytePlus route, use at most ten input references; sequential image batches, web search and streaming output are not supported. The 500 IPM limit is published service metadata, not independently measured throughput. No 4.0/Lite batch or search behavior should be inferred. [BytePlus image API](https://docs.byteplus.com/en/docs/modelark/image-generation-api) [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list).

**Save outputs promptly:** provider image URLs expire after 24 hours. Layer decomposition requires preserving PNG alpha, position and stacking metadata before recompositing. Confirm service/region availability, rights and current price for the chosen account. BytePlus currently scopes the published list to ap-southeast-1; other routes must be checked separately. [BytePlus image API](https://docs.byteplus.com/en/docs/modelark/image-generation-api) [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list).

BytePlus positions Flash as lower latency/cost and Pro as higher quality, but this is vendor positioning, not an AI Lab benchmark. Prior regional notices retiring 4.0/4.5/Lite routes do not establish Flash retirement. Russian beneficial-ownership review is still pending; no verified Tier 1 or Tier 2 conclusion is asserted. [BytePlus comparison](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro) [BytePlus pricing](https://docs.byteplus.com/en/docs/modelark/model-pricing).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [Seedream](../../../../README.md) | `model-family` |

## Sources

- [BytePlus release bulletin](https://docs.byteplus.com/en/docs/modelark/model-release-announcement)
- [Volcengine release bulletin](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh)
- [BytePlus Pro/Flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro)
- [BytePlus image generation API](https://docs.byteplus.com/en/docs/modelark/image-generation-api)
- [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list)
- [BytePlus pricing](https://docs.byteplus.com/en/docs/modelark/model-pricing)
