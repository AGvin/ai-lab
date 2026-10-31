# Seedream

Seedream is ByteDance Seed's image-generation and image-editing model family. Concrete releases have different capabilities and hosted access contracts; the family is distinct from ByteDance's apps, API providers and other model families. [ByteDance Seed models](https://seed.bytedance.com/en/models) [Seedream 4.0 release](https://seed.bytedance.com/en/blog/seedream-4-0-officially-released-beyond-drawing-into-imagination) [Seedream 5.0 Pro release](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro).

## Identity and scope

ByteDance Seed produces the released Seedream 4.0, 4.5, 5.0 Lite, 5.0 Pro and 5.0 Flash models represented here. Seedance, SeedAudio and consumer products have separate identities. [ByteDance Seed models](https://seed.bytedance.com/en/models) [Seedream 4.0 release](https://seed.bytedance.com/en/blog/seedream-4-0-officially-released-beyond-drawing-into-imagination) [Seedream 5.0 Pro release](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) [Flash release bulletin](https://docs.byteplus.com/en/docs/modelark/model-release-announcement) [Seedream 4.5 product page](https://seed.bytedance.com/en/seedream4_5) [Seedream 5.0 Lite launch](https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite).

## Route-specific lifecycle

**Check the exact provider, region and route before new integration.** Volcengine's main Ark API notice sets EOM to 2026-09-24 and EOS to 2026-11-24 14:00 (UTC+8) for the listed 4.0-250828, 4.5-251128 and Lite-260128 routes; Lite's two ID spellings are aliases. LAS separately schedules service termination for 2026-11-18. These are hosted-route notices, not a global retirement of all Seedream model identities. [Ark notice](https://docs.volcengine.com/docs/ark/model-deprecation-notice?lang=zh) [LAS notice](https://docs.volcengine.com/docs/lake-ai-service/operator-service-discontinuation-announcement-5th?lang=zh).

BytePlus deactivated Lite in eu-west-1 on 2026-09-10 and directs users to ap-southeast-1; its generic model list still mentions Lite EU-West support, so follow the dated deactivation notice and verify the live account/region rather than assuming the list is current. Volcengine Agent Plan separately retired its Lite route on 2026-10-12. Do not apply those dates to another region/API or silently substitute Pro: batch, search and editing capabilities differ. Recheck current notices and test the chosen replacement. [BytePlus regions](https://docs.byteplus.com/en/docs/modelark/model-deprecation-notice) [Agent Plan](https://docs.volcengine.com/docs/ark/agent-plan-personal-model-deprecation-announcement?lang=en).

## Use and limitations

Choose the exact model and provider route for batch generation, editing, search, output resolution and rights. In particular, current 5.0 Pro serving features do not automatically inherit 4.0 batch behavior or 5.0 Lite search capabilities. [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310) [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523) [Seedream 5.0 Lite release](https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite).

Seedream 4.5 and 5.0 Lite are separate released models, not aliases for Pro or Flash. The older dated provider routes support sequential multi-image batches; 4.5 focuses on multi-image editing and typography while Lite introduces reasoning-oriented creation and optional web-search enhancement. Check route support and pending Ark retirement before adopting either. [4.5 product](https://seed.bytedance.com/en/seedream4_5) [Lite launch](https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite) [Ark comparison](https://docs.volcengine.com/docs/ark/image-generation-tutorial?lang=en).

Seedream 5.0 Flash is a separately announced September 2026 hosted model with distinct provider-specific route IDs. Its standard optimization, interactive editing and layer decomposition should not be confused with Lite/4.5 sequential-image generation or Pro's additional fast optimization mode. Weight lineage relative to Pro is not disclosed. [BytePlus release bulletin](https://docs.byteplus.com/en/docs/modelark/model-release-announcement) [BytePlus Pro/Flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro) [BytePlus image generation API](https://docs.byteplus.com/en/docs/modelark/image-generation-api).

The family record establishes provenance and navigation. It does not imply downloadable weights, one license, a shared parameter count or identical regional availability. [ByteDance Seed models](https://seed.bytedance.com/en/models) [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `produced-by` | [ByteDance Seed](../../../../../producers/sub/b/sub/bytedance-seed/README.md) | `team` |
| `has-member` | [Seedream 4.0](sub/models/sub/seedream-4-0/README.md) | `model` |
| `has-member` | [Seedream 4.5](sub/models/sub/seedream-4-5/README.md) | `model` |
| `has-member` | [Seedream 5.0 Lite](sub/models/sub/seedream-5-0-lite/README.md) | `model` |
| `has-member` | [Seedream 5.0 Pro](sub/models/sub/seedream-5-0-pro/README.md) | `model` |
| `has-member` | [Seedream 5.0 Flash](sub/models/sub/seedream-5-0-flash/README.md) | `model` |

## Sources

- [ByteDance Seed models](https://seed.bytedance.com/en/models)
- [Seedream 4.0 release](https://seed.bytedance.com/en/blog/seedream-4-0-officially-released-beyond-drawing-into-imagination)
- [Seedream 5.0 Pro release](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro)
- [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310)
- [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523)
- [Seedream 5.0 Lite release](https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite)
- [Seedream 4.5 product](https://seed.bytedance.com/en/seedream4_5)
- [Volcengine Ark image model comparison](https://docs.volcengine.com/docs/ark/image-generation-tutorial?lang=en)
- [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list)
- [BytePlus Flash release bulletin](https://docs.byteplus.com/en/docs/modelark/model-release-announcement)
- [BytePlus Seedream Pro/Flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro)
