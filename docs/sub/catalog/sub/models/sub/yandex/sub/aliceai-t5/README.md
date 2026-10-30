# AliceAI-T5

> ⚠️ **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL.** Yandex lists its headquarters in Moscow, Russia. Under AI Lab's unconditional policy, this Yandex model or model index is **not recommended for adoption**, regardless of audits, licensing or sanctions status. Retained for **research and threat monitoring only**. Never send confidential data to Yandex endpoints; examine any downloaded weights or custom code only in isolation. The policy classification does not assert proven malware in a specific artifact. [Policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) · [Yandex company address](https://www.yandex.com/company/contacts/moscow).

AliceAI-T5 is Yandex's **sparse mixture-of-experts encoder-decoder language-model family**. Its [released base checkpoint](./sub/models/sub/aliceai-t5-35b-a0-6b/) uses UL2-style text-to-text modeling rather than the decoder-only architecture of many chat-oriented LLMs.

## Family and deployment boundaries

The released model is a **base model**, not the hosted Alice assistant, instruction-tuned dialogue service or interchangeable decoder-only inference endpoint. The publisher's official example loads a custom Transformers architecture with `trust_remote_code=True`; inspect, version-pin and trust that model code before executing it. Model-card benchmark comparisons are publisher-produced results and do not establish general inference runtime compatibility.

## Translations

- English

## Relations

- Produced by: [Yandex](../../../../../producers/sub/y/sub/yandex/)
- Has member: [AliceAI-T5-35B-A0.6B](./sub/models/sub/aliceai-t5-35b-a0-6b/)

## Official resources

- [Official Yandex model repository](https://huggingface.co/yandex/AliceAI-T5-35B-A0.6B)
