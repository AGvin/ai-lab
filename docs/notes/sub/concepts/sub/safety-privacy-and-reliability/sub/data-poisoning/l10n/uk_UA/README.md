<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:2eb921a00897b609d840b34c19737f29db38a720
  mode: copy-through
-->

# Data Poisoning



Corrupting training or adaptation data to degrade or manipulate model behavior.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

Corrupting training or adaptation data to degrade or manipulate model behavior. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Data poisoning modifies training or adaptation data to influence learned behavior.
- Attacks can degrade general performance, introduce targeted backdoors, or bias specific outputs.
- Defenses include provenance, anomaly detection, deduplication, review, and robust evaluation.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Data Poisoning affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Threat-model third-party datasets and community-contributed training data.
- Audit unexpected behavior after adaptation.

## Example

Malicious examples teach a model to produce a hidden response whenever a specific trigger phrase appears.

## Trade-offs and limitations

- Small targeted poison samples can be difficult to detect.
- Automated cleaning can remove legitimate rare examples.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Data Poisoning expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Safety, Privacy, and Reliability](../../../../l10n/uk_UA/)
- [Model Alignment](../../../model-alignment/l10n/uk_UA/)
- [Prompt Injection](../../../prompt-injection/l10n/uk_UA/)
