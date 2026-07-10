# Citations

Links or references that connect generated statements to supporting sources.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Links or references that connect generated statements to supporting sources. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A citation associates an answer span or claim with a source identifier and location.
- Reliable systems preserve source IDs through retrieval and generate citations from selected evidence rather than asking the model to invent links.
- Citation validation checks that the source exists and actually supports the adjacent claim.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Citations affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Make research, documentation, policy, and support answers auditable.
- Let readers inspect context and resolve uncertainty.

## Example

A model answer links a hardware recommendation to the exact benchmark note and quantization section used as evidence.

## Trade-offs and limitations

- A citation can be present but irrelevant or insufficient.
- Generated page numbers, URLs, or quotes must be validated against the source.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Citations expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Retrieval and Knowledge](../../)
- [Reranking](../reranking/)
- [Metadata Filtering](../metadata-filtering/)
