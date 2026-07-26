# Qwen2.5-Coder Model Line

Qwen2.5-Coder is the Qwen2.5 specialized language-model line for code generation, code reasoning, code repair, and coding-assistant workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model type

- Type: coding-specialized causal language models
- Training variants: base and instruction-tuned models
- Architecture family: dense decoder-only Transformers
- Access: downloadable open-weight artifacts

Model type, scale, architecture, deployment, and licensing are separate fields. Exact model pages record the values that apply to a concrete artifact.

## Documented models

- [Qwen2.5-Coder 3B Instruct](./sub/3b-instruct/) — economical instruction-tuned coding SLM with a 3.09B-parameter dense architecture.
- [Qwen2.5-Coder 7B Instruct](./sub/7b-instruct/) — stronger compact instruction-tuned coding SLM with a 7.61B-parameter dense architecture.

The official line also includes other sizes. Add their canonical pages only when a comparison or practical note requires exact coverage.

## Selection boundary

The smaller models are useful candidates for economical local coding assistance, but parameter count alone does not establish total cost or accepted-result quality. Measure runtime memory, throughput, retries, review effort, task acceptance, and the exact deployment artifact.

## Related pages

- [Qwen model family](../..)
- [Small and Large Language Models](../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Choosing Models for Coding](../../../../../../../../../notes/sub/comparisons/sub/model-selection/sub/coding/)

## Sources

- [Qwen2.5-Coder family release](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
- [Qwen2.5-Coder introduction](https://qwenlm.github.io/blog/qwen2.5-coder/)
