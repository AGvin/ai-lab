# Documentation Requirements

## Requirements

- Identify Qualcomm as the canonical producer organization for the represented Qualcomm Dragonfly AI200 accelerator.
- Keep Snapdragon client/mobile SoCs, Dragonfly data-center CPUs/accelerators, software stacks, complete rack systems, and third-party products as separate product boundaries.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The `produces` relation is the inverse of Qualcomm Dragonfly AI200 `produced-by`.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Qualcomm is the producer associated with the represented Dragonfly AI200 data-center inference accelerator. Its first-party data-center catalog distinguishes accelerator products from complete system configurations, CPUs and the accompanying software platform. [AI200 product page](https://www.qualcomm.com/data-center/products/qualcomm-dragonfly-ai200) · [Data-center catalog](https://www.qualcomm.com/data-center/products).

The AI200 listing is marked Active and directs buyers to Contact Sales. Treat that as a sales-led product status; establish the offered configuration, delivery terms, runtime/model support and power or cooling requirements for the actual deployment. Vendor efficiency or TCO comparisons require the stated workload and hardware assumptions before they can inform a purchase. [AI200 product page](https://www.qualcomm.com/data-center/products/qualcomm-dragonfly-ai200).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
