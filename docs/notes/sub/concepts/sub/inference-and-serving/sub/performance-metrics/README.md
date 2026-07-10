# Performance Metrics

Measurements such as time to first token, tokens per second, latency, and memory use.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Measurements such as time to first token, tokens per second, latency, and memory use. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Performance metrics separate loading time, prompt-processing speed, time to first token, generation speed, memory use, throughput, and tail latency.
- Measurements should include warm-up and repeat runs.
- Quality metrics must accompany speed metrics when optimizations change precision or decoding.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Performance Metrics affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Benchmark local hardware and model variants.
- Identify which stage limits the real workload.

## Example

A local benchmark records VRAM, prompt tokens per second, generation tokens per second, and output quality for each quantization.

## Trade-offs and limitations

- Metrics collected with different prompts or settings are not comparable.
- Peak numbers can hide thermal throttling, queueing, or unstable long-run behavior.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Performance Metrics expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Inference and Serving](../../)
- [Throughput](../throughput/)
- [Model Serving](../model-serving/)
