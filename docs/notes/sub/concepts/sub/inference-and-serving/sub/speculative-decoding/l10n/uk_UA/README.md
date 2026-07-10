<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:4bb470d28bb69fa5fe1e4fdb672da3f129a44408
  mode: copy-through
-->

# Speculative Decoding

Using a faster draft model or process to propose tokens for verification by a target model.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

Using a faster draft model or process to propose tokens for verification by a target model. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A smaller or faster draft model proposes several tokens.
- The target model verifies those proposals in fewer expensive steps and accepts a valid prefix.
- Speedup depends on draft accuracy, verification efficiency, and hardware utilization.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Speculative Decoding affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Reduce generation latency without changing the target model’s intended distribution.
- Use spare compute or a compact draft model to accelerate serving.

## Example

A small related model drafts four tokens and the larger target model validates them together.

## Trade-offs and limitations

- A poor draft model provides little speedup and adds overhead.
- Compatibility and implementation support vary by runtime and model family.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Speculative Decoding expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Inference and Serving](../../../../l10n/uk_UA/)
- [Continuous Batching](../../../continuous-batching/l10n/uk_UA/)
- [Inference](../../../inference/l10n/uk_UA/)
