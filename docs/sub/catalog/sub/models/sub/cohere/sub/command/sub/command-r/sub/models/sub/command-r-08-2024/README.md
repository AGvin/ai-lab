# Command R 08-2024

Command R 08-2024 is the 32B August 2024 text model for grounded generation, conversation and tool use.

## Identity and provenance

The exact card reports 32B parameters and explicitly credits Cohere and Cohere Labs. The original c4ai-command-r-v01 card describes a different 35B release; that older scale must not be copied onto this dated model. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Original Command R model card](https://huggingface.co/CohereLabs/c4ai-command-r-v01).

command-r-08-2024 is currently live. The deprecated undated command-r alias refers to the March 2024 release rather than this August model. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Decision and operating boundaries

- The documented context is 128K, with a 4K maximum API output. Sources distinguish ten optimized or evaluated languages from thirteen additional pretraining languages; this is not uniform demonstrated quality in every language. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command R documentation](https://docs.cohere.com/docs/command-r) [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024).
- Use the exact grounding and tool prompt templates. The model can request tools and generate cited answers over supplied snippets, while retrieval, tool execution and verification belong to the application. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R documentation](https://docs.cohere.com/docs/command-r).
- The public research weights state CC-BY-NC 4.0 with an acceptable-use policy. August-release throughput and latency improvements are source-specific comparisons; no runtime result or commercial downloaded-weight permission is inferred here. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Catalog relations

- [Cohere Labs](../../../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Command R](../../../../) — series or family.

## Official resources

- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024).
- [Original Command R model card](https://huggingface.co/CohereLabs/c4ai-command-r-v01).
- [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).
- [Command R documentation](https://docs.cohere.com/docs/command-r).
- [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
