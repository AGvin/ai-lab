# Latency and Throughput

<!--
ai_content:
  managed: true
  l10n: true
-->

Latency and throughput describe two related but competing dimensions of system performance: how long one request takes and how much total work the system completes over time.

## Core idea

Interactive applications usually prioritize time to first token and response smoothness. Batch systems prioritize total tokens or requests completed. Increasing batch size and queue depth can improve throughput while making individual users wait longer.

## Practical use

- Define service-level objectives for p50, p95, and p99 latency.
- Measure throughput at the required latency target.
- Test realistic prompt and output lengths.
- Separate queue, retrieval, model, tool, and network time.
- Evaluate sustained load rather than short bursts.

## Trade-offs and limitations

Hardware utilization, concurrency, batching, context length, and output length all affect the relationship. One “tokens per second” number cannot represent multi-user service quality.

## Common mistakes

- Maximizing throughput with no latency limit.
- Comparing systems with different workloads.
- Reporting averages without tail behavior.
- Ignoring failed and timed-out requests.

## Related concepts

- [Evaluation and Operations](../../)
- [Latency](../../../inference-and-serving/sub/latency/)
- [Throughput](../../../inference-and-serving/sub/throughput/)
- [Continuous Batching](../../../inference-and-serving/sub/continuous-batching/)
