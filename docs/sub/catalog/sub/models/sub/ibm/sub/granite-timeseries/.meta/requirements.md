# Documentation Requirements

## Requirements

- Identify Granite Time Series as IBM's open Granite time-series foundation-model family covering forecasting, anomaly detection, classification, imputation, similarity search, and adjacent time-series tasks.
- Preserve identity granularity from first-party release surfaces: PatchTST-FM R2 is a concrete released model, while FlowState R1, TSPulse R1, and TTM R3 are aggregate series-level release surfaces that expose multiple revision or trained-model variants.
- Do not create extra catalog nodes merely for repository branches or revision selectors. Materialize a child model only when its trained identity and durable boundary are independently established.
- Keep task support, context and horizon limits, benchmark results, revision selectors, licenses, hosted availability, and runtime integrations freshness-sensitive.

## Validation

- Producer provenance resolves to IBM.
- The three aggregate series retain their existing canonical IDs and parent membership, so this taxonomy correction does not change the Model denominator.
- Hosted integrations and runtime selectors are not conflated with model-release lifecycle.
