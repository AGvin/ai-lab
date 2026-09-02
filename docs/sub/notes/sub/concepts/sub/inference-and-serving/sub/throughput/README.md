# Throughput

Legacy residual retained for workload-shaped measurement, capacity planning, and serving-optimization guidance that is intentionally outside the canonical metric-definition owner.

> **Migration note:** Generic throughput semantics, work-unit distinctions, input/output token separation, concurrency/capacity boundaries, service-quality constraints, workload-condition disclosure, and failure-accounting requirements are already preserved in `docs/sub/concepts/sub/evaluation-and-measurement/sub/metrics/`. The remaining material below stays here until its exact learning, performance-engineering, benchmark, or evidence owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Practical measurement residual

Measure throughput with the expected distribution of prompt/input lengths, generated output lengths, batch sizes, concurrency, cache state, model/runtime configuration, and hardware topology. Report the work unit explicitly: generated tokens/s, prompt tokens/s, requests/s, samples/s, or another unit are not interchangeable.

When throughput is used as a service-capacity claim, report the associated latency, error/timeout/rejection behavior, queue policy, and quality target. Maximum unconstrained throughput can be materially different from usable throughput under an interactive or deadline-bound service objective.

## Performance-engineering residual

Throughput is shaped by the complete serving system rather than the model alone. Batching, scheduler behavior, request-length mix, quantization or precision, memory headroom, hardware utilization, and concurrency can increase aggregate work completed even while per-request generation speed or latency becomes worse.

Larger or dynamic batches can improve accelerator utilization but consume more memory and may increase queueing or time to first output. Continuous batching and related scheduling strategies can improve utilization while adding scheduling, fairness, admission, and tail-latency trade-offs.

These operational consequences remain migration source material until their exact performance/scalability, learning, benchmark, evidence, or decision-support owners are verified.
