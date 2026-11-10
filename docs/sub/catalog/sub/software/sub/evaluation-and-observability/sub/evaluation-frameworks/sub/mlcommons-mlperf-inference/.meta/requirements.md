# Documentation Requirements

## Requirements

- Identify **MLPerf Inference Reference Software** as the installable/executable source in `mlcommons/inference`: benchmark harness/LoadGen, scripts, reference implementations, examples and compliance validation. Distinguish it from the **existing** `catalog/datasets/mlperf-inference` benchmark-suite identity, vendor-submitted results, datasets and tested hardware.
- Pin repository commit `3fbc329939999c13d0a7b5e67fb2092287e06047` (September 2, 2026) and first-party README, `Submission_Guidelines.md`, and Apache-2.0 `LICENSE.md`; do not imply this is the latest tagged round, test result, or that all assets are Apache-2.0.
- As of the pinned source, the README describes MLPerf Inference **v6.1** and distinguishes seed-release requirements from submission policy. Model workloads, LoadGen, supported backends, accuracy targets, open/closed divisions, compliance and power requirements are version- and scenario-specific; official submissions must follow current separate MLCommons policies.
- Reference implementation is **not** a certified optimized deployment or a generic ranking of CPUs/GPUs. A valid result requires a documented system under test, benchmark revision, model, calibration, dataset, accuracy tier, scenario, load generation configuration and official compliance rules.
- Benchmarks may retrieve large externally licensed models and datasets, exercise hardware at sustained high load, use local privileged tools or require power analyzers under separate access/EULA. Obtain rights, protect test hosts and allocate memory/storage/energy budget before running.
- Preserve one reciprocal MLCommons producer relation and a reader cross-link to the existing MLPerf Inference benchmark. The benchmark node itself receives **zero new acceptance or materialization credit** in this package.
- No external dataset download, system benchmark run, official result validation, power/calibration audit, complete third-party licensing audit, full CI or whole-catalog clean pass is claimed.

## Validation

- [Pinned repository README](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/README.md), [submission guide](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/Submission_Guidelines.md), and [repository license](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/LICENSE.md) support software/package boundaries.
- MLCommons is reciprocal producer; category index includes exactly one software node and existing dataset remains a separate entity.
