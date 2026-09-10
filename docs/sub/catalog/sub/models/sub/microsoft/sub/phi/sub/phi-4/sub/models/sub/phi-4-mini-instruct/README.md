# Phi-4 Mini Instruct

Phi-4 Mini Instruct is a Microsoft instruction-tuned text model in the Phi-4 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical profile

- Model repository: `microsoft/Phi-4-mini-instruct`
- Parameters: 3.8B
- Architecture: dense decoder-only Transformer with grouped-query attention
- Input: text
- Output: generated text
- Context length: 128K tokens
- Post-training: supervised fine-tuning and direct preference optimization
- License: MIT
- Language coverage: 24 languages in the current model card, including Ukrainian

These are model facts from the current Microsoft model card. Runtime-specific throughput, memory fit, coding quality, translation quality, function-calling reliability, and accepted-result cost require separate deployment or task evaluation.

## Evidence boundary

Microsoft describes the model as intended for broad multilingual use, reasoning-heavy tasks, and compute- or latency-constrained environments, but those intended-use statements are not a task-specific AI Lab recommendation. Coding, translation, agent, or other suitability conclusions belong in the corresponding selection pages after representative testing.

## Official resources

- [Phi-4 Mini Instruct model card](https://huggingface.co/microsoft/Phi-4-mini-instruct)
