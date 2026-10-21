# Documentation Requirements

## Requirements

- Identify the independent Vespa.ai organization that develops Vespa and operates Vespa Cloud, following the 2023 Yahoo spin-out; keep historical Yahoo origin and present production stewardship distinct.
- Use official documentation and upstream repository organizations for product identity and lifecycle evidence.
- Differentiate released OSS/self-hosted offerings from provider-managed, cloud-only, and enterprise-only offerings.
- Keep mutable releases, licensing, service tiers, availability, performance, and platform capabilities source-backed.

## Validation

- Current official producer identity matches the cited upstream organization and documentation.
- Every `produces` relation reciprocates a `produced-by` relation in a materialized canonical child.
- Historical company history and hosted deployment offerings do not create duplicate producer identities.

## Producer evidence and reader projection

- Render the canonical entity name as the title and the source-backed `identity_note` as concise identity and operating-boundary prose.
- Preserve the existing ID, type and aliases. Historical authorship, current stewardship, corporate ownership and service operation must remain distinct where the note distinguishes them.
- Render every visible validated canonical relation exactly once through `entity-relations`, with canonical target names and resolving relative links. Distinct relation types to one target remain distinct rows.
- Render the canonical official references with descriptive labels; keep release, licensing, access and data-processing claims bounded to the cited sources.
- Keep detailed model, software, service and benchmark behavior on the related owner pages; do not infer new catalog membership from a provider inventory.

## Review checks

- The complete reader agrees with the canonical note and relation projection, including operational caveats.
- Every direct relation has its exact canonical inverse and every rendered destination resolves to its canonical owner.
