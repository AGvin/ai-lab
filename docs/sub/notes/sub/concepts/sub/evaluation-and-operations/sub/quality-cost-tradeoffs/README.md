# Quality and Cost Trade-Offs

Legacy residual retained for practical quality-versus-cost decision strategies that are intentionally outside the reusable AI System Cost and Capacity concept owner and outside concrete model-selection recommendations.

> **Migration note:** Cost per accepted result, acceptance-quality boundaries, full-system cost classes, caching and capacity trade-offs, and the rule that cost optimization must not silently weaken required quality, reliability, privacy, safety, or policy constraints are already preserved in `docs/sub/concepts/sub/ai-engineering/sub/cost-and-capacity/`. Concrete model-choice consequences and task-fit recommendations remain under `docs/sub/catalog/sub/models/sub/selection/`. The remaining material below stays here until its exact learning, workflow, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Decision-strategy residual

Define the minimum accepted quality and failure boundary before optimizing cost. Then compare eligible solutions by the total cost of accepted work, including retries, validation, human review, engineering/runtime overhead, and consequential errors where they materially change the decision.

Practical strategies can include:

- routing routine work to a cheaper eligible model or path;
- escalating difficult, failed, or high-risk cases to stronger capability;
- using deterministic tools for exact operations instead of paying for probabilistic generation;
- reducing irrelevant context while preserving evidence required for correctness;
- caching stable reusable results where correctness, privacy, and invalidation rules permit it;
- retaining independent validation when removing it would materially increase failure cost or severity.

A stronger or more expensive model is not automatically the most economical choice, and a lower token/request price is not automatically cheaper when success rate, retries, human correction, operational complexity, or error impact differ. Likewise, benchmark deltas are not business value unless they map to the actual acceptance criteria and workload.

These quality/cost optimization strategies remain migration source material until their exact learning, workflow, evaluation, or decision-support owners are verified.
