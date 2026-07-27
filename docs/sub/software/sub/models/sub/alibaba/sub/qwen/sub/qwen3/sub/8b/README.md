# Qwen3 8B

Qwen3 8B is a dense post-trained Qwen3 language model used as a local generalist candidate in the current model-portfolio profiles.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Scale class: [SLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab local-model comparison context.
- Architecture: [Dense](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/).
- Frontier status: not assessed for this exact model and workload scope.
- Ecosystem status: unclear until a dated adoption and tooling review is recorded.

The SLM label is contextual. It does not mean local-only, universally small, or automatically suitable for constrained hardware. Quantization and deployment fit remain separate properties.

## Official profile

- Model repository: `Qwen/Qwen3-8B`
- Architecture: dense causal language model
- Parameters: 8.2B total; 6.95B excluding embeddings
- Layers: 36
- Context: 32,768 tokens natively; official guidance documents YaRN extension to 131,072
- License: Apache-2.0
- Training stage: pretraining and post-training

The official model card describes thinking and non-thinking modes, multilingual support, reasoning, coding, instruction following, and tool-integrated agent capabilities. These are provider claims and do not replace assignment-level evaluation.

## Official GGUF artifact

The official `Qwen/Qwen3-8B-GGUF` repository publishes several quantizations. The current local portfolio uses:

- Artifact: `Qwen3-8B-Q4_K_M.gguf`
- Published file size: 5.03 GB
- License: Apache-2.0

File size is not peak VRAM. Runtime buffers, KV cache, context, batching, GPU offload, and concurrent services must be measured. A quantized artifact remains a representation of the underlying model; it does not create a separate scale class.

## Selection guidance

Consider the `Q4_K_M` artifact for:

- CPU-only or low-memory batch work where measured latency is acceptable;
- an economical local baseline;
- private preprocessing, classification, summarization, or draft work after task-specific validation;
- experimentation on 8–12 GB VRAM classes.

Do not assume that 8B is a reliable orchestrator, reviewer, or autonomous coding agent without role-specific testing. Escalate repeated omissions, tool failures, or quality-limit failures to a different model or human review rather than repeating the same prompt indefinitely.

## Evidence boundary

The architecture, parameter count, context, license, and published artifact size were rechecked from the official Qwen3 release and Hugging Face repositories on 2026-07-27. The SLM label is a repository comparison convention for the current context. Deployment fit, agent-role suitability, quality ceiling, frontier status, ecosystem status, and accepted-result cost remain unverified until assessed explicitly.

## Related pages

- [Qwen3](../..)
- [Qwen](../../../..)
- [Small and Large Language Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Frontier Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/frontier-models/)

## Sources

- [Qwen3 release](https://qwenlm.github.io/blog/qwen3/)
- [Qwen3-8B on Hugging Face](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-8B-GGUF repository](https://huggingface.co/Qwen/Qwen3-8B-GGUF)
- [Qwen3-8B Q4_K_M file](https://huggingface.co/Qwen/Qwen3-8B-GGUF/blob/main/Qwen3-8B-Q4_K_M.gguf)
