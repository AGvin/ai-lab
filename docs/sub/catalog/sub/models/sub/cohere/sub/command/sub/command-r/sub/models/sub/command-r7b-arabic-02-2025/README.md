# Command R7B Arabic

Command R7B Arabic is a separately published Cohere and Cohere Labs research language model optimized for Modern Standard Arabic and English.

## Identity and provenance

The original CohereLabs card identifies `c4ai-command-r7b-arabic-02-2025` as a distinct February 2025 research release. Cohere's release-note example incorrectly uses the older `c4ai-command-r7b-12-2024` identifier. Use the published Arabic model repository for exact provenance; do not mistake the model for a December R7B alias or invent a parent/derivative relation. [Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere announcement](https://docs.cohere.com/changelog/command-r7b-arabic).

## Decision and operating boundaries

- Model size is approximately 8B total, with ~7B transformer parameters and ~1B embeddings. Context is 128K tokens, with text-only input/output and Arabic/English target evaluation. Neither the "R7B" name nor training data in additional languages establishes a 7B exact count or equal multilingual quality. [Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).
- The card describes hybrid attention with three 4,096-token sliding-window layers followed by a global layer, plus supervised/preference post-training. Runtime speed, RAM/VRAM, and long-context accuracy are not independently measured in this catalog. [Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).
- Chat/instruct prompts and document-aware RAG templates need the matching tokenizer and application-side supplied documents. Inline citations are generated text that must be checked; the model alone does not retrieve source material or execute tools. [Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere announcement](https://docs.cohere.com/changelog/command-r7b-arabic).
- Weights are gated on Hugging Face, licensed CC-BY-NC with additional Cohere Labs acceptable-use restrictions. Do not treat accessible repository metadata, a playground, or a model card as unrestricted commercial deployment rights or guaranteed public inference endpoint. [Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere Labs license](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
- Reported Arabic benchmark gains are vendor claims, not independent AI Lab tests. Exact training lineage, live API service eligibility, beneficial ownership and partial Russian-origin interests were not independently verified.

## Catalog relations

- [Cohere Labs](../../../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Command R](../../../../) — series or family.

## Official resources

- [Command R7B Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).
- [Cohere Arabic release notes](https://docs.cohere.com/changelog/command-r7b-arabic).
- [Cohere Labs license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
