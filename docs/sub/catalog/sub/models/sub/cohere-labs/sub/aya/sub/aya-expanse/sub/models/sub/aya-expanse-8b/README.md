# Aya Expanse 8B

Aya Expanse 8B is Cohere Labs' 8-billion-parameter multilingual text model, released on 24 October 2024. Its official card documents text input/output, 23 supported languages and an 8K context window. [Source 1](https://huggingface.co/CohereLabs/aya-expanse-8b) · [Source 2](https://cohere.com/blog/aya-expanse-connecting-our-world)

## Identity and capability

The 8B model is an autoregressive transformer for text generation. Its posttraining combines supervised fine-tuning, preference training and model merging. The model card identifies a Command-family foundation but does not identify an exact concrete parent checkpoint. It documents 23 languages and an 8K context. [Specific model card](https://huggingface.co/CohereLabs/aya-expanse-8b) · [24 October 2024 release](https://cohere.com/blog/aya-expanse-connecting-our-world)

## Weights and hosted access

Use the official repository `CohereLabs/aya-expanse-8b` for the weight identity. Downloading its files requires accepting the displayed access conditions; the card specifies CC-BY-NC-4.0 and Cohere Labs acceptable-use terms. The former Cohere Chat route `c4ai-aya-expanse-8b` retired on 4 April 2026. The currently live 32B route is a different model choice. [Weights and conditions](https://huggingface.co/CohereLabs/aya-expanse-8b) · [Retirement](https://docs.cohere.com/docs/deprecations) · [Current routes](https://docs.cohere.com/docs/models)

## Operation and evaluation

The authored card loads the model with AutoTokenizer and AutoModelForCausalLM and formats messages with the tokenizer's chat template. Pin the weight revision, matching tokenizer, runtime version and precision before comparing outputs. Budget input and generated tokens within the supported context, and test translation direction, factual consistency and instruction following in the actual languages used. Published benchmark rankings apply to their stated test setup. [Usage and evaluation](https://huggingface.co/CohereLabs/aya-expanse-8b)

## Relations

- Member of: [Aya Expanse](../../../../README.md)

## Official resources

- <https://huggingface.co/CohereLabs/aya-expanse-8b>
- <https://cohere.com/blog/aya-expanse-connecting-our-world>
- <https://docs.cohere.com/docs/deprecations>
- <https://docs.cohere.com/docs/models>
