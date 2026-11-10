# Documentation Requirements

## Requirements

- Identify Granite Time Series as IBM's open Granite time-series foundation-model family covering forecasting, anomaly detection, classification, imputation, similarity search, and adjacent time-series tasks.
- Preserve identity granularity from first-party release surfaces: PatchTST-FM R2 and FlowState R1 are concrete models; FlowState R1 owns represented chronological version 1.0 and version 1.1 releases; TSPulse R1 and TTM R3 remain aggregate series-level release surfaces with multiple trained-model variants.
- Do not create extra catalog nodes merely for repository branches or revision selectors. Materialize chronological version nodes when first-party evidence establishes a durable release boundary that retains the same concrete-model identity.
- Keep task support, context and horizon limits, benchmark results, revision selectors, licenses, hosted availability, and runtime integrations freshness-sensitive.

## Validation

- Producer provenance resolves to IBM.
- FlowState R1 retains its existing parent-model canonical ID and family membership while its version 1.0 and version 1.1 releases are represented below it.
- TSPulse R1 and TTM R3 retain series-level identity; PatchTST-FM R2 and FlowState R1 retain concrete-model identity.
- Hosted integrations and runtime selectors are not conflated with model-release lifecycle.
