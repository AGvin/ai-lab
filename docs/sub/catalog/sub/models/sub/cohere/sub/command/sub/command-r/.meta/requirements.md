# Documentation Requirements

## Identity and provenance

- The Command R series groups original March/April 2024 R/R+, August 2024 refreshes, December 2024 Command R7B, and the February 2025 Arabic research checkpoint.
- Six dated models are now materialized. The original 35B March Command R and 104B April Command R+ are distinct trained releases from the August 2024 updates. Their old hosted API IDs and unversioned aliases were deprecated on September 15, 2025. [Historical identifiers](https://docs.cohere.com/v1/docs/models) [Deprecations](https://docs.cohere.com/docs/deprecations) [Original R card](https://huggingface.co/CohereLabs/c4ai-command-r-v01) [Original R+ card](https://huggingface.co/CohereLabs/c4ai-command-r-plus). [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

- Command R7B Arabic is a separate Cohere/Cohere Labs research model with Arabic/English emphasis, a gated CC-BY-NC weight card, 128K context and ~8B total parameters (7B transformer + 1B embeddings). The release note mistakenly quotes the older December checkpoint ID; use the explicit 2025 Hugging Face model identifier, not that copied example, for provenance. There is no source-proven derived-from link to the December weights. [Command R7B Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Arabic release note](https://docs.cohere.com/changelog/command-r7b-arabic).

## Operational decision boundaries

- The original 2024 R/R+ model cards specify 128K text context and gated CC-BY-NC-4.0 research weights. The historical API table lists a 4K maximum hosted output; deprecated routes are unsuitable for new integration. Local inference limits and benchmark quality have not been independently verified. [Original R card](https://huggingface.co/CohereLabs/c4ai-command-r-v01) [Original R+ card](https://huggingface.co/CohereLabs/c4ai-command-r-plus) [Historical model table](https://docs.cohere.com/v1/docs/models).
- The August R card reports 32B parameters, R+ reports 104B, and R7B uses a 7B-class name. The three earlier models advertise a 128K context and the current API table lists a 4K maximum output; the Arabic research release separately specifies 128K context without establishing the same service output cap; those limits are not a guarantee of quality throughout the window. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The weight cards state CC-BY-NC research terms and model-specific templates for grounded generation and tools. A tool-capable model requests actions; connected application software performs them. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
- Choose exact version and deployment from current documentation. August release throughput and latency comparisons are provider measurements, not reproduced runtime results. [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
