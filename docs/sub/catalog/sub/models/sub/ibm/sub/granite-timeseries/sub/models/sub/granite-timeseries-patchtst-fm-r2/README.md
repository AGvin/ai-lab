# Granite TimeSeries PatchTST-FM R2

Granite TimeSeries PatchTST-FM R2 is a concrete IBM Granite zero-shot forecasting model. IBM describes it as the successor to PatchTST-FM R1 with architectural changes, expanded training data, probabilistic forecasting, and an 8192-step training context.

Unlike the aggregate FlowState, TSPulse, and TTM release surfaces in this catalog, this R2 node represents one released trained-model identity. PatchTST-FM R1 is a separate predecessor rather than an alias.

## License and operating boundaries

The current [IBM model card](https://huggingface.co/ibm-granite/granite-timeseries-patchtst-fm-r2) offers a choice of OpenMDW 1.0 or Apache 2.0, despite its metadata listing only OpenMDW. Its usage example requires `granite-tsfm>=0.3.9`. The 8192-step figure describes training context, not a guarantee for arbitrary input lengths or forecast horizons. Validate the selected context, horizon, quantiles, and data preparation on the intended workload; runtime compatibility and forecast quality have not been tested here. Published benchmark results are source-reported, not locally reproduced.

## Translations

- English

## Relations

- Member of: [`catalog/models/ibm/granite-timeseries`](../../../../)

## Official resources

- <https://huggingface.co/ibm-granite/granite-timeseries-patchtst-fm-r2>
