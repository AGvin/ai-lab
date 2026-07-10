# Dense and Sparse Models

Dense models activate most parameters for each input, while sparse models activate selected subsets.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Dense models activate most parameters for each input, while sparse models activate selected subsets. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A dense model uses most or all of its parameters for each token, while a sparse model activates only selected parameter blocks.
- Mixture-of-Experts models use a router to select experts, increasing total parameter capacity without using every expert for every token.
- Memory needed to store all weights can remain high even when active compute per token is lower.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Dense and Sparse Models affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Interpret active-parameter versus total-parameter claims.
- Estimate whether a sparse model improves serving throughput or fits available memory.

## Example

A model may contain 100B total parameters but route each token through experts representing only a fraction of that compute.

## Trade-offs and limitations

- Sparse routing adds communication, load-balancing, and implementation complexity.
- A larger total parameter count does not directly translate into proportionally higher quality.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Dense and Sparse Models expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Foundations and Architecture](../../)
- [Encoder and Decoder Architectures](../encoder-decoder/)
- [Foundation Models](../foundation-models/)
