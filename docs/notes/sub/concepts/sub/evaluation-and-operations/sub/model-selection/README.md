# Model Selection

<!--
ai_content:
  managed: true
  l10n: true
-->

Model selection chooses a model and deployment configuration that best satisfy a task's quality, cost, latency, privacy, safety, and operational requirements.

## Core idea

There is rarely one universally best model. A larger hosted model may provide stronger reasoning, while a smaller local model may offer lower cost, privacy, or offline operation. Selection should be based on measured workflow performance rather than reputation or parameter count.

## Decision dimensions

- Task quality and failure severity.
- Context and modality requirements.
- Tool-calling and structured-output reliability.
- Latency, throughput, and concurrency.
- API cost or hardware requirement.
- License, privacy, and data residency.
- Provider stability and deployment control.

## Practical use

Define minimum acceptance thresholds, shortlist models using public evidence, then run the same internal evals. Test exact versions and quantizations. Record why the chosen model won and what conditions would trigger reconsideration.

## Common mistakes

- Selecting from a single benchmark.
- Comparing hosted and local models without total operating cost.
- Ignoring version changes and provider deprecations.
- Choosing the strongest model when a smaller one already meets requirements.

## Related concepts

- [Evaluation and Operations](../../)
- [Model Routing](../model-routing/)
- [Benchmarks](../benchmarks/)
- [Quality and Cost Trade-Offs](../quality-cost-tradeoffs/)
