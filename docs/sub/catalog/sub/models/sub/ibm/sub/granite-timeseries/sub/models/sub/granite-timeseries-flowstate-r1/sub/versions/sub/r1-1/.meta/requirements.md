# Documentation Requirements

## Requirements

- Identify this page as version 1.1 of Granite TimeSeries FlowState R1 and preserve the explicit `revision="r1.1"` loading boundary.
- Scope the first-party version 1.1 changes to this release: updated pretraining data, 4096-step context, S5 output gating, optimized hyperparameters, a larger MLP, and 18.5M total parameters.
- Keep those release deltas separate from model-wide FlowState facts and from the default version 1.0 state.
- Treat release-specific benchmark or quality claims as provider-reported evidence unless independently reproduced.
- Keep shared zero-shot forecasting, sampling-rate/seasonality scaling, and forecast-horizon guidance on the parent model unless a release-specific difference is established.

## Validation

- The `version-of` relation resolves to Granite TimeSeries FlowState R1.
- Version 1.1 is not presented as a different parameter-size family or unrelated model.
- The page does not generalize 4096 context or 18.5M parameters to version 1.0.
