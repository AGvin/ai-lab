# Documentation Requirements

## Requirements

- Identify Xiaomi MiMo Team as the canonical producing team for the represented MiMo model family.
- Keep team identity distinct from Xiaomi corporate/product surfaces, MiMo API/Studio products, and individual model checkpoints.
- Use first-party MiMo site and official model registry as provenance sources.
- Render the standard `entity-relations` block from validated relation state.

## Validation

- The MiMo family `produced-by` relation has the matching `produces` inverse here.
- No unsupported corporate parent relation is inferred merely from the Xiaomi brand.

## Producer evidence and reader projection

- Render the canonical entity name as the title and the source-backed `identity_note` as concise identity and operating-boundary prose.
- Preserve the existing ID, type and aliases. Historical authorship, current stewardship, corporate ownership and service operation must remain distinct where the note distinguishes them.
- Render every visible validated canonical relation exactly once through `entity-relations`, with canonical target names and resolving relative links. Distinct relation types to one target remain distinct rows.
- Render the canonical official references with descriptive labels; keep release, licensing, access and data-processing claims bounded to the cited sources.
- Keep detailed model, software, service and benchmark behavior on the related owner pages; do not infer new catalog membership from a provider inventory.

## Review checks

- The complete reader agrees with the canonical note and relation projection, including operational caveats.
- Every direct relation has its exact canonical inverse and every rendered destination resolves to its canonical owner.
