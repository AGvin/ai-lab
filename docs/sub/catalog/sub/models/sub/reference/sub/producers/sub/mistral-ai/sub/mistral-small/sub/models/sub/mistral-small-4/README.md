# Mistral Small 4

Mistral Small 4 is an open-weight multimodal Mixture-of-Experts model in the Mistral Small family.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical profile

- Model repository: `mistralai/Mistral-Small-4-119B-2603`
- Architecture: Mixture of Experts (MoE), 128 experts with 4 active
- Total parameters: 119B
- Activated parameters: 6.5B per token in the current official model card
- Input modalities: text and image
- Output modality: text
- Context length: 256K tokens
- Reasoning: configurable instruct/reasoning modes in the current model card
- License: Apache 2.0

Parameter activation is an architecture fact, not a storage or residency estimate. Exact memory use depends on the artifact, precision, runtime, context, and serving configuration.

## Evidence boundary

Mistral publishes coding, agentic, reasoning, throughput, and latency claims for the model. Those claims remain provider evidence until validated for a concrete AI Lab selection task; they are not copied into reference as workload rankings.

## Official resources

- [Mistral Small 4 model card](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
- [Mistral Small 4 documentation](https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03)
- [Introducing Mistral Small 4](https://mistral.ai/news/mistral-small-4/)
