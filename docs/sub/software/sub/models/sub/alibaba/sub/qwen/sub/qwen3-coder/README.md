# Qwen3-Coder

Qwen3-Coder is the Qwen3 specialized model line for coding agents and tool-using software workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification boundary

Qwen3-Coder is a model line, not one exact model. Classification must be recorded for the exact artifact or hosted deployment:

- the launch `Qwen3-Coder-480B-A35B-Instruct` artifact is an [LLM](../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) with [Sparse — MoE](../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/) architecture, 480B total parameters, and 35B active parameters;
- [Qwen3-Coder-Next](./sub/qwen3-coder-next/) is documented separately as an LLM with sparse MoE architecture, 80B total parameters, and 3B active parameters;
- frontier status and [ecosystem status](../../../../../../../../../notes/sub/glossary/#model-ecosystem-status) must be assessed for an exact model, task scope, evidence set, and date rather than inherited from the family name.

Active parameter count does not determine scale class, storage requirements, consumer-hardware fit, or coding quality.

## Identity boundary

The comparison candidate names the specialized line, not one exact artifact. At launch, the Qwen Team introduced multiple sizes and named `Qwen3-Coder-480B-A35B-Instruct` as the first flagship artifact: a mixture-of-experts model with 480 billion total and 35 billion active parameters, 256,000 native context, and up to one million tokens through extrapolation methods.

`qwen3-coder-plus` is a hosted Alibaba Cloud Model Studio deployment alias. Qwen Code is a coding tool. Neither replaces the canonical Qwen3-Coder line or an exact downloadable artifact identity.

## Concrete models

- [Qwen3-Coder-Next](./sub/qwen3-coder-next/) — a concrete open-weight coding-agent model.

## Selection guidance

Resolve a Qwen3-Coder evaluation to an exact artifact or hosted model ID before comparing quality, context, cost, infrastructure, scale, architecture, frontier status, or ecosystem maturity. Do not carry the launch flagship's specifications or labels onto every descendant.

The line identity and launch details were verified on 2026-07-25.

## Related pages

- [Qwen model family](../../)
- [Alibaba models](../../../..)
- [Small and Large Language Models](../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Mixture of Experts](../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/)
- [Frontier Models](../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/frontier-models/)

## Sources

- [Qwen3-Coder launch](https://qwenlm.github.io/blog/qwen3-coder/)
- [Qwen3-Coder-Next model card](https://huggingface.co/Qwen/Qwen3-Coder-Next)