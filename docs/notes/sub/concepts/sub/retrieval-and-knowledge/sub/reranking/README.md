# Reranking

<!--
ai_content:
  managed: true
  l10n: true
-->

A second-stage relevance model that reorders retrieved candidates.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

A second-stage relevance model that reorders retrieved candidates. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A reranker receives the query and a smaller set of retrieved candidates.
- It computes a more precise relevance score, often using a cross-encoder that jointly reads query and document.
- Only the highest-ranked passages are sent to the generator, reducing context noise.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Reranking affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Improve precision after fast vector, lexical, or hybrid candidate retrieval.
- Reduce irrelevant evidence before answer generation.

## Example

A retriever returns 50 documentation chunks and a reranker selects the best 6 for the final prompt.

## Trade-offs and limitations

- Reranking adds latency and model cost.
- It cannot recover a relevant passage that the first-stage retriever never returned.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Reranking expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Retrieval and Knowledge](../../)
- [Keyword Search](../keyword-search/)
- [Citations](../citations/)
