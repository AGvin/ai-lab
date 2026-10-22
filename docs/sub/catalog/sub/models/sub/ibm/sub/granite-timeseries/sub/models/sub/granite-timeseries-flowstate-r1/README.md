# Granite TimeSeries FlowState R1

Granite TimeSeries FlowState R1 is an IBM Granite Time Series release surface represented as a model series. The official repository exposes the original r1.0 state by default and a materially updated r1.1 state through an explicit Hugging Face revision selector.

The r1.1 update changes pretraining data, context, architecture details, hyperparameters, and parameter count. Those revision states remain inside this stable series identity for now rather than being counted as extra catalog nodes.

## Operating guidance

The current first-party card states that FlowState currently supports zero-shot forecasting. It recommends choosing `scale_factor` from the input sampling rate and seasonality rather than assuming one scale works universally, and recommends forecasting no more than 30 seasons because quality declines beyond that horizon.

The Granite card describes these weights as suitable for commercial and enterprise use and links a separate research version intended for research use only. Keep release-specific benchmark conclusions scoped to the exact release being discussed.

## Translations

- English

## Relations

- Member of: [`catalog/models/ibm/granite-timeseries`](../../../../)

## Official resources

- <https://huggingface.co/ibm-granite/granite-timeseries-flowstate-r1>