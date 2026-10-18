# Shieldstral 1.0 3B

Shieldstral 1.0 3B is Mistral AI’s policy-adaptive text-and-image safety classifier, released on August 4, 2026.

## Translations

- English

## Relations

- Family: [Shieldstral](../../../../)

## Model profile

The released repository is `mistralai/Shieldstral-1.0-3B`, based on Ministral 3 3B Base with a vision encoder, under Apache 2.0. Its marketed 3B name is retained; the docs list 3.8B total parameters. [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B) [Shieldstral 1.0 model card](https://docs.mistral.ai/models/shieldstral-1-0)

A natural-language policy question and the content to classify produce yes/no logits and a continuous score. The documented training range is 32K tokens. [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B)

## Scope and boundaries

Mistral documents self-hosting only, with no hosted Mistral API endpoint. Its model page labels the release public preview. [Self-hosted policy moderation with Shieldstral](https://docs.mistral.ai/resources/cookbooks/mistral-moderation-shieldstral_policy_moderation) [Shieldstral 1.0 model card](https://docs.mistral.ai/models/shieldstral-1-0)

Thresholds are application policy. Mistral reports uneven language/domain coverage and reduced reliability on obfuscated inputs or long documents; classification cannot guarantee prevention of harmful behavior. [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B)

## Official resources

- [Shieldstral release](https://mistral.ai/news/shieldstral/)
- [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B)
- [Shieldstral 1.0 model card](https://docs.mistral.ai/models/shieldstral-1-0)
- [Self-hosted policy moderation with Shieldstral](https://docs.mistral.ai/resources/cookbooks/mistral-moderation-shieldstral_policy_moderation)
