# Pretraining

<!--
ai_content:
  managed: true
  l10n: true
-->

Pretraining is the large-scale initial training phase that creates a broadly capable base model before task-specific adaptation.

## Core idea

Language models commonly learn by predicting missing or next tokens from massive corpora. Vision and multimodal models use related self-supervised or paired-data objectives. Pretraining teaches broad representations, patterns, and capabilities that later stages refine.

## Main requirements

- Large, diverse, and carefully processed datasets.
- Distributed compute and storage infrastructure.
- Stable optimization across many training steps.
- Tokenization and architecture decisions made before training.
- Evaluation for capability, safety, contamination, and bias.

## Trade-offs and limitations

Pretraining is expensive and difficult to reproduce. Data provenance and licensing can be hard to audit at scale. The resulting model reflects historical data and does not automatically know events after the training period.

## Common mistakes

- Treating pretraining as ordinary fine-tuning at larger scale.
- Assuming more tokens always improve quality.
- Ignoring duplicated or low-quality web data.
- Expecting pretraining to provide current, attributable knowledge.

## Related concepts

- [Training and Adaptation](../../)
- [Foundation Models](../../../foundations-and-architecture/sub/foundation-models/)
- [Instruction Tuning](../instruction-tuning/)
- [Datasets](../datasets/)
