# Command R7B

Command R7B is the December 2024 compact text model for multilingual grounded generation and tool use.

## Identity and provenance

The exact card identifies c4ai-command-r7b-12-2024 and explicitly credits Cohere and Cohere Labs. R7B is the producer’s 7B-class naming; public tensor metadata reports 8,028,033,024 stored parameters, so the name is not asserted as an exact total. [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024) [Command R7B model card public metadata](https://huggingface.co/api/models/CohereLabs/c4ai-command-r7b-12-2024?blobs=true).

Aya Vision 8B’s official card explicitly bases its language component on this exact Command R7B release, with further Aya Expanse-style post-training. The reciprocal derivative relation targets Aya Vision 8B alone, not the entire Aya Vision series. [Aya Vision 8B model card](https://huggingface.co/CohereLabs/aya-vision-8b).

## Decision and operating boundaries

- The live API identifier is command-r7b-12-2024, with a 128K context and a 4K maximum output. The card documents 23 languages and an attention pattern of three sliding-window layers followed by a global layer. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command R7B documentation](https://docs.cohere.com/docs/command-r7b) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
- Use the matching chat, grounding and tool templates. Tool requests require application execution, and generated citations require checking against supplied sources; compact scale does not remove these boundaries. [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024) [Command R7B documentation](https://docs.cohere.com/docs/command-r7b).
- Research weights state CC-BY-NC 4.0 plus the acceptable-use policy. Command R7B Arabic is a distinct source-discovered release outside this existing-node assessment; it is not an alias of the December model. [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024) [Command R7B Arabic discovery](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Catalog relations

- [Aya Vision 8B](../../../../../../../../../cohere-labs/sub/aya/sub/aya-vision/sub/models/sub/aya-vision-8b/) — derivative.
- [Cohere Labs](../../../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Command R](../../../../) — series or family.

## Official resources

- [Command R7B documentation](https://docs.cohere.com/docs/command-r7b).
- [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
- [Command R7B model card public metadata](https://huggingface.co/api/models/CohereLabs/c4ai-command-r7b-12-2024?blobs=true).
- [Aya Vision 8B model card](https://huggingface.co/CohereLabs/aya-vision-8b).
- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Command R7B Arabic discovery](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).
- [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
