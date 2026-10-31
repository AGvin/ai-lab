# Granite Speech 5.0

Granite Speech 5.0 is IBM's speech family covering **two distinct 470M TurboCTC ASR checkpoints** and a separate approximately **2.3B speech-language checkpoint** with multilingual speech recognition and translation. The 2B model is not a TurboCTC variant. [IBM 2B model card](https://huggingface.co/ibm-granite/granite-speech-5.0-2b).

## Current model boundaries

As of 21 October 2026, the standard `granite-speech-5.0-470m-turboctc` card is multilingual and explicitly lists English, French, German, Spanish, Portuguese, Italian and Japanese. Its weights state Apache 2.0.

The separate `granite-speech-5.0-470m-turboctc-nc` checkpoint remains English-only and states CC-BY-NC-SA-4.0. The standard model's multilingual update must not be projected onto the NC model.

All three models require representative audio evaluation for accents, noise, punctuation/capitalization, latency and selected runtime. The 2B checkpoint supports a separate prompt and language/translation contract, not automatically the 470M one. The older standard TurboCTC English-only revision remains historical revision state, not another learned identity. [IBM 2B card](https://huggingface.co/ibm-granite/granite-speech-5.0-2b) [IBM 470M card](https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc).

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [Granite Speech 5.0 470M TurboCTC](sub/models/sub/granite-speech-5-0-470m-turboctc/) — member.
- [Granite Speech 5.0 470M TurboCTC NC](sub/models/sub/granite-speech-5-0-470m-turboctc-nc/) — member.
- [Granite Speech 5.0 2B](sub/models/sub/granite-speech-5-0-2b/) — distinct speech-language member.

## Official resources

- <https://huggingface.co/collections/ibm-granite/granite-speech>
- <https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc>
- <https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc-nc>
- <https://huggingface.co/ibm-granite/granite-speech-5.0-2b>
