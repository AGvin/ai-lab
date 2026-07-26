# Qwen3 14B

Qwen3 14B is a dense post-trained Qwen3 language model used as the resident local generalist candidate in several current portfolio profiles.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Scale class: [LLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab local-model comparison context.
- Architecture: [Dense](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/).
- Frontier status: not assessed for this exact model and workload scope.
- Ecosystem status: unclear until a dated adoption and tooling review is recorded.

The LLM label describes relative scale in this comparison context. It does not imply provider-hosted deployment, cluster-only operation, or a specific quality tier.

## Official profile

- Model repository: `Qwen/Qwen3-14B`
- Architecture: dense causal language model
- Parameters: 14.8B total; 13.2B excluding embeddings
- Layers: 40
- Context: 32,768 tokens natively; official guidance documents YaRN extension to 131,072
- License: Apache-2.0
- Training stage: pretraining and post-training

The official model card describes thinking and non-thinking modes, multilingual instruction following, translation, reasoning, coding, and tool-integrated agent capabilities. Validate each claimed capability on the intended assignment.

## Official GGUF artifact

The official `Qwen/Qwen3-14B-GGUF` repository publishes several quantizations. The current local portfolio uses:

- Artifact: `Qwen3-14B-Q4_K_M.gguf`
- Published file size: approximately 9 GB
- License: Apache-2.0

Published file size does not include all runtime memory. Measure buffers, KV cache, target context, batching, GPU offload, and concurrent services. Quantization changes representation and resource requirements but does not reclassify the underlying model as an SLM.

## Selection guidance

Consider the `Q4_K_M` artifact as a starting point for:

- one resident local generalist on 16–24 GB VRAM hardware;
- private drafting, coding assistance, routing, summarization, and low-risk automation after role-specific validation;
- a local orchestrator only when decomposition, tool use, state tracking, completion decisions, and escalation behavior pass independent tests;
- hybrid systems that reserve hosted models for difficult, multimodal, or high-risk work.

On a 24 GB GPU, Qwen3 14B generally offers more operational headroom than the official 30B-A3B `Q4_K_M` artifact. This is a planning inference from published file sizes, not a measured performance or quality ranking.

## Evidence boundary

The architecture, parameter count, context, license, and published artifact size are provider-documented. The LLM label is a repository comparison convention for the current context. Deployment fit, role suitability, reliability, frontier status, ecosystem status, and cost per accepted result remain workload-specific and require measurement.

## Related pages

- [Qwen3](../..)
- [Qwen](../../../..)
- [Small and Large Language Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Frontier Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/frontier-models/)

## Sources

- [Qwen3-14B model card](https://huggingface.co/Qwen/Qwen3-14B)
- [Qwen3-14B-GGUF repository](https://huggingface.co/Qwen/Qwen3-14B-GGUF)