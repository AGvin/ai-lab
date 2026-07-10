# Throughput

<!--
ai_content:
  managed: true
  l10n: true
-->

Throughput measures how much inference work a system completes per unit of time.

## Common measures

- Generated tokens per second.
- Prompt tokens processed per second.
- Requests completed per second.
- Concurrent sessions sustained at a latency target.

## Core idea

Throughput is a system property, not only a model property. Batching, request length, hardware utilization, quantization, scheduler behavior, and concurrency all influence it. Per-request token speed may decrease while total system throughput increases.

## Practical use

Measure throughput with the expected mix of prompt lengths, output lengths, and concurrent users. Report latency alongside throughput so a high number is not achieved by making individual users wait excessively.

## Trade-offs and limitations

Larger batches improve hardware utilization but consume more memory and can raise time to first token. Continuous batching improves serving efficiency but creates more complex scheduling behavior.

## Common mistakes

- Comparing tokens per second from single-user and batched tests.
- Mixing prompt and generation throughput.
- Ignoring failed or timed-out requests.
- Optimizing maximum throughput when the real requirement is interactive latency.

## Related concepts

- [Inference and Serving](../../)
- [Latency](../latency/)
- [Continuous Batching](../continuous-batching/)
- [Performance Metrics](../performance-metrics/)
