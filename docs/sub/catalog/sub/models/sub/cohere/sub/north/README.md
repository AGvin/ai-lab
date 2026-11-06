# North

North groups Cohere’s specialized coding, translation and compact vision-language models.

## Identity and provenance

The materialized members are North Mini Code 1.0, its separate Eagle speculative-decoding draft component, North Small Translate 1.0 and North Micro Vision Instruct. This model family is separate from the North workspace application and from a hosting provider. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [North Mini Code documentation](https://docs.cohere.com/docs/north-mini-code-1.0) [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

Mini Code and Small Translate cards explicitly co-credit Cohere Labs; the Micro Vision card credits Cohere. The family’s canonical Cohere placement is preserved without generalizing a per-model co-development claim. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

## Decision and operating boundaries

- These releases have different purposes, scale and rights: North Mini Code, its Eagle draft component and compact vision weights state Apache 2.0; Small Translate states CC-BY-NC. Shared naming does not establish a shared checkpoint, training lineage or license. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- A sparse model’s active parameter count, a language backbone’s maximum context and a quantized file’s size describe different deployment constraints. Use each concrete model’s validated operating range and chosen runtime. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

- North Mini Code Eagle is a separately published small speculative-decoding draft model for the Mini Code target, not a substitute generator or a context-extension guarantee. A 320,000-token vLLM example is a server configuration, not standalone draft model context evidence; speedups and FP8/W4A16 compatibility are publisher claims. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).

## Catalog relations

- [Cohere](../../../../../producers/sub/c/sub/cohere/) — producer.
- [North Micro Vision Instruct](sub/models/sub/north-micro-vision-instruct/) — member.
- [North Mini Code 1.0](sub/models/sub/north-mini-code-1-0/) — member.
- [North Mini Code Eagle draft](sub/models/sub/north-mini-code-1-0-eagle/) — member.
- [North Small Translate 1.0](sub/models/sub/north-small-translate-1-0/) — member.

## Official resources

- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [North Mini Code documentation](https://docs.cohere.com/docs/north-mini-code-1.0).
- [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0).
- [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).
- [North Mini Code Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0).
