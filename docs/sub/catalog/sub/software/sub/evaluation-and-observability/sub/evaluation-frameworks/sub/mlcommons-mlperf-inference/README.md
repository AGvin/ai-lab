# MLPerf Inference Reference Software

The **MLPerf Inference Reference Software** is the public implementation repository maintained by [MLCommons](../../../../../../../producers/sub/m/sub/mlcommons/). It contains reference workloads, LoadGen, evaluation and compliance utilities, configuration examples and submission guidance for the [MLPerf Inference benchmark](../../../../../../../datasets/sub/mlperf-inference/).

## Software versus benchmark

The repository `mlcommons/inference` supplies executable tools; the **MLPerf Inference** benchmark is a separately cataloged versioned measurement suite. Neither artifact is a vendor GPU, optimized inference runtime, published result, or permission to redistribute every reference model and dataset.

The pinned [README](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/README.md) covers MLPerf Inference v6.1 and instructs official submitters to use compatible source versions and MLCommons submission rules. Benchmark scenarios, quality targets, accuracy thresholds, LoadGen inputs, hardware configurations, power rules and open/closed division eligibility are version-dependent. Reference implementations illustrate the benchmark rather than guaranteeing peak performance.

## Reproducibility and operating risk

To compare results, fix the benchmark release, system under test, workload, model and precision, data preprocessing, scenario, accuracy tier, load generator options, warm-up and system/power configuration. Confirm datasets and model licenses independently; large test workloads may consume substantial accelerator power, memory, disk and network resources. Official submissions and protected power tools have separate requirements.

Covered repository software is under [Apache-2.0](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/LICENSE.md); this does not automatically cover externally downloaded datasets, model weights, trademarks, protected test assets or third-party dependencies. No inference benchmarking or official compliance test was performed for this profile.

## Relations

- Produced by: [MLCommons](../../../../../../../producers/sub/m/sub/mlcommons/)
- Related benchmark: [MLPerf Inference](../../../../../../../datasets/sub/mlperf-inference/)

## Official resources

- [Reference software source](https://github.com/mlcommons/inference)
- [Pinned README](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/README.md)
- [Submission guide](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/Submission_Guidelines.md)
- [Source license](https://github.com/mlcommons/inference/blob/3fbc329939999c13d0a7b5e67fb2092287e06047/LICENSE.md)
