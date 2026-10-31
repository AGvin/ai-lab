# NVIDIA AIPerf

NVIDIA AIPerf is a CLI and Python API for performance testing AI inference endpoints using controlled workloads and measurable response metrics.

## Evaluation role and boundaries

It measures throughput, request latency, time-to-first-token, concurrency and selected multimodal serving behaviors with optional telemetry and visualization. AIPerf is neither an inference engine nor a benchmark dataset; models, servers and hardware under test remain independent.

## Reproducibility and operational safeguards

Record request mixture, input/output sizes, model/precision, serving software version, warm-up, concurrency, load duration and accelerator setup. Endpoint plugins, metric definitions and output formats vary by release. Avoid publishing vendor-specific performance figures without the tested configuration.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Documentation](https://docs.nvidia.com/aiperf/welcome-to-ai-perf-documentation)
- [Source](https://github.com/ai-dynamo/aiperf)
