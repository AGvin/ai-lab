# Latency

Legacy residual retained for practical measurement, workload comparison, and performance-engineering guidance that is intentionally outside the canonical metric-definition owner.

> **Migration note:** Generic latency semantics, milestone boundaries, queue/model/TTFT/inter-token/end-to-end distinctions, percentile/distribution requirements, workload-condition disclosure, and the separation of latency from throughput/concurrency are already preserved in `docs/sub/concepts/sub/evaluation-and-measurement/sub/metrics/`. The remaining material below stays here until its exact learning, performance-engineering, benchmark, or evidence owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Practical measurement residual

Measure latency under representative concurrency and workload conditions rather than reporting only an isolated best-case request. For interactive generation, time to first output and inter-output cadence can matter independently from total completion time; batch workloads can prioritize completion deadlines differently.

Application-level measurements should include the relevant end-to-end stages such as queue wait, network transfer, retrieval, tool calls, prompt/prefill processing, decode, validation, and post-processing when those stages affect the user-visible milestone.

Comparisons should control or disclose input/context size, output length, batch/concurrency, warm or cold state, cache state, model/runtime/hardware configuration, and failure handling. Average latency alone can hide important tail behavior, so p50/p95/p99 or another suitable distributional summary may be needed.

## Performance-engineering residual

Batching can improve aggregate throughput while increasing individual-request latency. Larger workloads, longer prompts, queueing, cache misses, model loading, or dependency calls can shift the critical path. Caching or precomputation can reduce repeated work but introduce memory, invalidation, and correctness trade-offs.

These operational consequences remain migration source material until their exact performance/scalability, learning, benchmark, evidence, or decision-support owners are verified.
