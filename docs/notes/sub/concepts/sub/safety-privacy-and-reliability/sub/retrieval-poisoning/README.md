# Retrieval Poisoning

Manipulating indexed knowledge so retrieval supplies misleading or malicious context.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Manipulating indexed knowledge so retrieval supplies misleading or malicious context. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Retrieval poisoning inserts or modifies indexed content so it is selected for important queries.
- The poisoned passage may contain false facts, manipulated ranking terms, or prompt-injection instructions.
- Defenses combine source authorization, provenance, ranking evaluation, content scanning, and answer grounding.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Retrieval Poisoning affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Secure knowledge bases that ingest external or user-contributed documents.
- Test whether RAG answers remain trustworthy after corpus changes.

## Example

A malicious document repeats popular query terms and tells an agent to send confidential data to an external endpoint.

## Trade-offs and limitations

- Legitimate documents can also become stale or contradictory without malicious intent.
- Ranking attacks may exploit both lexical and vector signals.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Retrieval Poisoning expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Data Privacy](../data-privacy/)
- [Guardrails](../guardrails/)
