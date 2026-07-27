# Qwen3-Coder-Next

Qwen3-Coder-Next is a concrete Qwen open-weight language model designed for coding agents and local development.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Scale class: [LLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab model-selection context.
- Architecture: [Sparse — Mixture of Experts](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/) within a hybrid Gated DeltaNet and gated-attention design.
- Total parameters: 80B.
- Active parameters: 3B according to the official model card.
- Frontier status: not assessed for this exact model and coding scope.
- Ecosystem status: unclear until a dated adoption and tooling review is recorded.

The 3B active count does not make this an SLM and must not be used as the storage, RAM, or VRAM requirement. Scale, architecture, deployment feasibility, frontier status, and ecosystem maturity remain separate fields.

## Official profile

- Artifact: `Qwen/Qwen3-Coder-Next`
- License: Apache-2.0
- Type: causal language model
- Architecture: hybrid Gated DeltaNet, gated attention, and mixture-of-experts layout
- Parameters: 80 billion total and 3 billion active
- Native context length: 262,144 tokens
- Reasoning mode: non-thinking only

The official model card documents Transformers for direct use and SGLang or vLLM for OpenAI-compatible serving.

## Deployment and hardware guidance

The model card documents tensor-parallel deployment and advises reducing context length, for example to 32,768 tokens, if a server cannot start or encounters out-of-memory errors. It does not establish a general consumer-GPU fit.

No quantization is selected by the current comparison. Evaluate an exact quantized artifact separately rather than applying its behavior or memory use to the canonical base artifact. Quantization does not change the LLM scale label or MoE architecture.

## Limitations and suitable workloads

The model does not generate thinking blocks and supports only non-thinking mode. It is intended for coding agents, long-horizon coding tasks, complex tool use, and recovery from execution failures; verify quality and serving behavior on the target repository and runtime.

## Evidence

Artifact metadata, architecture, total and active parameters, context, license, and runtime guidance were rechecked from the official technical report and model card on 2026-07-27. The LLM label is a repository comparison convention for the current context. Frontier status, ecosystem status, consumer-hardware fit, and task-specific quality remain unassessed.

## Related pages

- [Qwen3-Coder specialized line](../../)
- [Qwen model family](../../../..)
- [Small and Large Language Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Mixture of Experts](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/)
- [Frontier Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/frontier-models/)

## Sources

- [Qwen3-Coder-Next technical report](https://github.com/QwenLM/Qwen3-Coder/blob/main/qwen3_coder_next_tech_report.pdf)
- [Qwen3-Coder-Next on Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-Next)
