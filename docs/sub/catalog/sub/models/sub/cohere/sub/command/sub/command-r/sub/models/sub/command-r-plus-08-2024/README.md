# Command R+ 08-2024

Command R+ 08-2024 is the 104B August 2024 text model for complex grounded generation and multistep tool workflows.

## Identity and provenance

The exact model card reports 104B parameters and identifies the dated R+ release. Its text describes a joint Cohere/Cohere Labs release family, but this audit does not turn that wording into an explicit new co-producer edge for this particular model. Cohere provenance remains through Command family membership. [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024).

command-r-plus-08-2024 is live in the current API table. The undated command-r-plus alias names the deprecated April 2024 release; it is not an alias for this model. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Decision and operating boundaries

- The documented context is 128K with a 4K maximum API output. Ten optimized languages and thirteen additional pretraining languages are reported separately; retrieved current sources are needed for facts beyond the model’s training cutoff. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command R+ documentation](https://docs.cohere.com/docs/command-r-plus) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024).
- Grounded generation and multistep tool use require the matching templates and an application that supplies retrieval results, executes calls and validates outcomes. Larger scale or generated citations do not guarantee correctness. [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R+ documentation](https://docs.cohere.com/docs/command-r-plus).
- Research weights state CC-BY-NC 4.0 with an acceptable-use policy. Provider efficiency comparisons and hosted terms remain separate from local runtime validation and permission to operate downloaded weights commercially. [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Catalog relations

- [Command R](../../../../) — series or family.

## Official resources

- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024).
- [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).
- [Command R+ documentation](https://docs.cohere.com/docs/command-r-plus).
- [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
