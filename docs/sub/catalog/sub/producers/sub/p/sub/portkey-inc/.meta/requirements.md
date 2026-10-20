# Documentation Requirements

## Requirements

- Identify Portkey, Inc. as the organization behind the represented open-source Portkey AI Gateway and as an organization currently owned by Palo Alto Networks, Inc. following completion of the May 29, 2026 acquisition.
- Keep Portkey, Inc. distinct from Palo Alto Networks, Inc., the open-source gateway runtime, and the current producer-operated Prisma AIRS / Prisma AIRS AI Gateway commercial service surfaces.
- Preserve the `produces` relation to the open-source Portkey AI Gateway and the inverse `owned-by` relation to Palo Alto Networks.
- Do not create a separate current hosted Portkey service identity when first-party current material presents Portkey's commercial gateway surface as Prisma AIRS AI Gateway.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current first-party legal, repository, acquisition, and current-commercial-surface references supporting provenance.

## Validation

- Portkey, Inc., Palo Alto Networks, the open-source gateway, and Prisma AIRS service surfaces are not collapsed into one entity.
- `owned-by` is the inverse of Palo Alto Networks' `owns` relation.
- The producer relation does not imply that the software itself owns downstream model-provider APIs.
- No unapproved Prisma AIRS service entity or new taxonomy category is materialized by this producer page.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Portkey, Inc. is the publishing company associated with the Portkey AI Gateway repository. Palo Alto Networks' May 29, 2026 announcement confirms its completed acquisition of Portkey, while the July gateway announcement documents the resulting Prisma AIRS commercial integration. [Portkey site terms](https://portkey.ai/terms) · [Acquisition announcement](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-completes-acquisition-portkey-secure-ai).

The gateway repository is MIT-licensed software for routing model requests. A self-managed deployment and the current Prisma AIRS commercial gateway have separate software and service-contract boundaries. Evaluate the selected gateway's credential storage, provider routing and logging; upstream model access and its data terms remain relevant even when a gateway exposes a common interface. [Gateway repository](https://github.com/Portkey-AI/gateway) · [Prisma AIRS integration](https://www.paloaltonetworks.com/blog/2026/07/announcing-general-availability-of-prisma-airs-ai-gateway/).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
