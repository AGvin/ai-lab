<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:d80a6d5f3e921daeb39d1bf4d68277bd0fe5f4dc
  mode: copy-through
-->

# Latency



The elapsed time required to produce a response or reach a defined output milestone.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

The elapsed time required to produce a response or reach a defined output milestone. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Latency measures elapsed time for a request or stage, such as queue time, prompt processing, time to first token, or total completion.
- Different stages depend on model size, input length, hardware, batching, and provider load.
- Percentiles such as p50 and p95 reveal variation hidden by averages.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Latency affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Set responsiveness targets for interactive assistants and APIs.
- Find whether delays come from queueing, retrieval, prompt processing, or generation.

## Example

A chat UI may feel responsive with a low time to first token even when the full response takes several seconds.

## Trade-offs and limitations

- One benchmark number rarely represents real traffic.
- Optimizing average latency can worsen tail latency or throughput.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Latency expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Inference and Serving](../../../../l10n/uk_UA/)
- [KV Cache](../../../kv-cache/l10n/uk_UA/)
- [Throughput](../../../throughput/l10n/uk_UA/)
