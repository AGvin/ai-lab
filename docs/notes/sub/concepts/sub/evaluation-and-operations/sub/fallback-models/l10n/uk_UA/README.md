<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:8abd5df6f218a83efdbec48d128a98d3e2625fb1
  mode: copy-through
-->

# Fallback Models

Alternative models used when the preferred model fails, is unavailable, or exceeds policy limits.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

Alternative models used when the preferred model fails, is unavailable, or exceeds policy limits. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A fallback model is invoked when the preferred model is unavailable, too slow, too expensive, or fails validation.
- Fallback policies define ordering, retry conditions, and whether capability degradation is acceptable.
- The application normalizes differences in schemas, context, and safety behavior.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Fallback Models affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Increase service resilience and manage provider outages.
- Provide cheaper or local alternatives under budget or privacy rules.

## Example

A local model provides a basic response when a hosted API is unavailable, with the UI indicating reduced capability.

## Trade-offs and limitations

- Fallback output may have different quality or formatting.
- Silent degradation can hide operational problems from users.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Fallback Models expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Evaluation and Operations](../../../../l10n/uk_UA/)
- [Human Evaluation](../../../human-evaluation/l10n/uk_UA/)
- [Caching](../../../caching/l10n/uk_UA/)
