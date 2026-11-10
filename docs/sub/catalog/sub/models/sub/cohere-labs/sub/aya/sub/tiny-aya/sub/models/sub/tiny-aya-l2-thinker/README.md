# Tiny Aya L2-Thinker

A separately released 3.35B Cohere/Cohere Labs multilingual in-language reasoning text model under the Tiny Aya series.

## Identity and training provenance

- **Tiny Aya L2-Thinker** is the independently published `CohereLabs/tiny-aya-l2-thinker` (multilingual in-language reasoning text model, 3.35B parameters). Distinct 3.35B supervised reasoning fine-tune from Base 32K. It emits a visible thinking trace in the prompt language before its final answer. Cohere reports >93% in-language reasoning over six tests and 60 languages, not independently replicated. [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker) [Cohere research](https://cohere.com/blog/building-multilingual-bridges).

## Selection and operating boundaries

- The checkpoint is text-only, with 32K combined input/output context and published language scope of 44 translated reasoning languages plus English, with broader non-reasoning-language coverage; supported prompt modes and evaluation results are model-specific, not inherited from other Aya releases. [Exact card](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker).
- Downloadable weights require license-gated access under CC-BY-NC-4.0 and Cohere Labs acceptable-use terms; commercial self-hosting, live API hosting, independently repeated benchmarks, actual inference, hardware fit and corporate beneficial ownership are not verified. [Weights](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker) [License](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

The L2-Thinker and En-Thinker have different learned reasoning-language objectives, not a toggle of a shared model; even visible reasoning text does not prove faithful reasoning or factual correctness. Evaluate task-specific accuracy and set output limits. [Research](https://cohere.com/blog/building-multilingual-bridges).

## Catalog relations

- [Tiny Aya](../../../../README.md) — series.
- [Cohere](../../../../../../../../../../../producers/sub/c/sub/cohere/README.md) — co-producer.
- [Tiny Aya Base 32K](../tiny-aya-base-32k/README.md) — confirmed training parent.

## Official resources

- [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker).
- [Cohere research](https://cohere.com/blog/building-multilingual-bridges).
- [CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
