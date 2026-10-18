# Ministral 3 8B Instruct 2512

Ministral 3 8B Instruct 2512 is the instruction-tuned multimodal checkpoint in Mistral AI’s December 2025 Ministral 3 generation.

## Translations

- English

## Relations

- Family: [Ministral](../../../../)

## Model profile

The architecture has a 8.4B language model and a 0.4B vision encoder. The released instruct representation is FP8 under Apache 2.0. [Ministral 3 8B Instruct weights](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)

The GA API release `ministral-8b-2512` has a 256K-token context. Text and image inputs produce text, including function-call and JSON output. [Ministral 3 8B model card](https://docs.mistral.ai/models/ministral-3-8b-25-12)

## Operational boundaries

This is the Instruct checkpoint; the separately trained Base and Reasoning releases are not aliases. Mistral recommends a small, clearly defined tool set and avoiding extreme image aspect ratios. [Ministral 3 8B Instruct weights](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)

A parameter count is not a memory budget. The runtime, precision, images and context determine deployment requirements; the calling application controls tool execution.

## Official resources

- [Ministral 3 8B Instruct weights](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)
- [Ministral 3 8B model card](https://docs.mistral.ai/models/ministral-3-8b-25-12)
