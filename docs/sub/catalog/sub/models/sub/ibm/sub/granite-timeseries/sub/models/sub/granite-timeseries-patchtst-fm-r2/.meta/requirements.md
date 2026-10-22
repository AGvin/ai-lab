# Documentation Requirements

## Requirements

- Keep PatchTST-FM R2 as a concrete Granite Time Series forecasting model, not an aggregate series node.
- Preserve its explicit continuation from PatchTST-FM R1, probabilistic forecasting behavior, model size, architecture, training-data, license, revision, and benchmark claims only from current first-party sources.
- Treat PatchTST-FM R1 as a distinct predecessor release rather than an alias of R2; it remains outside the current materialized scope unless separately qualified and materialized.
- State the current model card's dual-license choice (OpenMDW 1.0 or Apache 2.0); do not reduce it to the metadata's single license tag.
- Scope the 8192-step context to training, preserve the documented Granite-TSFM minimum version, and require workload-specific forecasting validation without claiming local runtime or benchmark reproduction.

## Validation

- Membership resolves to Granite Time Series.
- This node remains type `model`; FlowState R1 is also a concrete model with chronological version nodes, while TSPulse R1 and TTM R3 retain series-level identity.
