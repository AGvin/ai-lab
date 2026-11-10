# Documentation Requirements

## Identity and provenance

- North groups Cohere’s specialized coding, translation and compact vision-language models.
- The materialized members are North Mini Code 1.0, its separate Eagle speculative-decoding draft component, North Small Translate 1.0 and North Micro Vision Instruct. This model family is separate from the North workspace application and from a hosting provider. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [North Mini Code documentation](https://docs.cohere.com/docs/north-mini-code-1.0) [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- Mini Code and Small Translate cards explicitly co-credit Cohere Labs; the Micro Vision card credits Cohere. The family’s canonical Cohere placement is preserved without generalizing a per-model co-development claim. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

## Operational decision boundaries

- These releases have different purposes, scale and rights: North Mini Code, its Eagle draft component and compact vision weights state Apache 2.0; Small Translate states CC-BY-NC. Shared naming does not establish a shared checkpoint, training lineage or license. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- A sparse model’s active parameter count, a language backbone’s maximum context and a quantized file’s size describe different deployment constraints. Use each concrete model’s validated operating range and chosen runtime. [North Mini Code model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

- The separately released North Mini Code Eagle draft has its own small learned parameters for speculative decoding and is not a standalone 30B code-generation checkpoint, FP8 quantization or guaranteed decoder replacement. Its Hugging Face card describes three dense sliding-window draft layers and compatible target serving via vLLM; the 320,000-token example is a **target server setting**, not independently established Eagle context capacity. Do not infer a `derived-from` training relationship from runtime compatibility. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle) [North Mini Code base card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
