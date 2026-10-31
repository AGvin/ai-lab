# Documentation Requirements

## Requirements

- Identify Portkey AI Gateway as an open-source AI model gateway for unified model/provider access, routing, fallbacks, load balancing, caching, guardrails, and related gateway controls.
- Preserve its primary placement under `gateways/model-gateways`; the gateway mediates access to external model providers rather than owning the underlying model APIs.
- Preserve Portkey, Inc. as the direct product producer identity while recording Palo Alto Networks as Portkey, Inc.'s current corporate owner through the producer layer rather than changing the software's `produced-by` relation.
- Distinguish the open-source/self-hostable Portkey AI Gateway runtime from the current producer-operated Prisma AIRS AI Gateway commercial service surface after Palo Alto Networks' 2026 acquisition of Portkey.
- Do not materialize Prisma AIRS AI Gateway as a service from this page before the stabilized AI-security taxonomy proposal is explicitly approved.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep provider/model counts, benchmark claims, roadmap details, and other mutable product facts source-backed when expanded.
- Include current official Portkey Gateway documentation/repository/legal references and first-party Palo Alto acquisition/current-commercial-surface references.

## Validation

- The page describes the open-source gateway runtime without conflating it with Prisma AIRS or the broader Palo Alto Networks commercial platform.
- `produced-by` still targets Portkey, Inc., not Palo Alto Networks.
- Vendor benchmark and scale claims are not presented as independent AI Lab evaluation.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
- No new service category or Prisma AIRS service entity is created by this change.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
