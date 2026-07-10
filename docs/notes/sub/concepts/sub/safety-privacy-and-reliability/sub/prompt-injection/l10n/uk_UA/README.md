<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:4c759622ffd1041a9549d0681be7f69c36226da1
  mode: copy-through
-->

# Prompt Injection



Input designed to override or manipulate an AI system's intended instructions.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

Input designed to override or manipulate an AI system's intended instructions. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Prompt injection is an instruction inside user-controlled content that attempts to change the model’s intended behavior.
- The attack exploits the model’s tendency to treat natural-language data and natural-language instructions similarly.
- Defenses combine trust separation, tool restrictions, output validation, and minimizing sensitive context.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Prompt Injection affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Threat-model assistants, agents, and RAG systems that process untrusted text.
- Design policies for which content may influence decisions or tool calls.

## Example

A user message tells an assistant to ignore its system policy and reveal hidden configuration; the application must not treat that request as authorized.

## Trade-offs and limitations

- No prompt wording alone provides complete protection.
- Detection models and filters can miss novel or obfuscated attacks.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Prompt Injection expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Safety, Privacy, and Reliability](../../../../l10n/uk_UA/)
- [Data Poisoning](../../../data-poisoning/l10n/uk_UA/)
- [Indirect Prompt Injection](../../../indirect-prompt-injection/l10n/uk_UA/)
