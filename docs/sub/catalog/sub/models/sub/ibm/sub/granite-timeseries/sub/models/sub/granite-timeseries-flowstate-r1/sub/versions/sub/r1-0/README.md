# Granite TimeSeries FlowState R1 Version 1.0

Version 1.0 is the original and default release of IBM Granite TimeSeries FlowState R1. The official repository loads this release **when no revision selector is supplied**.

## Release-specific profile

- **Context:** 2048 time steps.
- **Parameters:** approximately 9.07 million for the default repository checkpoint.
- **Loading:** use the official FlowState R1 repository without specifying `revision="r1.1"`.

These specifications belong to version 1.0 only. Do not transfer changes introduced in version 1.1, including its different training data, S5 output gating, larger MLP and context, to this release.

Shared zero-shot forecasting behavior, seasonality/sampling-rate scaling and horizon recommendations are documented on the parent model. Benchmark comparisons must identify the precise version and source.

## Parent and official source

- [Granite TimeSeries FlowState R1](../../../../)
- [IBM FlowState R1 repository — default Version 1.0](https://huggingface.co/ibm-granite/granite-timeseries-flowstate-r1)
