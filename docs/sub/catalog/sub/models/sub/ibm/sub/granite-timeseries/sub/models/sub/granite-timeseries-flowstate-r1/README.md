# Granite TimeSeries FlowState R1

Granite TimeSeries FlowState R1 is **one concrete IBM time-series forecasting model identity**, with two represented chronological releases. The official repository loads Version 1.0 by default; Version 1.1 requires the explicit Hugging Face selector `revision="r1.1"`.

## Operating guidance

IBM currently describes FlowState as supporting **zero-shot forecasting**. Choose `scale_factor` using the input sampling rate and seasonality rather than a universal setting. The official card recommends forecasting no more than **30 seasons**, since quality declines past that horizon. Measure accuracy on the target series, sampling frequencies and forecasting horizons; these are source-scoped recommendations, not runtime guarantees.

The official card describes its published weights as suitable for commercial and enterprise use, while separately linking a research version intended for research use only. Confirm the selected weights, license and runtime before use; do not infer release-specific context, parameter count or architecture from the model-wide identity.

## Chronological releases

- [Version 1.0 — default release](./sub/versions/sub/r1-0/)
- [Version 1.1 — explicit `r1.1` revision](./sub/versions/sub/r1-1/)
- [All represented versions](./sub/versions/)

Version-specific training-data changes, architecture, context windows and hyperparameters are documented on the respective release pages.

## Translations

- English

## Relations

- Member of: [Granite TimeSeries](../../../../)

## Official resources

- [IBM Granite TimeSeries FlowState R1](https://huggingface.co/ibm-granite/granite-timeseries-flowstate-r1)
