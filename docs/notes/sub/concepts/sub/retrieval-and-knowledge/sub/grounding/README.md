# Grounding

<!--
ai_content:
  managed: true
  l10n: true
-->

Constraining generated claims to supplied evidence, tools, or authoritative sources.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Constraining generated claims to supplied evidence, tools, or authoritative sources. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Grounding supplies evidence or tool results that the model is expected to use for claims.
- The prompt and application distinguish evidence from instructions and require the answer to stay within supported facts.
- Grounding quality can be checked through citation accuracy, faithfulness, and abstention when evidence is insufficient.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Grounding affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Reduce unsupported claims in technical, legal, financial, or operational answers.
- Make answers auditable by linking them to documents, databases, or tool outputs.

## Example

A deployment recommendation cites measured benchmark rows and hardware notes instead of relying on the model’s memory.

## Trade-offs and limitations

- Supplying evidence does not guarantee the model interprets it correctly.
- Contradictory, stale, or malicious sources can ground the answer in the wrong information.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Grounding expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Retrieval and Knowledge](../../)
- [Hybrid Search](../hybrid-search/)
- [Vector Search](../vector-search/)
