# Qwen3-Coder-Next

Qwen3-Coder-Next is a concrete Qwen open-weight language model designed for coding agents and local development.

## Translations

- English
- [Українська](./l10n/uk_UA/)

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

No quantization is selected by the current comparison. Evaluate an exact quantized artifact separately rather than applying its behavior or memory use to the canonical base artifact.

## Limitations and suitable workloads

The model does not generate thinking blocks and supports only non-thinking mode. It is intended for coding agents, long-horizon coding tasks, complex tool use, and recovery from execution failures; verify quality and serving behavior on the target repository and runtime.

## Evidence

Artifact metadata, architecture, context, license, and runtime guidance were verified on 2026-07-25.

## Related pages

- [Qwen3-Coder specialized line](../../)
- [Qwen model family](../../../..)

## Sources

- [Qwen3-Coder-Next model card](https://huggingface.co/Qwen/Qwen3-Coder-Next)
