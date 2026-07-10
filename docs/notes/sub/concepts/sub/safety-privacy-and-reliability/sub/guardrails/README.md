# Guardrails

<!--
ai_content:
  managed: true
  l10n: true
-->

Controls that validate, restrict, or monitor model inputs, outputs, and actions.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Controls that validate, restrict, or monitor model inputs, outputs, and actions. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Guardrails are controls around model input, output, tools, state, and workflow transitions.
- They may include schemas, allowlists, content classifiers, deterministic rules, policy engines, and approval gates.
- Effective guardrails are enforced by application code rather than only described in a prompt.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Guardrails affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Restrict unsafe tool arguments and unsupported output formats.
- Block or escalate sensitive actions and data flows.

## Example

A file-writing tool rejects paths outside an approved workspace even if the model requests them.

## Trade-offs and limitations

- Guardrails can create false positives and false negatives.
- A collection of filters without a clear threat model can provide false confidence.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Guardrails expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Retrieval Poisoning](../retrieval-poisoning/)
- [Data Residency](../data-residency/)
