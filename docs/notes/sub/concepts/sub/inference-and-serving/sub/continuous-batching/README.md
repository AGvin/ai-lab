# Continuous Batching

<!--
ai_content:
  managed: true
  l10n: true
-->

Continuous batching dynamically combines active inference requests so new work can enter the batch as other requests finish.

## Core idea

Static batching waits for a fixed group and processes it together, which wastes capacity when sequences have different lengths. Continuous batching schedules tokens or sequence blocks across requests, keeping the accelerator busy while allowing requests to start and finish independently.

## Practical use

- Multi-user language-model APIs.
- High-throughput serving with variable output lengths.
- Better accelerator utilization under sustained load.
- Combining streaming responses with batched computation.

## Trade-offs and limitations

Scheduling adds complexity and can affect fairness. Large active batches improve throughput but may increase time to first token. Memory pressure from many KV caches can become the limiting factor.

## Good practice

Set admission limits by tokens and memory, not only request count. Measure latency percentiles at realistic concurrency. Protect short interactive requests from starvation by very long generations.

## Common mistakes

- Reporting batch throughput without user latency.
- Accepting unlimited context and output lengths.
- Ignoring memory fragmentation and KV-cache capacity.
- Using one scheduling policy for both batch and interactive workloads.

## Related concepts

- [Inference and Serving](../../)
- [Throughput](../throughput/)
- [Latency](../latency/)
- [Model Serving](../model-serving/)
