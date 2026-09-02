# Performance Metrics

Legacy residual retained for workload profiling, benchmark execution, sustained-system measurement, and optimization-comparison guidance that is intentionally outside the canonical metric-definition owner.

> **Migration note:** Generic metric semantics, latency/throughput definitions, workload-condition disclosure, aggregation/failure handling, and the distinction between metric definitions and concrete measured results are already preserved in `docs/sub/concepts/sub/evaluation-and-measurement/sub/metrics/`. Reusable system-performance mechanisms and trade-offs are owned by `docs/sub/concepts/sub/ai-engineering/sub/performance-and-scalability/`. The remaining material below stays here until its exact benchmark, learning, hardware-evidence, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Workload-profile residual

Define the intended workload before measuring: model and version, runtime, numerical representation or quantization, hardware/topology, context or input shape, output length, batch/concurrency, cache/warm state, and request mix can materially change results.

A single tokens-per-second number is not sufficient to describe interactive behavior, serving capacity, memory pressure, reliability, or quality. Relevant observations can include time-to-first output, inter-output latency, throughput, end-to-end percentiles, RAM/VRAM/storage use, concurrent capacity, power/thermal behavior, and error/timeout/retry outcomes.

## Benchmark-execution residual

Use warm-up where appropriate, then collect enough samples to expose variability and compare both isolated and representative concurrent operation. Record model/runtime versions and test conditions so measurements can be reproduced or interpreted later.

For sustained deployments, short burst tests can hide thermal throttling, allocator growth, queue buildup, or other long-run effects. Include sustained/load/soak behavior when those effects matter to the target environment.

## Optimization-comparison residual

Keep output quality and correctness evaluation explicit when comparing performance changes. Larger batches can improve throughput while worsening request latency; lower precision can reduce memory or increase speed while changing output behavior; aggressive caching or reduced context can improve performance while changing freshness or task quality.

These benchmark and comparison practices remain migration source material until their exact evaluation/benchmark, learning, hardware-evidence, or decision-support owners are verified.
