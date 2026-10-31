# Tiny Aya En-Thinker

A separately released 3.35B Cohere/Cohere Labs multilingual English-trace reasoning text model under the Tiny Aya series.

## Identity and training provenance

- **Tiny Aya En-Thinker** is the independently published `CohereLabs/tiny-aya-en-thinker` (multilingual English-trace reasoning text model, 3.35B parameters). Distinct 3.35B supervised fine-tune from Base 32K. The thinking trace is in English, with multilingual user-facing answers. The different training target is not merely a serving toggle of L2-Thinker. [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-en-thinker) [Cohere research](https://cohere.com/blog/building-multilingual-bridges).

## Selection and operating boundaries

- The checkpoint is text-only, with 32K combined input/output context and published language scope of 44 translated reasoning languages plus English, with broader non-reasoning-language coverage; supported prompt modes and evaluation results are model-specific, not inherited from other Aya releases. [Exact card](https://huggingface.co/CohereLabs/tiny-aya-en-thinker).
- Downloadable weights require license-gated access under CC-BY-NC-4.0 and Cohere Labs acceptable-use terms; commercial self-hosting, live API hosting, independently repeated benchmarks, actual inference, hardware fit and corporate beneficial ownership are not verified. [Weights](https://huggingface.co/CohereLabs/tiny-aya-en-thinker) [License](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

The L2-Thinker and En-Thinker have different learned reasoning-language objectives, not a toggle of a shared model; even visible reasoning text does not prove faithful reasoning or factual correctness. Evaluate task-specific accuracy and set output limits. [Research](https://cohere.com/blog/building-multilingual-bridges).

## Catalog relations

- [Tiny Aya](../../../../README.md) — series.
- [Cohere](../../../../../../../../../../../producers/sub/c/sub/cohere/README.md) — co-producer.
- [Tiny Aya Base 32K](../tiny-aya-base-32k/README.md) — confirmed training parent.

## Official resources

- [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-en-thinker).
- [Cohere research](https://cohere.com/blog/building-multilingual-bridges).
- [CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
