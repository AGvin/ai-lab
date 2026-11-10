# Documentation Requirements

## Identity and provenance

- Seedream 4.5 is ByteDance Seed's distinct released image-generation and image-editing model. The first-party product page documents multi-reference consistency, target preservation and typography-focused enhancements, with internal MagicBench claims; those are not independent AI Lab tests. [Seedream 4.5 product page](https://seed.bytedance.com/en/seedream4_5).
- Volcengine's dated model ID is `doubao-seedream-4-5-251128`; BytePlus lists `seedream-4-5-251128`. Treat these as provider route IDs for the one named model, not separate trained checkpoints. A suffix alone does not establish an exact public release date or training/weight ancestry. [Ark model list](https://docs.volcengine.com/docs/ark/model-list?lang=en) [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list).

## Hosted access and lifecycle — warning

- **Do not start a new integration on the retiring Ark 4.5 route.** Ark's tenth deprecation batch sets EOM `2026-09-24 10:00 UTC+8` and EOS `2026-11-24 14:00 UTC+8` for the named dated route. Pro is suggested as replacement; batch, editing, cost and output properties must be compared and tested rather than assumed equivalent. This is a provider-service lifecycle, not proof that released model provenance or independently hosted weights globally disappeared. [Ark deprecation](https://docs.volcengine.com/docs/ark/model-deprecation-notice?lang=zh).
- Source-backed image use cases include prompt-to-image, editing from one/multiple references and sequential group generation, with the exact input/output constraints depending on the provider. Check resolution and batch API parameters before use. [Seedream 4.5 product](https://seed.bytedance.com/en/seedream4_5) [Ark tutorial](https://docs.volcengine.com/docs/ark/image-generation-tutorial?lang=en) [BytePlus image generation API](https://docs.byteplus.com/en/docs/modelark/image-generation-api).
- BytePlus currently lists 4.5 in its ap-southeast-1 model catalog and price list; this does **not** establish availability in every region or retention after future changes. Output images are charged per successful image, including grouped generation; verify current live account availability and pricing rather than caching a rate as model metadata. [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list) [BytePlus pricing](https://docs.byteplus.com/en/docs/modelark/model-pricing).
- No public parameter count, downloadable checkpoint rights, weight lineage, independent benchmark or ultimate beneficial-ownership determination was established. Provenance-review pending must not be treated as Russian Tier 1/2 without verified source evidence. [Seedream 4.5 product](https://seed.bytedance.com/en/seedream4_5).

## Validation

- Preserve unique canonical identity and reciprocal family membership. Keep historical existence distinct from provider/region/model-route availability; no new parent producer or 4.5 derivative relation.
- Render complete reader from these requirements with exact local links and source-supported risk statements. No inference, all-region availability, model freshness marker, global cache/CI, clean research cycle or publication gate credit from scoped authoring alone.
