# Large Language Models

<!--
ai_content:
  managed: true
  l10n: true
-->

Language-focused foundation models that predict and generate token sequences.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Language-focused foundation models that predict and generate token sequences. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A large language model predicts token sequences using parameters learned from large text or multimodal corpora.
- During generation, the model repeatedly estimates a distribution for the next token, selects a token according to decoding rules, and updates its generation state.
- Instruction tuning and preference optimization can make a base model follow requests more reliably without changing the basic next-token objective used during inference.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Large Language Models affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Generate, transform, classify, summarize, and reason over natural-language or code input.
- Provide the language component inside assistants, agents, RAG systems, and tool-using applications.

## Example

An LLM can draft a migration plan from repository context, but the surrounding application must supply the files and validate the proposed changes.

## Trade-offs and limitations

- Fluent output can be unsupported, outdated, or logically inconsistent.
- The model does not automatically have live access to private data, the web, tools, or persistent memory.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Large Language Models expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Foundations and Architecture](../../)
- [Foundation Models](../foundation-models/)
- [Multimodal Models](../multimodal-models/)
