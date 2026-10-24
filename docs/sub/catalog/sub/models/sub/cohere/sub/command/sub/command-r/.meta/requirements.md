# Documentation Requirements

## Identity and provenance

- The Command R series groups the August 2024 R and R+ releases and Command R7B from December 2024.
- The catalog materializes three dated models. Their versioned API identifiers are distinct from the older undated R/R+ aliases, which the current lifecycle table maps to deprecated March/April 2024 releases. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Operational decision boundaries

- The August R card reports 32B parameters, R+ reports 104B, and R7B uses a 7B-class name. All three advertise a 128K context and the current API table lists a 4K maximum output; those limits are not a guarantee of quality throughout the window. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The weight cards state CC-BY-NC research terms and model-specific templates for grounded generation and tools. A tool-capable model requests actions; connected application software performs them. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
- Choose exact version and deployment from current documentation. August release throughput and latency comparisons are provider measurements, not reproduced runtime results. [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
