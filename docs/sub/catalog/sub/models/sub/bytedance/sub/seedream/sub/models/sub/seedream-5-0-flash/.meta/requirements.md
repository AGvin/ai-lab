# Documentation Requirements

## Identity and provenance

- Seedream 5.0 Flash is a separately announced ByteDance image-generation model in the September 2026 Volcengine/BytePlus release lists. Volcengine calls its service `doubao-seedream-5-0-flash-260915`; BytePlus uses `dola-seedream-5-0-flash-260915`. These are provider route IDs for one named model, not two independently accepted checkpoints. [Volcengine release](https://docs.volcengine.com/docs/ark/model-release-announcement?lang=zh) [BytePlus release](https://docs.byteplus.com/en/docs/modelark/model-release-announcement).
- Keep the producer as ByteDance Seed via the Seedream family. Neither the September announcements nor the reviewed API guides establish downloadable weights, parameter count, model architecture, a trained-from-Pro relation or independent quality/speed benchmark. [BytePlus Pro/Flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro).

## Access and capability boundaries

- Flash supports text-to-image and image-reference editing, interactive editing by markers/coordinates, native multilingual generation, and decomposition of one input into one base image and up to sixteen layers. The provider lists 1K/1.5K/2K output tiers and PNG/JPEG; Flash has standard prompt optimization but not Pro's additional fast prompt-optimization mode. This is documented feature support, not independently tested accuracy. [BytePlus Pro/Flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro).
- The reviewed BytePlus route supports up to ten input reference images and does not support sequential batch images, web-search enhancement or streamed output. A published account/model limit is 500 IPM, not a verified sustained throughput. Do not inherit 4.0/Lite batch/search behavior or assume Flash is a drop-in replacement for those routes. [BytePlus image API](https://docs.byteplus.com/en/docs/modelark/image-generation-api) [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list).
- Generated image URLs expire after 24 hours. Persist intended output, alpha-bearing PNG layers and layer position/order metadata; reconstruct and review the composited result before production use. Provider activation, region eligibility, content/rights terms and current pricing must be verified for the chosen account. BytePlus currently scopes its ModelArk listed models to ap-southeast-1; do not infer global access. [BytePlus image API](https://docs.byteplus.com/en/docs/modelark/image-generation-api) [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list).
- BytePlus describes Flash as faster and cheaper, while positioning Pro for higher quality. Those are vendor comparisons, not AI Lab measurements. Pricing is mutable and belongs to provider terms at selection time. [BytePlus Pro/Flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro) [BytePlus pricing](https://docs.byteplus.com/en/docs/modelark/model-pricing).
- Existing 4.0/4.5/Lite route retirement notices are provider/region-specific and must not be applied to Flash without a matching source. Beneficial ownership/partial Russian equity has not been resolved in this review: retain provenance review pending, never invent Tier 1/Tier 2 ties. [BytePlus model list](https://docs.byteplus.com/en/docs/modelark/model-list).

## Validation

- Preserve one canonical Flash model identity, the exact `member-of` / `has-member` inverse pair and its family/producer hierarchy. Do not invent a series or derivative relation.
- Render a complete reader with correct scoped links, limitations and explicit source attribution. Do not imply local weights, independent benchmark, finalized beneficial ownership or global freshness/CI acceptance.
