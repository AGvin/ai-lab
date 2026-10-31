# Tiny Aya Water

Tiny Aya Water is a region-specialized instruction-tuned 3.35-billion-parameter multilingual text model developed by Cohere and Cohere Labs. Its current documentation covers 70 languages and an 8K context, with emphasis on European and Asia-Pacific language tasks. [Source 1](https://huggingface.co/CohereLabs/tiny-aya-water) · [Source 2](https://docs.cohere.com/docs/tiny-aya)

## Identity, coverage and provenance

The exact weight repository is `CohereLabs/tiny-aya-water`. Its card credits both Cohere and Cohere Labs and identifies a 3.35B model. The current model documentation lists 70 supported languages and positions Water for European and Asia-Pacific language tasks. That emphasis is not an exclusive language boundary. [Specific model card](https://huggingface.co/CohereLabs/tiny-aya-water) · [Current coverage and positioning](https://docs.cohere.com/docs/tiny-aya)

## Training lineage

The technical paper describes Water as a final regional release formed by merging a region-specialized post-trained checkpoint with Tiny Aya Global. This trained merge ancestry is separate from its membership in the Tiny Aya series. The February 17 release date and March 12 technical-paper date are separate milestones. [Training procedure and release relationships](https://arxiv.org/html/2603.11510v1) · [Model launch](https://cohere.com/blog/cohere-labs-tiny-aya)

## Hosted and local access

The current Cohere Chat identifier is `tiny-aya-water`, listed as live with 8K context and an 8K maximum output. These are separate documented limits, not a promise of a 16K combined request. Official weights require accepting the displayed access conditions and are distributed under CC-BY-NC-4.0 with Cohere Labs acceptable-use terms. GGUF or other quantizations are artifact choices for this identity. [Current endpoint table](https://docs.cohere.com/docs/models) · [Weight conditions](https://huggingface.co/CohereLabs/tiny-aya-water) · [Local distributions](https://docs.cohere.com/docs/tiny-aya)

## Operation and evaluation

Follow the authored card's AutoTokenizer/AutoModelForCausalLM workflow and apply the matching chat template. Pin model revision, tokenizer, runtime, precision and generation settings. Measure memory and response quality with the intended context on the actual device, and compare translation direction, factual consistency and instruction following in the required languages. Reported regional benchmark gains describe particular evaluations rather than universal superiority. [Usage](https://huggingface.co/CohereLabs/tiny-aya-water) · [Evaluation design](https://arxiv.org/html/2603.11510v1)

## Relations

- Derived from: [Tiny Aya Global](../tiny-aya-global/README.md)
- Member of: [Tiny Aya](../../../../README.md)
- Produced by: [Cohere](../../../../../../../../../../../producers/sub/c/sub/cohere/README.md)

## Official resources

- <https://huggingface.co/CohereLabs/tiny-aya-water>
- <https://docs.cohere.com/docs/tiny-aya>
- <https://arxiv.org/html/2603.11510v1>
- <https://cohere.com/blog/cohere-labs-tiny-aya>
- <https://docs.cohere.com/docs/models>
- <https://huggingface.co/CohereLabs/tiny-aya-base>
