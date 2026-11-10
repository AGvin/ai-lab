# Documentation Requirements

## Identity and provenance

- Seedream 5.0 Pro is ByteDance Seed's image-generation and editing model released on 2026-07-08, with design-oriented layout, interactive editing and layer-decomposition workflows. Its hosted service identifiers are access routes rather than separate model identities.
- The official release and product page establish a distinct named model, not a silent relabeling of Seedream 4.0. Keep design, multilingual text and local-editing capabilities separate from a claim of perfectly accurate or pixel-consistent output. [Seedream 5.0 Pro release](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) [Seedream 5.0 Pro product page](https://seed.bytedance.com/en/seedream5_0_pro).
- BytePlus names this model Dola Seedream 5.0 Pro and lists dola-seedream-5-0-pro-260628. The provider prefix and versioned identifier are serving labels; the release date remains the official 2026-07-08 announcement. [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310) [BytePlus Seedream 5.0 Pro and Flash tutorial](https://docs.byteplus.com/en/docs/ModelArk/seedream-5-0-pro).

## Operational decision boundaries

- The reviewed BytePlus contract supports single-image generation from up to ten references or decomposition of one image into one base image and up to sixteen layers. It currently does not support sequential image batches, streaming output or web search for Pro. [BytePlus Seedream 5.0 Pro and Flash tutorial](https://docs.byteplus.com/en/docs/ModelArk/seedream-5-0-pro) [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523).
- That service offers 1K, 1.5K and 2K tiers for Pro, with explicit pixel-product and aspect-ratio constraints. Do not inherit 4.0's 4K tier or 5.0 Lite's search support from their shared family name. [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523).
- Interactive markers and layer editing still require review: ByteDance identifies fine text and pixel-consistent edits as remaining challenges. Layer requests can fail as a whole if one layer fails; saved PNG alpha channels and returned layer positions matter for reconstruction. [Seedream 5.0 Pro release](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) [BytePlus Seedream 5.0 Pro and Flash tutorial](https://docs.byteplus.com/en/docs/ModelArk/seedream-5-0-pro) [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523).
- Current hosted access requires the selected service's activation, credentials and terms. Image URLs last 24 hours; save outputs and layer metadata. No public parameter count, downloadable weights or open-weight license was established by this review. [Seedream 5.0 Pro product page](https://seed.bytedance.com/en/seedream5_0_pro) [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310) [BytePlus Seedream 5.0 Pro and Flash tutorial](https://docs.byteplus.com/en/docs/ModelArk/seedream-5-0-pro) [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
