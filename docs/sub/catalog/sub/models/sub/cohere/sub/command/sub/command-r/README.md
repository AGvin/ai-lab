# Command R

The Command R series groups the August 2024 R and R+ releases and Command R7B from December 2024.

## Identity and provenance

The catalog materializes three dated models. Their versioned API identifiers are distinct from the older undated R/R+ aliases, which the current lifecycle table maps to deprecated March/April 2024 releases. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Decision and operating boundaries

- The August R card reports 32B parameters, R+ reports 104B, and R7B uses a 7B-class name. All three advertise a 128K context and the current API table lists a 4K maximum output; those limits are not a guarantee of quality throughout the window. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The weight cards state CC-BY-NC research terms and model-specific templates for grounded generation and tools. A tool-capable model requests actions; connected application software performs them. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
- Choose exact version and deployment from current documentation. August release throughput and latency comparisons are provider measurements, not reproduced runtime results. [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Catalog relations

- [Command](../../) — series or family.
- [Command R 08-2024](sub/models/sub/command-r-08-2024/) — member.
- [Command R+ 08-2024](sub/models/sub/command-r-plus-08-2024/) — member.
- [Command R7B](sub/models/sub/command-r7b-12-2024/) — member.

## Official resources

- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Command R7B documentation](https://docs.cohere.com/docs/command-r7b).
- [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).
- [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024).
- [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024).
- [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
