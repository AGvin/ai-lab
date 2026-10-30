# AliceAI-T5-35B-A0.6B

**AliceAI-T5-35B-A0.6B** is Yandex's released **base sparse-MoE encoder-decoder text-to-text model**. Its official card describes approximately **34.35 billion unique parameters**, **512 experts per MoE layer** with **top-8 routing**, and a **128K-token context configuration** using RoPE with YaRN. The publisher's `A0.6B` identifier is not a substitute for estimating total stored weights, activation memory or runtime throughput.

## Architecture and operational boundaries

The model has separate encoder and decoder pathways and a custom `aliceai_t5_moe` implementation. The published Transformers loading example uses `trust_remote_code=True`: this executes model-supplied code, so inspect and pin its exact revision before use. Do not assume stock decoder-only inference software supports the encoder, cross-attention and decoder execution path.

The model is a **base** text-to-text checkpoint, not the consumer Alice assistant or an instruction-tuned chat model. Reported benchmarks are publisher-produced, not independently reproduced AI Lab comparisons. Maximum context length alone does not establish task accuracy, deployment memory or provider runtime compatibility. Community conversions and quantizations are separate distribution artifacts, not new original Yandex checkpoints.

## Translations

- English

## Relations

- Member of: [AliceAI-T5 family](../../../../)

## Official resources

- [Official Yandex model card and custom-code instructions](https://huggingface.co/yandex/AliceAI-T5-35B-A0.6B)
