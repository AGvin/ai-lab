# Latency

<!--
ai_content:
  managed: true
  l10n: true
-->

Latency is the elapsed time required for an inference system to reach a defined response milestone.

## Useful latency measures

- **Queue latency:** time spent waiting before processing starts.
- **Model-loading latency:** time needed to make the model ready.
- **Time to first token:** delay before the first generated token is returned.
- **Inter-token latency:** delay between generated tokens.
- **End-to-end latency:** total time until the complete response is available.

## Core idea

A single average hides important user experience differences. Interactive chat prioritizes time to first token and smooth token delivery, while batch processing may prioritize total completion time.

## Practical use

Measure percentiles such as p50, p95, and p99 under realistic concurrency. Separate prompt-processing time from decode time. Include network, queue, retrieval, and tool latency when evaluating an application.

## Trade-offs and limitations

Batching can improve throughput while increasing individual request latency. Larger models and longer prompts usually increase latency. Caching reduces repeated work but adds memory and invalidation complexity.

## Common mistakes

- Reporting only the fastest isolated request.
- Using average latency without tail percentiles.
- Excluding queue and retrieval time from user-facing measurements.
- Comparing latency with different output lengths.

## Related concepts

- [Inference and Serving](../../)
- [Throughput](../throughput/)
- [Performance Metrics](../performance-metrics/)
- [Continuous Batching](../continuous-batching/)
