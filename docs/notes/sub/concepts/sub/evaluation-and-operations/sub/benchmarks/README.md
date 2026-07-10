# Benchmarks

<!--
ai_content:
  managed: true
  l10n: true
-->

A benchmark is a standardized task, dataset, protocol, or workload used to compare models or systems under defined conditions.

## Core idea

Benchmarks support broad comparison, but their results are meaningful only when the tested model version, prompt, scoring method, hardware, and execution settings are understood. A benchmark score is evidence for the measured task, not a universal measure of intelligence.

## Common benchmark types

- Knowledge and reasoning question sets.
- Coding and software-engineering tasks.
- Multilingual and multimodal evaluations.
- Safety and adversarial tests.
- Inference latency, throughput, and memory workloads.
- Human preference leaderboards.

## Practical use

Use public benchmarks to narrow candidates, then run task-specific evals on the real workflow. Check whether results are independently reproducible and whether training contamination or prompt optimization may affect the ranking.

## Trade-offs and limitations

Popular benchmarks can become saturated, leaked into training data, or optimized indirectly. Different harnesses may produce materially different scores. Leaderboards also tend to simplify multi-dimensional trade-offs into one ranking.

## Common mistakes

- Selecting a model from one aggregate rank.
- Comparing scores produced by different harnesses as equivalent.
- Ignoring cost and latency.
- Treating benchmark names as stable methodology without checking versions.

## Related concepts

- [Evaluation and Operations](../../)
- [Evals](../evals/)
- [Model Selection](../model-selection/)
- [Performance Metrics](../../../inference-and-serving/sub/performance-metrics/)
