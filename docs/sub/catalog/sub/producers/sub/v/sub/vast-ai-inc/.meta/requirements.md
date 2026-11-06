# Documentation Requirements

## Requirements

- Identify Vast.ai Inc. as the producer/operator organization behind the Vast.ai infrastructure marketplace/service.
- Preserve the legal company form only as supported by current official Vast.ai legal/privacy documents; do not conflate independent marketplace hosts, infrastructure suppliers, or affiliates with the canonical producer identity.
- Keep the producer profile distinct from the Vast.ai hosted service and from independent compute providers participating in the marketplace.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep funding, employee counts, host counts, GPU inventory, geographic coverage, pricing, and other mutable company/service metrics outside this concise producer profile unless materially relevant to represented catalog entities.
- Include the current official site and legal/privacy identity sources from canonical entity metadata.

## Validation

- The page distinguishes Vast.ai Inc. from the Vast.ai service and independent marketplace hosts.
- The `produces` relation resolves to Vast.ai and is matched by Vast.ai's inverse `produced-by` relation.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Producer evidence and reader projection

- Render the canonical entity name as the title and the source-backed `identity_note` as concise identity and operating-boundary prose.
- Preserve the existing ID, type and aliases. Historical authorship, current stewardship, corporate ownership and service operation must remain distinct where the note distinguishes them.
- Render every visible validated canonical relation exactly once through `entity-relations`, with canonical target names and resolving relative links. Distinct relation types to one target remain distinct rows.
- Render the canonical official references with descriptive labels; keep release, licensing, access and data-processing claims bounded to the cited sources.
- Keep detailed model, software, service and benchmark behavior on the related owner pages; do not infer new catalog membership from a provider inventory.

## Review checks

- The complete reader agrees with the canonical note and relation projection, including operational caveats.
- Every direct relation has its exact canonical inverse and every rendered destination resolves to its canonical owner.
