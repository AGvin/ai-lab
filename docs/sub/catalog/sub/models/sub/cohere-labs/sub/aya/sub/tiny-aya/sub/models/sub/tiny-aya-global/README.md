# Tiny Aya Global

Tiny Aya Global is a globally balanced instruction-tuned 3.35-billion-parameter multilingual text model developed by Cohere and Cohere Labs. Its current documentation covers 70 languages and an 8K context, with emphasis on a balance across languages and regions. [Source 1](https://huggingface.co/CohereLabs/tiny-aya-global) · [Source 2](https://docs.cohere.com/docs/tiny-aya)

## Identity, coverage and provenance

The exact weight repository is `CohereLabs/tiny-aya-global`. Its card credits both Cohere and Cohere Labs and identifies a 3.35B model. The current model documentation lists 70 supported languages and positions Global for a balance across languages and regions. That emphasis is not an exclusive language boundary. [Specific model card](https://huggingface.co/CohereLabs/tiny-aya-global) · [Current coverage and positioning](https://docs.cohere.com/docs/tiny-aya)

## Training lineage

The technical paper describes Global's instruction and lightweight preference training from Tiny Aya Base. Global is also the global post-trained merge parent used in the final Earth, Fire and Water releases. The February 17 release date and March 12 technical-paper date are separate milestones. [Training procedure and release relationships](https://arxiv.org/html/2603.11510v1) · [Model launch](https://cohere.com/blog/cohere-labs-tiny-aya)

## Hosted and local access

The current Cohere Chat identifier is `tiny-aya-global`, listed as live with 8K context and an 8K maximum output. These are separate documented limits, not a promise of a 16K combined request. Official weights require accepting the displayed access conditions and are distributed under CC-BY-NC-4.0 with Cohere Labs acceptable-use terms. GGUF or other quantizations are artifact choices for this identity. [Current endpoint table](https://docs.cohere.com/docs/models) · [Weight conditions](https://huggingface.co/CohereLabs/tiny-aya-global) · [Local distributions](https://docs.cohere.com/docs/tiny-aya)

## Operation and evaluation

Follow the authored card's AutoTokenizer/AutoModelForCausalLM workflow and apply the matching chat template. Pin model revision, tokenizer, runtime, precision and generation settings. Measure memory and response quality with the intended context on the actual device, and compare translation direction, factual consistency and instruction following in the required languages. Reported regional benchmark gains describe particular evaluations rather than universal superiority. [Usage](https://huggingface.co/CohereLabs/tiny-aya-global) · [Evaluation design](https://arxiv.org/html/2603.11510v1)

## Relations

- Derived models: [Tiny Aya Earth](../tiny-aya-earth/README.md), [Tiny Aya Fire](../tiny-aya-fire/README.md), [Tiny Aya Water](../tiny-aya-water/README.md)
- Member of: [Tiny Aya](../../../../README.md)
- Produced by: [Cohere](../../../../../../../../../../../producers/sub/c/sub/cohere/README.md)

## Official resources

- <https://huggingface.co/CohereLabs/tiny-aya-global>
- <https://docs.cohere.com/docs/tiny-aya>
- <https://arxiv.org/html/2603.11510v1>
- <https://cohere.com/blog/cohere-labs-tiny-aya>
- <https://docs.cohere.com/docs/models>
- <https://huggingface.co/CohereLabs/tiny-aya-base>
