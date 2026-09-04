# Documentation Requirements

## Requirements

- Teach Cost Modeling as identifying the cost components and unit-economics model needed to compare complete AI system routes.
- Include fixed, variable, idle, hardware, energy, provider/service, storage/network, engineering, maintenance, validation/review, retry, and consequential-error costs when they materially affect the decision.
- Use cost per accepted result or another workload-relevant accepted-output unit instead of isolated request/token price when quality and retry rates differ.
- Separate current provider prices and billing rules from the reusable modeling method; recheck mutable prices, quotas, billable units, and terms at decision time.
- Preserve the distinction between sunk acquisition cost, ongoing fixed/idle cost, and marginal workload cost when comparing local/self-hosted and hosted routes.
- State assumptions, workload volume, utilization, quality/acceptance boundary, and evidence date when a cost model is used for a concrete decision.

## Validation

- One provider token/request price is not presented as total system cost.
- Local/self-hosted infrastructure is not treated as free merely because hardware is already owned.
- Concrete price claims remain date/source bounded.
