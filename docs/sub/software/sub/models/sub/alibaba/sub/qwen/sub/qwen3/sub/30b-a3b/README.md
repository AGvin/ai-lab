# Qwen3 30B-A3B

Qwen3 30B-A3B is a post-trained mixture-of-experts Qwen3 language model used as a higher-capacity local candidate in the current portfolio profiles.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Scale class: [LLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab local-model comparison context.
- Architecture: [Sparse — Mixture of Experts](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/).
- Total parameters: 30.5B.
- Active parameters: 3.3B per token according to the official model card.
- Frontier status: not assessed for this exact model and workload scope.
- Ecosystem status: unclear until a dated adoption and tooling review is recorded.

The LLM scale label follows total model capacity and the current comparison context. The 3.3B active count does not reclassify the model as an SLM and must not be used as its storage or VRAM requirement.

## Official profile

- Model repository: `Qwen/Qwen3-30B-A3B`
- Architecture: mixture-of-experts causal language model
- Parameters: 30.5B total; 3.3B active per token
- Non-embedding parameters: 29.9B
- Experts: 128 total; 8 active per token
- Layers: 48
- Context: 32,768 tokens natively; official guidance documents YaRN extension to 131,072
- License: Apache-2.0
- Training stage: pretraining and post-training

The official model card describes thinking and non-thinking modes, multilingual work, coding, reasoning, instruction following, and tool-integrated agent capabilities. Total and active parameter counts do not establish quality, speed, or memory use for a concrete runtime.

## Official GGUF artifact

The official `Qwen/Qwen3-30B-A3B-GGUF` repository publishes several quantizations. The current portfolio uses:

- Artifact: `Qwen3-30B-A3B-Q4_K_M.gguf`
- Published file size: approximately 18.6 GB
- License: Apache-2.0

On a 24 GB GPU, the file size leaves limited nominal headroom before runtime buffers and KV cache. Treat this as a constrained candidate until the exact runtime, context, batch size, and concurrent services are measured. Quantization reduces representation size but does not change the MoE architecture or total-versus-active distinction.

## Selection guidance

Consider the `Q4_K_M` artifact for:

- sequential use on one 24 GB GPU after unloading a smaller resident model;
- a resident text core on one GPU in a two-GPU system after exact memory and throughput validation;
- private workloads where its measured accepted-result quality materially exceeds a smaller local model;
- comparison against hosted economic and flagship routes.

Do not infer that mixture-of-experts activation makes the model equivalent to a 3.3B dense model in memory, scale class, or quality. Complete weights, shared layers, routing implementation, runtime, and cache behavior remain relevant.

## Evidence boundary

Architecture, total and active parameter counts, context, license, and published artifact size are provider-documented. The LLM label is a repository comparison convention for the current context. The current 24 GB classification is a planning inference and must not be presented as a benchmarked production fit. Frontier status, ecosystem status, quality, and accepted-result cost remain unassessed.

## Related pages

- [Qwen3](../..)
- [Qwen](../../../..)
- [Small and Large Language Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Mixture of Experts](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/)
- [Frontier Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/frontier-models/)

## Sources

- [Qwen3-30B-A3B model card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-30B-A3B-GGUF repository](https://huggingface.co/Qwen/Qwen3-30B-A3B-GGUF)