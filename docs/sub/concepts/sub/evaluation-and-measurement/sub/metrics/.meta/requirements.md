# Documentation Requirements

## Requirements

- Use the reader-facing title `Evaluation Metrics`.
- Define a metric as a specified rule/procedure for turning observations about a defined unit, population, workload, or evaluation sample into a quantitative, ordinal, categorical, or otherwise structured measure that can be interpreted against an explicit property/question.
- Require every metric definition to state what is measured, unit/scale, direction of better/worse where meaningful, denominator/population, aggregation, exclusions/failures, operating conditions, and uncertainty/variability needed for interpretation. A bare number/name is not a complete metric specification.
- Distinguish a metric definition from a metric value/result. `Latency`, `accuracy`, or `toxicity rate` names a measurement construct; `42 ms` or `91%` is evidence from a concrete run under stated conditions.
- Distinguish metrics from benchmarks, evaluation datasets, judges, and acceptance thresholds. A benchmark bundles tasks/data/procedure; a judge supplies observations/scores; a threshold converts measurements into a decision rule.
- Explain that metrics can cover task quality/correctness, calibration, robustness, safety, fairness, retrieval, human preference, latency, throughput, memory/capacity, reliability, power/energy, cost, or other properties. Metrics from different properties are not interchangeable and generally should not be collapsed without an explicit justified aggregation.
- Define latency generically as elapsed time between two explicitly named events/milestones. Queue wait, request arrival-to-start, model/prefill time, time to first output/token, inter-output/token delay, tool/retrieval/network stages, and end-to-end completion are different latency boundaries and must not be mixed under one unlabeled number.
- Explain that latency distributions often require percentiles/tails or another distributional summary rather than only a mean. Percentile definition, sample population, warm/cold state, concurrency/load, prompt/input size, output length, streaming policy, and failure handling can materially affect the result.
- Define throughput generically as accepted/completed work per unit time under a stated workload and service condition. Requests/s, samples/s, input/prompt tokens/s, generated/output tokens/s, audio seconds/s, images/s, or another work unit are different metrics and must not be compared as though equivalent.
- Distinguish per-request generation speed from aggregate system throughput and from concurrency/capacity. More simultaneous requests or larger batches can increase total completed work while changing individual request latency.
- When a throughput claim is constrained by service quality, state the constraint explicitly: latency SLO/percentile, error/timeout rate, output/quality target, queue policy, and workload mix. Maximum unconstrained throughput is not the same as usable service capacity.
- Explain that token-based metrics depend on tokenizer/model representation and on whether input versus output tokens are counted; cross-model token/s comparisons can be misleading when tokenization or output semantics differ.
- Explain that performance metrics require matched workload and quality conditions for meaningful comparison. Model/version, numerical precision/quantization, runtime, hardware/topology, context/input shape, batch/concurrency, output length, cache/warm state, and preprocessing/post-processing boundaries can materially change measurements.
- Report failed, rejected, retried, timed-out, or truncated work according to an explicit rule instead of silently excluding it when those outcomes affect the intended measurement.
- Distinguish metric semantics from performance engineering. Batching, scheduling, caching, offloading, parallelism, kernel tuning, and capacity planning can change latency/throughput but their mechanism/design guidance belongs with `ai-engineering/performance-and-scalability` or other applicable owners.
- Keep concrete benchmark scores, service SLO values, current model/provider latency/throughput, hardware measurements, cost numbers, leaderboard results, and optimization recommendations with their applicable evidence, catalog, benchmark, engineering, or decision owners.
- Use the canonical entity references as research inputs for documented measurement conditions and workload/scenario-specific latency/throughput interpretation when reader-facing rendering is activated.

## Validation

- A metric is not presented as meaningful without its unit/population/conditions/aggregation semantics.
- Metric definitions are distinguished from measured values, benchmarks, judges, and acceptance decisions.
- Latency names a defined event interval rather than one universal timing number; throughput names a defined work unit per time rather than generic `tokens/s`.
- Average-only performance reporting does not replace tail/distribution information where variability matters.
- Throughput, concurrency, per-request speed, and service capacity are not treated as synonyms.
- Performance engineering mechanisms and mutable measurements remain outside the canonical metric-definition owner.
