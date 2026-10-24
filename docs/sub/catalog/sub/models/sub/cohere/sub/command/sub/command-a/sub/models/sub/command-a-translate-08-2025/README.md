# Command A Translate

Command A Translate is the 111B August 2025 model specialized for translation across 23 languages.

## Identity and provenance

The model card explicitly credits Cohere and Cohere Labs and identifies command-a-translate-08-2025. Official Hub metadata lists Command A as its base; North Small Translate remains a separate later model. [Command A Translate model card](https://huggingface.co/CohereLabs/command-a-translate-08-2025) [Command A Translate model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-translate-08-2025?blobs=true) [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0).

## Decision and operating boundaries

- The card specifies 8K input and 8K output. The dedicated documentation describes their combined 16K budget, while the current model table lists 8K context and 8K output; preserve the explicit input/output split instead of claiming a 16K input window. [Command A Translate model card](https://huggingface.co/CohereLabs/command-a-translate-08-2025) [Command A Translate documentation](https://docs.cohere.com/docs/command-a-translate) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The documented 23-language set includes Ukrainian, Arabic, Japanese and Korean. Set the requested target language and evaluate terminology, omitted text and meaning preservation on representative material; advertised translation quality is not a per-document guarantee. [Command A Translate documentation](https://docs.cohere.com/docs/command-a-translate) [Command A Translate model card](https://huggingface.co/CohereLabs/command-a-translate-08-2025).
- The released research weights state CC-BY-NC 4.0 with the additional acceptable-use policy. The API identifier remains live, but hosted contracts do not grant commercial operation of the downloaded weights. [Command A Translate model card](https://huggingface.co/CohereLabs/command-a-translate-08-2025) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Catalog relations

- [Cohere Labs](../../../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Command A](../../../../) — series or family.
- [Command A](../command-a-03-2025/) — derived from.

## Official resources

- [Command A Translate documentation](https://docs.cohere.com/docs/command-a-translate).
- [Command A Translate release](https://docs.cohere.com/v1/changelog/2025-08-28-command-a-translate).
- [Command A Translate model card](https://huggingface.co/CohereLabs/command-a-translate-08-2025).
- [Command A Translate model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-translate-08-2025?blobs=true).
- [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0).
- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
