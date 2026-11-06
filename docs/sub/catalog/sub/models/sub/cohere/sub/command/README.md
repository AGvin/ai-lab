# Command

Command is Cohere’s language-model family, organized here into the Command A and Command R series.

## Identity and provenance

The family groups concrete versioned models; A, A+, A Reasoning, A Translate, A Vision, R, R+ and R7B have distinct identities and operating boundaries. Family membership does not establish checkpoint derivation. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).

## Decision and operating boundaries

- Use the exact versioned API identifier and matching weight card. Text-only generation, image understanding, reasoning and translation differ across members; A Vision does not generate images or support the same tool-use contract as text Command models. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command A Vision documentation](https://docs.cohere.com/docs/command-a-vision).
- The reviewed A/R research weights generally state CC-BY-NC with an acceptable-use policy, while A+ states Apache 2.0. The family has no single weight license; hosted access terms are separate. [Command A model card](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024).
- Current lifecycle documentation distinguishes live August 2024 R/R+ models and December R7B from the deprecated March/April 2024 releases and their undated aliases. Older documentation calling A the latest model is not a current family-wide ordering rule. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command R documentation](https://docs.cohere.com/docs/command-r).

## Catalog relations

- [Cohere](../../../../../producers/sub/c/sub/cohere/) — producer.
- [Command A](sub/command-a/) — member.
- [Command R](sub/command-r/) — member.

## Official resources

- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Command A Vision documentation](https://docs.cohere.com/docs/command-a-vision).
- [Command A model card](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025).
- [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16).
- [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024).
- [Command R documentation](https://docs.cohere.com/docs/command-r).
