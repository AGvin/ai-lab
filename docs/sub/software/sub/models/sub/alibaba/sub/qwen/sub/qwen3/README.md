# Qwen3

Qwen3 is a Qwen language-model generation that includes dense and mixture-of-experts variants for reasoning, instruction following, multilingual work, coding, and tool-integrated agent workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Shared characteristics

Official model cards describe Qwen3 post-trained variants as supporting:

- thinking and non-thinking response modes;
- multilingual instruction following and translation across more than 100 languages and dialects;
- coding, mathematical, and general reasoning workloads;
- external-tool integration and agent-oriented tasks;
- Apache-2.0 licensed downloadable weights for the documented variants.

Native context for the documented 8B, 14B, and 30B-A3B variants is 32,768 tokens. Official guidance documents extension to 131,072 tokens with YaRN. Extended context is a deployment option, not proof that quality, latency, or memory remain acceptable for a specific workload.

## Architecture variants

- **Dense** — all model parameters participate in each token computation. Qwen3 8B and 14B are dense variants.
- **Mixture of experts** — a subset of experts is activated per token. Qwen3 30B-A3B has 30.5 billion total parameters and 3.3 billion activated parameters according to its official model card.

Parameter count and activated-parameter count do not determine practical quality or memory use by themselves. Runtime, precision, quantization, context, KV cache, batching, and implementation remain material.

## Documented versions

- [Qwen3 8B](./sub/8b/) — dense 8.2B-parameter variant and official GGUF artifacts.
- [Qwen3 14B](./sub/14b/) — dense 14.8B-parameter variant and official GGUF artifacts.
- [Qwen3 30B-A3B](./sub/30b-a3b/) — mixture-of-experts variant with 30.5B total and 3.3B activated parameters.

## Selection guidance

Use the exact version and artifact in recommendations. Do not transfer an evaluation between:

- base and post-trained variants;
- full-precision weights and a quantized artifact;
- one runtime or prompt template and another;
- native and extended context;
- local and hosted deployments.

The current VRAM-oriented comparison treats official `Q4_K_M` GGUF files as planning candidates and requires measurement before declaring a deployment comfortable or production-ready.

## Related pages

- [Qwen](../..)
- [Alibaba models](../../../..)
- [Models](../../../../../..)

## Sources

- [Qwen3 technical report](https://arxiv.org/abs/2505.09388)
- [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-14B model card](https://huggingface.co/Qwen/Qwen3-14B)
- [Qwen3-30B-A3B model card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
