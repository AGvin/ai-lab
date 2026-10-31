# Seedream 4.5

Seedream 4.5 is ByteDance Seed's released image-generation and image-editing model, distinct from 4.0 and 5.0 Lite/Pro/Flash. ByteDance describes improved editing consistency across multiple references, subject preservation and dense-text typography. Publisher MagicBench claims are not independent AI Lab measurements. [ByteDance product](https://seed.bytedance.com/en/seedream4_5).

## Identity and scope

The dated `doubao-seedream-4-5-251128` Volcengine Ark and `seedream-4-5-251128` BytePlus identifiers are hosted routes for one named model, not two learned identities. The suffix does not prove a precise release date or a trained-from-4.0 relationship. No public weights or parameter count were verified. [Ark list](https://docs.volcengine.com/docs/ark/model-list?lang=en) [BytePlus list](https://docs.byteplus.com/en/docs/modelark/model-list).

## Hosted lifecycle and limitations

**Not recommended for new integrations via the dated Volcengine Ark route.** Ark stopped new 4.5 endpoint purchases on **2026-09-24 10:00 UTC+8** and schedules service closure for **2026-11-24 14:00 UTC+8**. Pro is the named migration target, but its sequential-batch and editing feature parity is not guaranteed. Do not equate Ark EOS with global retirement of the named model. [Ark deprecation notice](https://docs.volcengine.com/docs/ark/model-deprecation-notice?lang=zh).

In the reviewed providers, 4.5 supports text-to-image, single/multiple-reference editing and sequential group-image generation. Validate the selected route's actual resolution, batch count, limits and output persistence contract before production use. [Ark tutorial](https://docs.volcengine.com/docs/ark/image-generation-tutorial?lang=en) [BytePlus image API](https://docs.byteplus.com/en/docs/modelark/image-generation-api).

BytePlus lists the model for ap-southeast-1, and currently bills per successful image, including grouped outputs; this is mutable service availability and vendor pricing rather than a permanent model capability. Provider rights, region and user-account activation must be checked. Partial/indirect Russian beneficial ownership remains unverified; do not label Tier 1/2 without evidence. [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list) [BytePlus price](https://docs.byteplus.com/en/docs/modelark/model-pricing).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [Seedream](../../../../README.md) | `model-family` |

## Sources

- [ByteDance Seedream 4.5 product](https://seed.bytedance.com/en/seedream4_5)
- [Ark model list](https://docs.volcengine.com/docs/ark/model-list?lang=en)
- [Ark Seedream comparison](https://docs.volcengine.com/docs/ark/image-generation-tutorial?lang=en)
- [Ark deprecation notice](https://docs.volcengine.com/docs/ark/model-deprecation-notice?lang=zh)
- [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list)
- [BytePlus image API](https://docs.byteplus.com/en/docs/modelark/image-generation-api)
- [BytePlus pricing](https://docs.byteplus.com/en/docs/modelark/model-pricing)
