# North Small Translate 1.0

North Small Translate 1.0 is Cohere’s sparse translation model with 218B total parameters and 25B active per token.

## Identity and provenance

The card explicitly credits Cohere and Cohere Labs. North-Small-Translate-1.0 is the weight identity; the current Cohere API identifier is north-small-translate-09-2026. Similar scale to A+ is not evidence of a derivation relation. [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).

## Decision and operating boundaries

- The card specifies 16K input and 16K output and lists 50 languages or locale variants; current provider documentation describes more than 50. The current API table lists a 16K context and 16K output; do not double that into a claimed 32K input window. [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The research weights state CC-BY-NC 4.0 with an acceptable-use policy, not Apache 2.0. BF16, FP8 and W4A16 are distributions of the same model; any hardware fit depends on the chosen precision, full model storage, context and runtime. [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
- Use the documented target-language controls and evaluate terminology and meaning on the intended language pair. The model is a translation specialist; model size and provider benchmark positioning do not guarantee a particular translation is correct. [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0) [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0).

## Catalog relations

- [Cohere Labs](../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [North](../../../../) — series or family.

## Official resources

- [North Small Translate documentation](https://docs.cohere.com/docs/north-small-translate-1.0).
- [North Small Translate launch article](https://cohere.com/blog/north-small-translate).
- [North Small Translate model card](https://huggingface.co/CohereLabs/North-Small-Translate-1.0).
- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license).
- [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
