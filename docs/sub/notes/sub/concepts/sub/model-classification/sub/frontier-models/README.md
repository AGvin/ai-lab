# Frontier Models

A frontier model is a model that current evidence places near the leading boundary of capability at a stated time and for a stated scope.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

`Frontier` is a relative and time-sensitive status, not a permanent model class. The boundary moves as new models, training methods, tools, and evaluations appear. A model can therefore remain an LLM or multimodal foundation model after it is no longer considered frontier.

The repository uses **frontier model** as the preferred term. Do not introduce `FLM` as an abbreviation because it is ambiguous and not consistently standardized.

## Evidence boundary

A frontier label should identify:

- the exact model version, snapshot, or service release;
- the capability scope, such as general reasoning, coding, multimodal understanding, or another bounded domain;
- the evidence used, such as independent evaluations, validated task results, or well-defined benchmark suites;
- the verification date;
- important access, tool, context, and deployment assumptions;
- evidence limitations and areas where the model is not leading.

Provider claims can be useful evidence, but they should not be treated as sufficient independent proof when the distinction materially affects selection.

## Relationship to other classifications

Frontier status is independent from:

- **Scale:** frontier models are often LLMs or large multimodal models, but scale alone does not establish frontier status.
- **Architecture:** a frontier model can be dense, sparse, or MoE.
- **Deployment:** a model can be provider-hosted, self-hosted, or locally deployable and still require separate frontier evidence.
- **Access:** proprietary and open-weight models can both approach a capability frontier.
- **Ecosystem maturity:** a newly released frontier model may be experimental or emerging, while a mainstream model may no longer be frontier.
- **Safety or suitability:** frontier capability does not prove reliability, safety, cost efficiency, agent suitability, or fit for a specific workflow.

## Scope-sensitive status

A model may be near the frontier for one task and ordinary for another. Use task-scoped language when the evidence is narrow:

```text
Frontier status: coding — supported
Frontier status: general reasoning — unclear
Verified: 2026-07-26
```

Avoid a universal frontier label when the evidence only covers one benchmark or workload.

## Use in comparisons

Model-selection tables should use frontier status only when it changes the decision. Recommended values are:

- `Supported` — current, sufficiently broad evidence supports frontier status for the stated scope;
- `Not supported` — available evidence does not support the label;
- `Unclear` — evidence is incomplete, conflicting, stale, or too narrow;
- `Not assessed` — the comparison does not evaluate frontier position.

Keep the supporting date and evidence outside the compact label or link to a focused evidence note.

## Common mistakes

- Treating frontier as a synonym for newest, largest, most expensive, or most popular.
- Keeping the label indefinitely after the evidence becomes stale.
- Applying a coding result to every other capability domain.
- Assuming frontier status guarantees low hallucination rates or reliable tool use.
- Using provider marketing language without a defined evidence boundary.
- Treating every LLM as a frontier model.

## Related concepts

- [Model Classification](../../)
- [Small and Large Language Models](../language-model-scale/)
- [Model Architectures](../../../model-architectures/)
- [Model Capabilities and Limitations](../../../model-usage-and-generation/sub/model-capabilities-and-limitations/)
- [Benchmarks](../../../../../benchmarks/)
