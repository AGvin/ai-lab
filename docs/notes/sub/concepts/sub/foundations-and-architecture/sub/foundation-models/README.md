# Foundation Models

A foundation model is a broadly trained model that can support many downstream tasks through prompting, retrieval, tools, fine-tuning, or adapters.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Instead of training a separate model from scratch for every task, a foundation model learns reusable representations from large and diverse data. Language models, vision-language models, and general image-generation models are common examples.

## Adaptation methods

- Zero-shot and few-shot prompting.
- System prompts and structured outputs.
- Retrieval-Augmented Generation.
- Tool calling and agent workflows.
- Fine-tuning, LoRA, or other adapters.

## Practical use

Foundation models reduce the cost of building new applications because one model can support summarization, extraction, coding, search, generation, and many other tasks. Selection should consider capability, license, privacy, deployment options, and evaluation results.

## Trade-offs and limitations

Broad capability does not guarantee domain accuracy. Pretraining data may be outdated, biased, incomplete, or legally restricted. Large models also require substantial inference resources or provider dependence.

## Common mistakes

- Assuming a general model needs no task-specific evaluation.
- Fine-tuning before testing prompting and retrieval.
- Ignoring model and dataset licensing.
- Treating the model as a complete application without controls or tools.

## Related concepts

- [Foundations and Architecture](../../)
- [Large Language Models](../large-language-models/)
- [Multimodal Models](../multimodal-models/)
- [Fine-Tuning](../../../training-and-adaptation/sub/fine-tuning/)