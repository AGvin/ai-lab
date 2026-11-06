# Documentation Requirements

## Requirements

- Identify this page as version 1.0, the default/original represented release of Granite TimeSeries FlowState R1.
- Preserve the first-party loading boundary that omitting the revision selector loads version 1.0.
- Scope the 2048-step context and the current default-repository 9.07M parameter surface to version 1.0 rather than generalizing them across all represented FlowState releases.
- Do not project version 1.1 changes in pretraining data, S5 output gating, hyperparameters, MLP size, context, or parameter count onto version 1.0.
- Keep shared zero-shot forecasting, sampling-rate/seasonality scaling, and forecast-horizon guidance on the parent model unless a release-specific difference is established.

## Validation

- The `version-of` relation resolves to Granite TimeSeries FlowState R1.
- Version 1.0 is not presented as a separate parameter-size model family or series.
- Release-specific facts are not duplicated as universal parent-model facts.
