# Documentation Requirements

## Identity and provenance

- Command R7B Arabic is the separate February 2025 Cohere/Cohere Labs custom research checkpoint `c4ai-command-r7b-arabic-02-2025`, published in the CohereLabs Hugging Face repository. It is not an alias of December 2024 `c4ai-command-r7b-12-2024`. [Original model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere announcement](https://docs.cohere.com/changelog/command-r7b-arabic).
- Cohere's announcement mistakenly prints `c4ai-command-r7b-12-2024` (including its example) despite announcing Arabic; the authoritative published Arabic repository/model card identifies the distinct `c4ai-command-r7b-arabic-02-2025`. No explicit trained-from relationship is verified, so do not add derivative edges by speculation. [Original model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere announcement](https://docs.cohere.com/changelog/command-r7b-arabic).
- The card explicitly credits development to Cohere and Cohere Labs; record Cohere Labs' exact producer inverse while preserving the existing Command R family and Cohere organizational parent. No additional producer identity. [Original model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).

## Operational decision boundaries

- The approximately 8B parameters comprise roughly 7B transformer plus 1B embedding parameters; this is not an exactly 7B-parameter model. Context is 128K tokens, text-only input/output, centered on Modern Standard Arabic and English. Examples in other training languages do not establish equivalent quality. [Original model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).
- The model's optimized transformer uses local sliding-window attention (4096 token window for three layers) and a global fourth layer; the 128K context is a vendor setting, not independent accuracy/latency proof at full context. [Original model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).
- It supports chat/instruct preamble modes and retrieval-augmented generation through explicitly formatted document snippets and chat templates. Source citations must be checked against supplied snippets; tool execution and retrieval require application logic. [Original model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere announcement](https://docs.cohere.com/changelog/command-r7b-arabic).
- Gated Hugging Face weights are available under CC-BY-NC with Cohere Labs acceptable-use restrictions; no unrestricted commercial permission is implied. The model is distinct from a guarantee of a live Cohere production API route; review deployment eligibility, memory, tokenizer/template, licensing and region separately. [Original model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
- Arabic benchmark improvements are publisher claims, not reproduced AI Lab evaluation. No weight download, inference, license grant beyond stated text, training-parent provenance, beneficial-ownership conclusion or Russian-control tier determination was independently made.

## Validation

- Preserve distinct canonical ID, model type and exact source card; keep one reciprocal Command R membership pair and one Cohere Labs producer pair without inventing derivative lineage.
- Render the full English reader, exposing rights, limits, source discrepancy, quality boundaries, and all links; check parent and producer inverse relations.
- This scoped acceptance does not award downloaded-weight/runtime/benchmark, global schema/cache/CI, clean-catalog-pass or final publication-gate credit.
