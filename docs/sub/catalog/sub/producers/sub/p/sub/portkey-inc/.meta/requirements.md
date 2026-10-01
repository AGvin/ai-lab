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
