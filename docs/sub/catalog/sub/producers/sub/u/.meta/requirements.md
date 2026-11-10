# Documentation Requirements

## Requirements

- Provide the alphabetical producer index for materialized canonical producers in the stable `u` slug partition.
- Render the standard `child-navigation` block from the validated materialized direct-child projection.
- Keep the page concise and navigational.
- Use the canonical entity name for each child label and sort by that name, with canonical ID as a deterministic tie-breaker. A changed public or legal name does not itself move a stable producer ID to another partition.
- Do not create absent letter indexes or additional producer nodes to make alphabetical coverage symmetric.

## Validation

- Every direct materialized producer under this index is rendered exactly once through the canonical child projection.
- Every rendered producer belongs to the U index.
- The index does not duplicate model, software, or service profiles.
