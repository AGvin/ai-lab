# Qwen3 8B

Qwen3 8B is a dense post-trained Qwen3 language model used as a local generalist candidate in the current model-portfolio profiles.

## Translations

- English
- [Українська](./l10n/uk_UA/)

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

File size is not peak VRAM. Runtime buffers, KV cache, context, batching, GPU offload, and concurrent services must be measured.

## Selection guidance

Consider the `Q4_K_M` artifact for:

- CPU-only or low-memory batch work where measured latency is acceptable;
- an economical local baseline;
- private preprocessing, classification, summarization, or draft work after task-specific validation;
- experimentation on 8–12 GB VRAM classes.

Do not assume that 8B is a reliable orchestrator, reviewer, or autonomous coding agent without role-specific testing. Escalate repeated omissions, tool failures, or quality-limit failures to a different model or human review rather than repeating the same prompt indefinitely.

## Evidence boundary

The architecture, parameter count, context, license, and published artifact size are provider-documented facts. Deployment fit, agent-role suitability, quality ceiling, and accepted-result cost remain repository recommendations or untested assumptions until measured.

## Related pages

- [Qwen3](../..)
- [Qwen](../../../..)

## Sources

- [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-8B-GGUF repository](https://huggingface.co/Qwen/Qwen3-8B-GGUF)
- [Qwen3-8B Q4_K_M file](https://huggingface.co/Qwen/Qwen3-8B-GGUF/blob/main/Qwen3-8B-Q4_K_M.gguf)
