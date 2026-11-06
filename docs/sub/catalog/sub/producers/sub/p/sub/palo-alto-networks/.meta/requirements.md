# Documentation Requirements

## Requirements

- Identify Palo Alto Networks, Inc. as the current corporate owner of Portkey, Inc. following completion of the Portkey acquisition on May 29, 2026.
- Keep the corporate owner identity distinct from Portkey, Inc., the open-source Portkey AI Gateway software, and producer-operated Prisma AIRS / Prisma AIRS AI Gateway service surfaces.
- Do not imply that Palo Alto Networks directly authored the historical Portkey open-source gateway solely because it acquired Portkey, Inc.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current first-party corporate, acquisition, and Prisma AIRS AI Gateway references supporting ownership and current commercial context.

## Validation

- `owns` is the inverse of Portkey, Inc.'s `owned-by` relation.
- Corporate ownership does not collapse Portkey, Inc., the open-source gateway, or Prisma AIRS service identities into one entity.
- No unapproved Prisma AIRS service entity or new taxonomy category is materialized by this producer page.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Palo Alto Networks is the security company behind the represented Prisma AIRS service. Its first-party announcement records the completed acquisition of Portkey on May 29, 2026; the subsequent Prisma AIRS AI Gateway announcement describes the commercial integration of Portkey technology. These are separate product and ownership relationships. [Acquisition announcement](https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-completes-acquisition-portkey-secure-ai) · [Gateway announcement](https://www.paloaltonetworks.com/blog/2026/07/announcing-general-availability-of-prisma-airs-ai-gateway/).

The represented Prisma AIRS service supplies commercial security controls around AI applications. Assess the purchased service, supported integration points and traffic policy before adopting it; the corporate acquisition does not establish that every Portkey feature or deployment is included in a Prisma AIRS subscription. [Gateway announcement](https://www.paloaltonetworks.com/blog/2026/07/announcing-general-availability-of-prisma-airs-ai-gateway/).

Portkey's separately published gateway repository declares MIT licensing. That license applies to the repository software, while the security service, model-provider access and customer deployment remain separate operating boundaries. [Gateway repository](https://github.com/Portkey-AI/gateway).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
