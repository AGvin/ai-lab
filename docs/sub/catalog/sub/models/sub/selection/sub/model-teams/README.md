# Model Teams

Choose a model portfolio only when role separation, routing, specialization, or independent evaluation produces a measurable benefit over one model.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Team-design boundary

Model-team selection covers role-based portfolios, model routing, and ensembles or consensus. Start with the smallest portfolio that can meet the complete workflow acceptance criteria.

The same model may cover several compatible roles when doing so does not create unacceptable conflicts, correlated failure, quality loss, latency, or cost. Add a specialist or independent model only when the operational gain justifies the additional service, context, routing, and verification complexity.

## Current materialized guidance

- [`role-based-portfolios/`](./sub/role-based-portfolios/) — choose models by planner, worker, reviewer, verifier, evaluator, advisor, memory/context, and related role contracts.

Routing and ensemble branches are materialized only when reviewed task content requires them; the selected navigation is not created as an empty skeleton.

## Portfolio evidence

Evaluate terminal workflow acceptance, correlated errors, role independence, handoff quality, retries, routing mistakes, latency, resource residency, human review, and total cost per accepted result. Compare the proposed team against a single-generalist baseline rather than assuming more models improve quality.

Link canonical facts for every participating model from [Model Reference](../../../reference/).
