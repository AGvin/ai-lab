# AliceAI-Foundation-80B-A3B-Base

> ⚠️ **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL.** The pretrained base checkpoint was published by Yandex, whose headquarters are in Moscow, Russia. This is an unconditional **AI Lab exclusion from adoption**, regardless of security scan results, Apache-2.0 licensing or sanctions status. Kept **only for research and threat monitoring**. Do not expose private data to Yandex systems; evaluate downloaded code and artifacts only in an isolated, restricted environment. This is a policy risk designation, not evidence of malware in this checkpoint. [Policy](../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) · [Official publisher location](https://www.yandex.com/company/contacts/moscow).

Yandex released **AliceAI-Foundation-80B-A3B-Base** on September 21, 2026 as an experimental pretrained-from-scratch **base** model, distinct from its AliceAI-T5 encoder-decoder family and the consumer Alice AI assistant. It exposes open weights under Apache-2.0, not a ready-made commercial chat endpoint. [Yandex release](https://www.yandex.com/company/news/2026-09-21).

## Architecture and intended use

The source card describes a hybrid-attention **mixture-of-experts** model with about **80 billion parameters total, 3 billion active per token**, and up to **262,144 tokens configured context**. The published base checkpoint is intended for research and adaptation; this is not proof of instruction-following, reliable agent behavior or a particular deployment's effective context. [Official model card](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base).

## Deployment and limitations

The publisher provides architecture-specific code and runtime examples. Inspect and pin the exact revision/dependencies before any `trust_remote_code` execution; verify framework support, whole-model weight storage, live VRAM/KV requirements, precision and throughput with the intended hardware. Three billion *active* parameters does not imply the weights consume only three-billion-parameter storage.

The license is **Apache-2.0 for released weights**; check other components and third-party runtime terms separately. Yandex benchmark comparisons, including Russian factual knowledge, math and code, have **not** been independently reproduced by AI Lab. No runtime inference or independent benchmark is credited here.

## Relations

- Member of: [AliceAI Foundation family](../../../../)

## Official resources

- [Original Yandex release](https://www.yandex.com/company/news/2026-09-21)
- [Published base-model weights and model card](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base)
