# Performance Metrics

Performance metrics describe how an inference system uses time, memory, compute, and capacity under a defined workload.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Important metrics

- Time to first token and inter-token latency.
- Prompt-processing and generation throughput.
- End-to-end latency percentiles.
- RAM, VRAM, and storage usage.
- Concurrent request capacity.
- Power consumption and sustained thermals.
- Error, timeout, and retry rates.

## Core idea

A benchmark is meaningful only when the model, quantization, runtime, context length, batch size, output length, and hardware are recorded. A single tokens-per-second number cannot describe interactive quality or serving capacity.

## Practical use

Create a workload profile before testing. Run warm-up iterations, then collect enough samples to show variability. Measure both isolated and concurrent operation. Keep quality evaluation separate so an optimization that harms output is not reported as a pure improvement.

## Trade-offs and limitations

Optimizing one metric often harms another. Larger batches increase throughput but may worsen latency. Lower precision reduces memory but may alter quality. Power-limited devices can perform well in short tests and throttle during sustained use.

## Common mistakes

- Comparing results with different prompt or output lengths.
- Omitting model and runtime versions.
- Reporting averages without percentiles.
- Ignoring failed requests and quality regressions.

## Related concepts

- [Inference and Serving](../../)
- [Latency](../latency/)
- [Throughput](../throughput/)
- [Benchmarks](../../../evaluation-and-operations/sub/benchmarks/)
