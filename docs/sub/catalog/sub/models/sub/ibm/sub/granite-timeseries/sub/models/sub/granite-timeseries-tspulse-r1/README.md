# Granite TimeSeries TSPulse R1

Granite TimeSeries TSPulse R1 is represented as a model series, not a single checkpoint. IBM's official model card releases three separately pretrained variants under the same repository:

- `tspulse-hybrid-allhead-512-p8-r1` — anomaly detection;
- `tspulse-hybrid-dualhead-512-p8-r1` — imputation and semantic search;
- `tspulse-block-dualhead-512-p16-r1` — classification.

The variants are selected with repository branches/revisions. Those selectors are not aliases, and this checkpoint does not create extra child identities merely to mirror branch names.

## Translations

- English

## Relations

- Member of: [`catalog/models/ibm/granite-timeseries`](../../../../)

## Official resources

- <https://huggingface.co/ibm-granite/granite-timeseries-tspulse-r1>
