# Throughput

The amount of model work completed per unit of time.

## Core idea

The amount of model work completed per unit of time. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Throughput measures work completed per unit of time, such as tokens per second or requests per second.
- Batching and concurrency often improve aggregate throughput by using hardware more fully.
- Throughput must be reported with model, precision, context, output length, and hardware conditions.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Throughput affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Size servers for multiple users or batch processing.
- Compare runtimes under sustained workload.

## Example

A server can generate more total tokens per second with continuous batching even though each user waits slightly longer.

## Trade-offs and limitations

- Higher aggregate throughput can increase individual request latency.
- Token throughput is not directly comparable across tokenizers or task shapes.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Throughput expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Inference and Serving](../../)
- [Latency](../latency/)
- [Performance Metrics](../performance-metrics/)
