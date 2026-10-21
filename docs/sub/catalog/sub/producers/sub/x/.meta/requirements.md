# Documentation Requirements

## Requirements

- Provide the alphabetical producer index for materialized canonical producers in the stable `x` slug partition.
- Render the standard child-navigation block from the validated direct-child projection so every materialized canonical producer under this index appears exactly once.
- Keep the page concise and navigational.
- Use the canonical entity name for each child label and sort by that name, with canonical ID as a deterministic tie-breaker. A changed public or legal name does not itself move a stable producer ID to another partition.
- Do not create absent letter indexes or additional producer nodes to make alphabetical coverage symmetric.

## Validation

- The child-navigation block matches the validated materialized direct-child projection and every destination resolves to a canonical producer node.
- No producer outside the X index is presented.
- The index does not duplicate model, software, or service profiles.
