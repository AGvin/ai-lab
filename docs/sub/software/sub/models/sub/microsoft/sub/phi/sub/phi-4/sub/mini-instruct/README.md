# Phi-4 Mini Instruct

Phi-4 Mini Instruct is a compact Microsoft instruction-tuned language model for general-purpose, multilingual, reasoning, function-calling, and resource-constrained applications.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Model type: general-purpose instruction-tuned language model with reasoning and coding capability
- Scale class: [SLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab comparison context
- Architecture: [Dense](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/) decoder-only Transformer
- Frontier status: not assessed for this exact model and coding scope
- Ecosystem status: unclear until a dated adoption and tooling review is recorded

This is not a coding-specialized model. Its coding support must be evaluated together with its broader instruction-following and reasoning behavior.

## Official profile

- Model repository: `microsoft/Phi-4-mini-instruct`
- Parameters: 3.8B
- Context length: 131,072 tokens
- Architecture: dense decoder-only Transformer with grouped-query attention
- Training stage: supervised fine-tuning and direct preference optimization after pretraining
- License: MIT
- Supported inputs and outputs: text input and generated text output
- Supported languages: 24 languages, including Ukrainian

## Selection guidance

Consider this model for:

- compact local or self-hosted mixed workloads that include code, reasoning, and general instructions;
- multilingual developer assistance;
- latency- or memory-constrained applications;
- function-calling experiments and structured assistant workflows after scaffold-specific validation.

Prefer a coding-specialized SLM when code quality is the dominant objective and representative tests show a material advantage. Escalate to a larger or hosted model when repository understanding, architecture, long tool sequences, or repeated omissions exceed the demonstrated capability of the compact route.

## Evidence boundary

Model identity, parameter count, architecture, context, training stages, license, languages, and intended constrained-environment use were verified from official Microsoft sources on 2026-07-26. The SLM label is an AI Lab comparison convention. Coding quality, local hardware fit, throughput, frontier status, ecosystem status, and accepted-result cost remain deployment- and task-specific.

## Related pages

- [Phi-4](../..)
- [Phi model family](../../../..)
- [Microsoft models](../../../../../..)
- [Small and Large Language Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Choosing Models for Coding](../../../../../../../../../../../notes/sub/comparisons/sub/model-selection/sub/coding/)

## Sources

- [Phi-4 Mini technical report](https://www.microsoft.com/en-us/research/publication/phi-4-mini-technical-report-compact-yet-powerful-multimodal-language-models-via-mixture-of-loras/)
- [Phi-4 Mini Instruct model card](https://huggingface.co/microsoft/Phi-4-mini-instruct)
