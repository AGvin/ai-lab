# Granite TimeSeries FlowState R1 Version 1.1

Version 1.1 is a distinct chronological release of IBM Granite TimeSeries FlowState R1, **not** a new model family or parameter-size model. It requires the explicit Hugging Face revision selector `revision="r1.1"`.

## Release-specific changes

Compared with the original/default Version 1.0, Version 1.1 introduces:

- updated pretraining data;
- a 4096-step context;
- S5 output gating;
- optimized hyperparameters and a larger MLP;
- approximately 18.5 million total parameters.

These details describe Version 1.1 only; the default repository state remains Version 1.0. Published benchmark or quality claims are provider-reported unless independently reproduced. Parent-level zero-shot forecasting and horizon guidance should not be restated as release-specific changes.

## Parent and official source

- [Granite TimeSeries FlowState R1](../../../../)
- [Official Version 1.1 revision](https://huggingface.co/ibm-granite/granite-timeseries-flowstate-r1/tree/r1.1)
