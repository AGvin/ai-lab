# Documentation Requirements

## Identity and provenance

- Seedream is ByteDance Seed's image-generation and image-editing model family. Concrete releases have different capabilities and hosted access contracts; the family is distinct from ByteDance's apps, API providers and other model families.
- ByteDance Seed produces the released Seedream 4.0 and 5.0 Pro models represented here. Seedance, SeedAudio and consumer products have separate identities. [ByteDance Seed models](https://seed.bytedance.com/en/models) [Seedream 4.0 release](https://seed.bytedance.com/en/blog/seedream-4-0-officially-released-beyond-drawing-into-imagination) [Seedream 5.0 Pro release](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro).

## Route-specific lifecycle

**Check the exact provider, region and route before new integration.** Volcengine's main Ark API notice sets EOM to 2026-09-24 and EOS to 2026-11-24 14:00 (UTC+8) for the listed 4.0-250828, 4.5-251128 and Lite-260128 routes; Lite's two ID spellings are aliases. LAS separately schedules service termination for 2026-11-18. These are hosted-route notices, not a global retirement of all Seedream model identities. [Ark notice](https://docs.volcengine.com/docs/ark/model-deprecation-notice?lang=zh) [LAS notice](https://docs.volcengine.com/docs/lake-ai-service/operator-service-discontinuation-announcement-5th?lang=zh).

BytePlus deactivated Lite in eu-west-1 on 2026-09-10 and directs users to ap-southeast-1. Volcengine Agent Plan separately retired its Lite route on 2026-10-12. Do not apply those dates to another region/API or silently substitute Pro: batch, search and editing capabilities differ. Recheck current notices and test the chosen replacement. [BytePlus regions](https://docs.byteplus.com/en/docs/modelark/model-deprecation-notice) [Agent Plan](https://docs.volcengine.com/docs/ark/agent-plan-personal-model-deprecation-announcement?lang=en).

## Operational decision boundaries

- Choose the exact model and provider route for batch generation, editing, search, output resolution and rights. In particular, current 5.0 Pro serving features do not automatically inherit 4.0 batch behavior or 5.0 Lite search capabilities. [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310) [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523) [Seedream 5.0 Lite release](https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite).
- The family record establishes provenance and navigation. It does not imply downloadable weights, one license, a shared parameter count or identical regional availability. [ByteDance Seed models](https://seed.bytedance.com/en/models) [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
