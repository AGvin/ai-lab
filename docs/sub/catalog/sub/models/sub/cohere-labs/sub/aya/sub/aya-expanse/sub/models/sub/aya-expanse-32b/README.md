# Aya Expanse 32B

Aya Expanse 32B is Cohere Labs' 32-billion-parameter multilingual text model, released on 24 October 2024. Its model card documents text input/output, 23 supported languages and a 128K context window. [Source 1](https://huggingface.co/CohereLabs/aya-expanse-32b) · [Source 2](https://cohere.com/blog/aya-expanse-connecting-our-world)

## Identity and language-model role

Aya Expanse 32B is a text-input, text-output autoregressive transformer with multilingual posttraining. It is a separate trained model from Expanse 8B. The Aya Vision 32B card explicitly identifies this Expanse model as its language component, combined with a vision encoder and multimodal adapter. [Model card](https://huggingface.co/CohereLabs/aya-expanse-32b) · [Release](https://cohere.com/blog/aya-expanse-connecting-our-world) · [Derived Vision model](https://huggingface.co/CohereLabs/aya-vision-32b)

## Access and limits

The current Cohere Chat identifier is `c4ai-aya-expanse-32b`. Its documentation lists 128K context and a 4K maximum output. The official `CohereLabs/aya-expanse-32b` repository separately provides gated weights under CC-BY-NC-4.0 with acceptable-use terms. A hosted output cap is not an intrinsic parameter-count or weight-format distinction. [Current route and limits](https://docs.cohere.com/docs/aya-expanse) · [Weight distribution](https://huggingface.co/CohereLabs/aya-expanse-32b)

## Operation and evaluation

For local use, follow the model card's AutoTokenizer/AutoModelForCausalLM and chat-template workflow with a pinned model revision. Plan memory for the full weights, precision and context workload. Test multilingual generation, translation and long-document recall with representative data; a large context window does not establish accurate retrieval at every position. [Usage and evaluation](https://huggingface.co/CohereLabs/aya-expanse-32b)

## Relations

- Derived models: [Aya Vision 32B](../../../../../aya-vision/sub/models/sub/aya-vision-32b/README.md)
- Member of: [Aya Expanse](../../../../README.md)

## Official resources

- <https://huggingface.co/CohereLabs/aya-expanse-32b>
- <https://cohere.com/blog/aya-expanse-connecting-our-world>
- <https://docs.cohere.com/docs/aya-expanse>
- <https://docs.cohere.com/docs/models>
- <https://huggingface.co/CohereLabs/aya-vision-32b>
