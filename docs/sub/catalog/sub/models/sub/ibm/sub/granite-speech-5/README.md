# Granite Speech 5.0

Granite Speech 5.0 is IBM's compact TurboCTC automatic-speech-recognition family represented by two separate 470M-class checkpoints.

## Current model boundaries

As of 21 October 2026, the standard `granite-speech-5.0-470m-turboctc` card is multilingual and explicitly lists English, French, German, Spanish, Portuguese, Italian and Japanese. Its weights state Apache 2.0.

The separate `granite-speech-5.0-470m-turboctc-nc` checkpoint remains English-only and states CC-BY-NC-SA-4.0. The standard model's multilingual update must not be projected onto the NC model.

Both models require representative ASR evaluation for accents, noise, punctuation/capitalization, latency and the selected runtime. An older revision of the standard model being English-only is revision history, not another learned identity.

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [Granite Speech 5.0 470M TurboCTC](sub/models/sub/granite-speech-5-0-470m-turboctc/) — member.
- [Granite Speech 5.0 470M TurboCTC NC](sub/models/sub/granite-speech-5-0-470m-turboctc-nc/) — member.

## Official resources

- <https://huggingface.co/collections/ibm-granite/granite-speech>
- <https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc>
- <https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc-nc>
