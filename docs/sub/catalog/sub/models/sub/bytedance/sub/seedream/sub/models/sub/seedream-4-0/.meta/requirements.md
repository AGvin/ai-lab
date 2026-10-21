# Documentation Requirements

## Identity and provenance

- Seedream 4.0 is ByteDance Seed's image-generation and general-purpose editing model, officially released on 2025-09-09. Its unified architecture accepts text and reference images and supports related-image generation workflows.
- The released 4.0 model supports text-to-image, image editing, visual conditioning, multi-image references and output up to the advertised 4K tier. Product demonstrations and historical rankings are ByteDance claims. [Seedream 4.0 release](https://seed.bytedance.com/en/blog/seedream-4-0-officially-released-beyond-drawing-into-imagination) [Seedream 4.0 product page](https://seed.bytedance.com/en/seedream4_0).
- BytePlus currently lists seedream-4-0-250828 as its service identifier. This dated endpoint label is not the public release date and does not create another learned-model node by itself. [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310).

## Operational decision boundaries

- In the reviewed BytePlus API, 4.0 supports one image or sequential batches. Multi-reference requests accept up to fourteen input images, with total input plus generated images at most fifteen; resolution tiers include 1K, 2K and 4K. These limits belong to that service revision. [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523).
- API activation, credentials, region, billing and endpoint controls are service concerns. Generated-image URLs expire within 24 hours and should be saved promptly; the watermark parameter defaults to true in the documented API. [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310) [BytePlus image generation API](https://docs.byteplus.com/en/docs/ModelArk/1541523).
- The sources reviewed do not establish public model weights, a parameter count or a reusable open-weight license. Factual content, text rendering and reference fidelity need review; old product benchmark positions are not a current independent evaluation. [Seedream 4.0 release](https://seed.bytedance.com/en/blog/seedream-4-0-officially-released-beyond-drawing-into-imagination) [Seedream 4.0 product page](https://seed.bytedance.com/en/seedream4_0) [BytePlus ModelArk model list](https://docs.byteplus.com/en/docs/ModelArk/1330310).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
