# Mistral Large 3 675B Instruct 2512

Mistral Large 3 675B Instruct 2512 is Mistral AI’s December 2025 multimodal Mixture-of-Experts instruct checkpoint.

## Translations

- English

## Relations

- Family: [Mistral Large](../../../../)

## Model profile

Mistral reports 675B total and 41B active parameters, with a 256K-token context. The released FP8 instruct weights use Apache 2.0. [Mistral Large 3 model card](https://docs.mistral.ai/models/mistral-large-3-25-12) [Mistral Large 3 weights and limitations](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512)

The hosted `mistral-large-2512` release remains listed as GA. Its released weights are distinct from the newer Large 4 preview. [Mistral Large 3 model card](https://docs.mistral.ai/models/mistral-large-3-25-12)

## Operational boundaries

Mistral explicitly describes limitations in dedicated reasoning, vision-specialist tasks and deployment complexity. The model’s 41B active count does not mean that only 41B parameters need storage. [Mistral Large 3 weights and limitations](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512)

Use the model-specific tokenizer and tool parser; function output and JSON structure do not validate the correctness or authorization of an action. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

## Official resources

- [Mistral Large 3 weights and limitations](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512)
- [Mistral 3 release](https://mistral.ai/news/mistral-3/)
- [Mistral Large 3 model card](https://docs.mistral.ai/models/mistral-large-3-25-12)
- [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)
