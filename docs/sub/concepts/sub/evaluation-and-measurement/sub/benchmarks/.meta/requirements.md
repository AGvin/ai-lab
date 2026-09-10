# Documentation Requirements

## Requirements

- Use the reader-facing title `Benchmarks`.
- Define a benchmark as a standardized, versioned evaluation specification or package that enables repeatable comparison by fixing or constraining the task/workload, evaluation data or input distribution, procedure/harness, allowed system behavior/configuration, metrics/scoring, quality/validity conditions, and reporting rules relevant to the benchmark's purpose.
- Distinguish a benchmark from a benchmark run/result. The benchmark defines what and how to measure; a concrete score, submission, result record, leaderboard row, or ranking is evidence produced by applying that definition to a particular model/system/configuration at a particular time.
- Distinguish a benchmark from an evaluation dataset. A dataset can supply cases or workload inputs, while the benchmark additionally defines task semantics, procedure, scoring/metrics, constraints, and comparison rules. A dataset by itself is not necessarily a benchmark.
- Distinguish a benchmark from a metric. A benchmark can report one or many metrics and can impose quality thresholds or other validity constraints; a metric definition alone does not specify the complete test workload or protocol.
- Explain that benchmark suites can contain multiple benchmark tasks/scenarios with separate datasets, metrics, quality targets, modalities, workloads, or operating conditions. An aggregate suite score/rank is a reporting choice rather than the definition of benchmark validity.
- Require benchmark version/protocol identity for comparison. Changes to data, prompts/tasks, reference implementations, allowed optimizations, quality targets, scoring, load generation, harness code, or rules can make results from different versions non-equivalent unless an explicit normalization/bridge exists.
- Explain that comparability depends on following the same relevant protocol and reporting configuration differences. Model/checkpoint, prompt/template, tools/retrieval, numerical precision, runtime, hardware, batch/concurrency, context/input/output shape, allowed external resources, preprocessing/post-processing, and other controlled factors can materially affect results.
- Distinguish closed/controlled comparison rules from open/exploratory benchmark use where applicable. A benchmark can permit innovation while still requiring enough metadata and constraints to know which results are comparable.
- Explain that benchmark validity is scoped to the tasks, distributions, operating conditions, metrics, and populations represented. Strong benchmark performance is evidence for those conditions, not a universal measure of intelligence, safety, factuality, usefulness, or production suitability.
- Explain saturation, contamination, leakage, repeated optimization, prompt/harness tuning, memorization, and benchmark gaming as threats to external validity. Public benchmark familiarity can reduce the amount of evidence a score provides about unseen real-world use.
- Explain that implementation/harness differences can change outcomes even when a benchmark name is the same. Scoring code, prompt formatting, sampling/decoding, retry/failure handling, parsing, tool access, and dependency versions require documented control for meaningful comparison.
- Require invalid/failed/timed-out/skipped cases to follow an explicit benchmark rule rather than being silently removed when they affect the measured workload or score.
- Distinguish reproducibility from representativeness. A benchmark can be highly reproducible yet poorly represent a target use case, and a representative workload can still require stronger controls to produce comparable results.
- Make clear that human/model-judge leaderboards are benchmark result surfaces only when backed by a specified evaluation protocol; preference rankings or crowdsourced votes without stable sampling/judging rules should not be treated as equivalent to a controlled benchmark by name alone.
- Keep concrete benchmark identities/resources, benchmark repositories, current versions, task lists, result submissions, leaderboard positions, model scores, benchmark-run evidence, and task-specific model-selection recommendations with their applicable catalog, evidence, benchmark-resource, or decision owners.
- Use the canonical entity references as research inputs for standardized, reproducible, scenario/metric/quality-constrained benchmark boundaries when reader-facing rendering is activated.

## Validation

- A benchmark is distinguished from its dataset, metric, run/result, submission, leaderboard, and ranking.
- Benchmark version/rules/procedure are explicit enough that cross-result comparability is not assumed from a shared benchmark name alone.
- A benchmark score is not presented as universal model/system quality or suitability evidence outside the measured scope.
- Reproducibility is not treated as equivalent to deployment representativeness.
- Contamination, repeated tuning, harness variation, and failure-handling rules are recognized as threats to interpretation.
- Concrete benchmark resources, versions, results, rankings, and model-selection decisions remain outside the reusable benchmark concept owner.
